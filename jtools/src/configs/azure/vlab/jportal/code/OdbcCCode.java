/// ------------------------------------------------------------------
/// Copyright (c) from 1996 Vincent Risi
///
/// All rights reserved.
/// This program and the accompanying materials are made available
/// under the terms of the Common Public License v1.0
/// which accompanies this distribution and is available at
/// http://www.eclipse.org/legal/cpl-v10.html
/// Contributors:
///    Vincent Risi
/// ------------------------------------------------------------------
package configs.azure.vlab.jportal.code;

import java.io.*;
import java.util.*;

import static azure.vlab.jportal.Writer.*;

import azure.vlab.jportal.*;
import vlab.jportal.*;

public class OdbcCCode extends Generator
{
  protected static PrintWriter outLog;

  static public String description()
  {
    return "Generate ODBC C++ Code";
  }

  static public String documentation()
  {
    return "Generate ODBC C++ Code";
  }

  static private PlaceHolder placeHolder;
  static private byte paramStyle = PlaceHolder.QUESTION;

  /**
   * Generates the procedure classes for each table present.
   */
  static public void generate(Database database, String output, PrintWriter outLog)
  {
    OdbcCCode.outLog = outLog;
    loadProperties(database, output);
    getFlags(database);
    for (int i = 0; i < database.tables.size(); i++)
    {
      try
      {
        Table table = database.tables.elementAt(i);
        generate(table, output);
        TJCStructs.generateSnips(table, output, outLog, true);
      }
      catch (Exception ex)
      {
        outLog.println(ex);
        ex.printStackTrace(outLog);
      }
    }
  }

  static private void loadProperties(Database database, String output)
  {
    Properties properties;
    try
    {
      String propertiesName = format("%s%s.properties", output, database.name);
      InputStream input = new FileInputStream(propertiesName);
      properties = new Properties();
      properties.load(input);
    }
    catch (Exception ex)
    {
      properties = null;
    }
  }

  static private String cppRetType;

  static private void setParamStyle(String flag)
  {
    if (flag.equalsIgnoreCase("oracle"))
    {
      paramStyle = PlaceHolder.COLON;
      cppRetType = "ORACLE";
    }
    else if (flag.equalsIgnoreCase("db2"))
    {
      paramStyle = PlaceHolder.QUESTION;
      cppRetType = "DB2";
    }
    else if (flag.equalsIgnoreCase("mssql"))
    {
      paramStyle = PlaceHolder.AT;
      cppRetType = "MSSQL";
    }
    else if (flag.equalsIgnoreCase("mysql"))
    {
      paramStyle = PlaceHolder.AT_NAMED;
      cppRetType = "MYSQL";
    }
    else if (flag.equalsIgnoreCase("postgre"))
    {
      paramStyle = PlaceHolder.AT_NAMED;
      cppRetType = "POSTGRE";
    }
  }

  static private boolean useLongAsChar()
  {
    return cppRetType.equalsIgnoreCase("ORACLE");
  }

  static private void getFlags(Database database)
  {
    for (int i = database.flags.size() - 1; i >= 0; i--)
    {
      boolean dropFlag = false;
      String flag = database.flags.elementAt(i);
      flag = flag.toLowerCase();
      if (flag.startsWith("%"))
      {
        dropFlag = true;
        flag = flag.substring(1);
      }
      if (flag.startsWith("odbc="))
        setParamStyle(flag.substring(5));
      if (dropFlag)
        database.flags.remove(i);
    }
  }

  /**
   * Build of standard and user defined procedures
   */
  static public void generate(Table table, String output) throws Exception
  {
    outLog.println("Code: " + fileName(output, table.useName().toLowerCase(), ".sh"));
    try (PrintWriter outData = new PrintWriter(new FileOutputStream(fileName(output, table.useName().toLowerCase(), ".sh"))))
    {
      writer = outData;
      indent_size = 4;
      writeln("// This code was generated, do not modify it, modify it at source and regenerate it.");
      writeln("#ifndef _" + table.useName().toLowerCase() + "SH");
      writeln("#define _" + table.useName().toLowerCase() + "SH");
      writeln();
      writeln("#include <stddef.h>");
      writeln("#include \"padgen.h\"");
      writeln("#include \"odbcapi.h\"");
      writeln("#include \"swapbytes.h\"");
      writeln();
      if (table.hasStdProcs)
        TJCStructs.generateStdOutputRec(table);
      TJCStructs.generateUserOutputRecs(table);
      generateInterface(table);
      writeln("#endif");
      writer.flush();
    }
    outLog.println("Code: " + fileName(output, table.useName().toLowerCase(), ".cpp"));
    try (PrintWriter outData = new PrintWriter(new FileOutputStream(fileName(output, table.useName().toLowerCase(), ".cpp"))))
    {
      writer = outData;
      indent_size = 4;
      writeln("// This code was generated, do not modify it, modify it at source and regenerate it.");
      writeln();
      writeln("#include \"" + fileName("", table.useName().toLowerCase(), ".sh") + "\"");
      writeln();
      generateImplementation(table);
      writer.flush();
    }
  }

  /**
   * Build of output data rec for standard procedures
   */
  static private void generateInterface(Table table)
  {
    for (int i = 0; i < table.procs.size(); i++)
    {
      Proc proc = table.procs.elementAt(i);
      if (proc.isData)
        continue;
      generateInterface(table, proc);
    }
  }

  /**
   * Emits class method for processing the database activity
   */
  static private void generateInterface(Table table, Proc proc)
  {
    String dataStruct;
    if (proc.comments.size() > 0)
      for (int i = 0; i < proc.comments.size(); i++)
      {
        String comment = proc.comments.elementAt(i);
        writeln(1, "//" + comment);
      }
    if (proc.hasNoData())
    {
      writeln("struct T" + table.useName() + proc.upperFirst());
      writeln("{");
      writeln(1, "TJQuery q_;");
      writeln(1, "void Exec();");
      writeln(1, "T" + table.useName() + proc.upperFirst() + "(TJConnector &conn, char *aFile=__FILE__, long aLine=__LINE__)");
      writeln(1, ": q_(conn)");
      writeln(1, "{q_.FileAndLine(aFile,aLine);}");
      writeln("};");
      writeln();
    }
    else
    {
      if (proc.isStdExtended() || proc.isStd)
        dataStruct = "D" + table.useName();
      else
        dataStruct = "D" + table.useName() + proc.upperFirst();
      writeln("struct T" + table.useName() + proc.upperFirst() + " : public " + dataStruct);
      writeln("{");
      generateInterface(table, proc, dataStruct);
      writeln("};");
      writeln();
    }
  }

  /**
   *
   */
  static private void generateImplementation(Table table)
  {
    for (int i = 0; i < table.procs.size(); i++)
    {
      Proc proc = table.procs.elementAt(i);
      if (proc.isData)
        continue;
      if (proc.isMultipleInput)
        generateMultipleImplementation(table, proc);
      else
        generateImplementation(table, proc);
    }
  }

  static private String useNull(Field field)
  {
    if (isNull(field)
        || (field.type == Field.CHAR && field.isNull == true)
        || (field.type == Field.ANSICHAR && field.isNull == true))
      return ", " + field.useName() + "IsNull);";
    return ");";
  }

  static private void generateMultipleImplementation(Table table, Proc proc)
  {
    placeHolder = new PlaceHolder(proc, paramStyle, "");
    String dataStruct;
    if (proc.isStdExtended() || proc.isStd)
      dataStruct = "D" + table.useName();
    else
      dataStruct = "D" + table.useName() + proc.upperFirst();
    String fullName = table.useName() + proc.upperFirst();
    writeln("void T" + fullName + "::Exec(int32 noOf, " + dataStruct + " *Recs)");
    writeln("{");
    generateCommand(proc);
    writeln(1, "q_.OpenArray(q_.command, NOBINDS, NONULLS, noOf, ROWSIZE+32);");
    for (int i = 0, n = 0; i < proc.inputs.size(); i++)
    {
      Field field = proc.inputs.elementAt(i);
      writeln(1, "" + cppArrayPointer(field));
      if (isNull(field))
        writeln(1, "SQLINTEGER* " + field.useName() + "IsNull = &q_.indicators[noOf*" + n++ + "];");
      else if (field.type == Field.CHAR && field.isNull == true)
        writeln(1, "SQLINTEGER* " + field.useName() + "IsNull = &q_.indicators[noOf*" + n++ + "];");
      else if (field.type == Field.ANSICHAR && field.isNull == true)
        writeln(1, "SQLINTEGER* " + field.useName() + "IsNull = &q_.indicators[noOf*" + n++ + "];");

    }
    writeln(1, "for (int i=0; i<noOf; i++)");
    writeln(1, "{");
    for (int i = 0; i < proc.inputs.size(); i++)
    {
      Field field = proc.inputs.elementAt(i);
      writeln(2, "" + cppArrayCopy(field));
      if (isNull(field))
        writeln(2, "" + field.useName() + "IsNull[i] = Recs[i]." + field.useName() + "IsNull;");
      else if (field.type == Field.CHAR && field.isNull == true)
        writeln(2, "" + field.useName() + "IsNull[i] = strlen(Recs[i]." + field.useName() + ") == 0 ? JP_NULL : SQL_NTS;");
      else if (field.type == Field.ANSICHAR && field.isNull == true)
        writeln(2, "" + field.useName() + "IsNull[i] = strlen(Recs[i]." + field.useName() + ") == 0 ? JP_NULL : SQL_NTS;");
    }
    writeln(1, "}");
    for (int i = 0; i < placeHolder.pairs.size(); i++)
    {
      PlaceHolderPairs pair = placeHolder.pairs.elementAt(i);
      Field field = pair.field;
      String size = field.useName().toUpperCase() + "_SIZE";
      switch (field.type)
      {
        case Field.ANSICHAR:
          writeln(1, "q_.BindAnsiCharArray(" + i + ", " + field.useName() + ", " + size + useNull(field));
          break;
        case Field.CHAR:
        case Field.TLOB:
        case Field.XML:
        case Field.USERSTAMP:
          writeln(1, "q_.BindCharArray(" + i + ", " + field.useName() + ", " + size + useNull(field));
          break;
        case Field.LONG:
        case Field.BIGSEQUENCE:
        case Field.BIGIDENTITY:
          writeln(1, "q_.BindInt64Array(" + i + ", " + field.useName() + useNull(field));
          break;
        case Field.INT:
        case Field.SEQUENCE:
        case Field.IDENTITY:
          writeln(1, "q_.BindInt32Array(" + i + ", " + field.useName() + useNull(field));
          break;
        case Field.BOOLEAN:
        case Field.BYTE:
        case Field.SHORT:
          writeln(1, "q_.BindInt16Array(" + i + ", " + field.useName() + useNull(field));
          break;
        case Field.FLOAT:
        case Field.DOUBLE:
          if (field.precision <= 15)
            writeln(1, "q_.BindDoubleArray(" + i + ", " + field.useName() + ", " + (field.precision) + ", " + (field.scale) + useNull(field));
          else
            writeln(1, "q_.BindMoneyArray(" + i + ", " + field.useName() + ", " + (field.precision) + ", " + (field.scale) + useNull(field));
          break;
        case Field.MONEY:
          writeln(1, "q_.BindMoneyArray(" + i + ", " + field.useName() + ", 18, 2" + useNull(field));
          break;
        case Field.DATE:
          writeln(1, "q_.BindDateArray(" + i + ", " + field.useName() + useNull(field));
          break;
        case Field.TIME:
          writeln(1, "q_.BindTimeArray(" + i + ", " + field.useName() + useNull(field));
          break;
        case Field.DATETIME:
        case Field.TIMESTAMP:
          writeln(1, "q_.BindDateTimeArray(" + i + ", " + field.useName() + useNull(field));
          break;
        case Field.AUTOTIMESTAMP:
          writeln(1, "//q_.BindDateTimeArray(" + i + ", " + field.useName() + useNull(field));
          break;
      }
    }
    writeln(1, "q_.Exec();");
    writeln("}");
    writeln();
  }

  /**
   * Emits class method for processing the database activity
   */
  static private boolean isIdentity(Field field)
  {
    return field.type == Field.BIGIDENTITY || field.type == Field.IDENTITY;
  }

  static private boolean isSequence(Field field)
  {
    return field.type == Field.BIGSEQUENCE || field.type == Field.SEQUENCE;
  }

  static private void generateImplementation(Table table, Proc proc)
  {
    boolean doReturning = false;
    placeHolder = new PlaceHolder(proc, paramStyle, "");
    String fullName = table.useName() + proc.upperFirst();
    writeln("void T" + fullName + "::Exec()");
    writeln("{");
    generateCommand(proc);
    if (proc.isInsert == true && proc.hasReturning == true && proc.outputs.size() == 1)
    {
      writeln(1, format("q_.Open(q_.command, %d);", proc.inputs.size() + 1));
      Field field = proc.outputs.elementAt(0);
      generateCppBind(field);
      doReturning = true;
    }
    else if (proc.outputs.size() > 0)
      writeln(1, "q_.Open(q_.command, NOBINDS, NODEFINES, NOROWS, ROWSIZE+32);");
    else if (proc.inputs.size() > 0)
      writeln(1, "q_.Open(q_.command, " + proc.inputs.size() + ");");
    else
      writeln(1, "q_.Open(q_.command);");
    for (int j = 0; j < proc.inputs.size(); j++)
    {
      Field field = proc.inputs.elementAt(j);
      generateCppBind(field);
    }
    boolean hasBlob = false;
    Vector<Field> blobs = new Vector<>();
    for (int j = 0; j < placeHolder.pairs.size(); j++)
    {
      PlaceHolderPairs pair = placeHolder.pairs.elementAt(j);
      Field field = pair.field;
      String tablename = table.tableName();
      String bind = "Bind";
      String TYPEOF = "";
      if (field.type == Field.BLOB || field.type == Field.TLOB || field.type == Field.IMAGE)
      {
        TYPEOF = "Blob";
        hasBlob = true;
      }
      else if (field.type == Field.UNICODE)
        TYPEOF = "Unicode";
      else if (field.type == Field.UTF8)
        TYPEOF = "Utf8";
      writeln(1, "q_." + bind + TYPEOF + "(" + TJCStructs.padder("" + j + ",", 4) + cppBind(field, tablename, proc.isInsert) + TJCStructs.padder(", " + cppDirection(field), 4) + ((isNull(field)) ? ", &" + field.useName() + "IsNull" : "") + charFieldFlag(field) + ");");
      if (field.type == Field.BLOB || field.type == Field.TLOB || field.type == Field.IMAGE)
        blobs.addElement(field);
    }
    if (doReturning)
    {
      Field field = proc.outputs.elementAt(0);
      int pos = proc.inputs.size();
      writeln(1, format("q_.Bind(%d, %s, SQL_PARAM_INPUT);", pos, cppBind(field)));
    }
    else
    {
      for (int j = 0; j < proc.outputs.size(); j++)
      {
        Field field = proc.outputs.elementAt(j);
        String TYPEOF = "";
        if (field.type == Field.BLOB || field.type == Field.TLOB || field.type == Field.IMAGE)
          TYPEOF = "Blob";
        else if (field.type == Field.UNICODE)
          TYPEOF = "Unicode";
        else if (field.type == Field.UTF8)
          TYPEOF = "Utf8";
        writeln(1, "q_.Define" + TYPEOF + "(" + TJCStructs.padder("" + j + ",", 4) + cppDefine(field) + ");");
      }
    }
    writeln(1, "q_.Exec();");
    if (doReturning && useLongAsChar())
    {
      Field field = proc.outputs.elementAt(0);
      if (field.type == Field.BIGSEQUENCE)
        writeln(1, format("%s = atoll(%s_ODBC_LONG);", field.useName(), field.useName()));
    }
    for (int j = 0; j < blobs.size(); j++)
    {
      Field field = blobs.elementAt(j);
      writeln(1, "SwapBytes(" + field.useName() + ".len); // fixup len in data on intel type boxes");
    }
    writeln("}");
    writeln();
    boolean skipExecWithParms = false;
    for (int j = 0; j < proc.inputs.size(); j++)
    {
      Field field = proc.inputs.elementAt(j);
      if (field.type == Field.BLOB)
      {
        skipExecWithParms = true;
        break;
      }
    }
    if (skipExecWithParms == false)
      if ((proc.inputs.size() > 0) || proc.dynamics.size() > 0)
      {
        writeln("void T" + fullName + "::Exec(");
        generateWithParms(proc, "");
        writeln(")");
        writeln("{");
        for (int j = 0; j < proc.inputs.size(); j++)
        {
          Field field = proc.inputs.elementAt(j);
          if ((isSequence(field) && proc.isInsert)
              || isIdentity(field)
              || field.type == Field.TIMESTAMP
              || field.type == Field.AUTOTIMESTAMP
              || field.type == Field.USERSTAMP)
            continue;
          writeln(1, "" + cppCopy(field));
        }
        for (int j = 0; j < proc.dynamics.size(); j++)
        {
          String s = proc.dynamics.elementAt(j);
          writeln(1, "strncpy(" + s + ", a" + s + ", sizeof(" + s + ")-1);");
        }
        writeln(1, "Exec();");
        writeln("}");
        writeln();
      }
    if (proc.outputs.size() > 0)
    {
      writeln("bool T" + fullName + "::Fetch()");
      writeln("{");
      writeln(1, "if (q_.Fetch() == false)");
      writeln(2, "return false;");
      for (int j = 0; j < proc.outputs.size(); j++)
      {
        Field field = proc.outputs.elementAt(j);
        String TYPEOF = "";
        if (field.type == Field.BLOB || field.type == Field.TLOB || field.type == Field.IMAGE)
          TYPEOF = "Blob";
        else if (field.type == Field.UNICODE)
          TYPEOF = "Unicode";
        else if (field.type == Field.UTF8)
          TYPEOF = "Utf8";
        writeln(1, "q_.Get" + TYPEOF + "(" + cppGet(field) + ");");
        if (isNull(field))
          writeln(1, "q_.GetNull(" + field.useName() + "IsNull, " + j + ");");
      }
      writeln(1, "return true;");
      writeln("}");
      writeln();
    }
  }

  static private String check(String value)
  {
    return value;
  }

  static private void generateCommand(Proc proc)
  {
    boolean isReturning = false;
    boolean isBulkSequence = false;
    String fieldName = "";
    String tableName = proc.table.useName();
    String serverName = proc.table.database.server;
    Vector<String> lines = placeHolder.getLines();
    if (proc.isInsert == true && proc.hasReturning == true && proc.outputs.size() == 1)
    {
      Field field = proc.outputs.elementAt(0);
      if (field.isSequence == true)
      {
        fieldName = field.useName();
        isReturning = true;
      }
    }
    if (proc.isMultipleInput == true && proc.isInsert == true)
      isBulkSequence = true;
    int size = 0;
    for (int i = 0; i < lines.size(); i++)
    {
      String l = lines.elementAt(i);
      if (l.charAt(0) == '"')
        size += (l.length() + 2);
      else
      {
        String var = l.trim();
        for (int j = 0; j < proc.dynamics.size(); j++)
        {
          String s = proc.dynamics.elementAt(j);
          if (var.compareTo(s) == 0)
          {
            Integer n = proc.dynamicSizes.elementAt(j);
            size += (n + 2);
          }
        }
      }
    }
    if (placeHolder.limit != null)
    {
      switch (cppRetType)
      {
        case "ORACLE", "DB2" -> size += placeHolder.limit.fetchRowsSize();
        case "MSSQL" -> size += placeHolder.limit.topRowsSize();
        case "MYSQL", "POSTGRE" -> size += placeHolder.limit.limitRowsSize();
      }
    }
    writeln(1, format("size_t size = %d;", size));
    writeln(1, format("TJCppRet::setType(CPP_RET_%s);", cppRetType));
    if (isReturning == true || isBulkSequence == true)
    {
      writeln(1, "TJCppRet _ret;");
      writeln(1, format("size += _ret.setup(\"%s\", \"%s\", \"%s\", \"%s\", %s);", serverName, tableName, proc.name, fieldName, isReturning ? "true" : "false"));
    }
    writeln(1, "if (q_.command != 0) delete [] q_.command;");
    writeln(1, "q_.command = new char [size];");
    writeln(1, "memset(q_.command, 0, size);");
    String strcat = "strcat(q_.command, ";
    String terminate = "";
    if (lines.size() > 0)
    {
      for (int i = 0; i < lines.size(); i++)
      {
        String str = lines.elementAt(i);
        if (cppRetType.equals("MSSQL") && i == 0 && placeHolder.limit != null && str.toLowerCase().contains("select"))
        {
          str = str.replace("\"", "").substring(7);
          String[] code = placeHolder.limit.topRowsLines();
          writeln(1, "strcat(q_.command, \"SELECT \");");
          for (String line : code)
            writeln(line);
          if (str.length() > 0)
            writeln(1, format("strcat(q_.command, \"%s \");", str));
          continue;
        }
        if (str.charAt(0) != '"')
        {
          terminate = ");";
          strcat = "strcat(q_.command, ";
          if (i != 0)
            writeln(terminate);
        }
        else if (i != 0)
          writeln(terminate);
        if (str.charAt(0) != '"')
          write(1, strcat + check(str));
        else
          write(1, strcat + str);
        if (str.charAt(0) == '"')
        {
          terminate = "\"\\n\"";
          strcat = "    ";
        }
      }
      writeln(");");
      if (placeHolder.limit != null)
      {
        String[] code = {};
        switch (cppRetType)
        {
          case "ORACLE", "DB2" -> code = placeHolder.limit.fetchRowsLines();
          case "MYSQL", "POSTGRE" -> code = placeHolder.limit.limitRowsLines();
        }
        for (String line : code)
          writeln(line);
      }
    }
  }

  /**
   * generate Holding variables
   */
  static private void generateCppBind(Field field)
  {
    switch (field.type)
    {
      case Field.DATE:
        writeln(1, "DATE_STRUCT " + field.useName() + "_CLIDate;");
        break;
      case Field.TIME:
        writeln(1, "TIME_STRUCT " + field.useName() + "_CLITime;");
        break;
      case Field.DATETIME:
        writeln(1, "TIMESTAMP_STRUCT " + field.useName() + "_CLIDateTime;");
        break;
      case Field.TIMESTAMP:
        writeln(1, "TIMESTAMP_STRUCT " + field.useName() + "_CLITimeStamp;");
        break;
      case Field.AUTOTIMESTAMP:
        writeln(1, "//TIMESTAMP_STRUCT " + field.useName() + "_CLITimeStamp;");
        break;
      case Field.LONG:
      case Field.BIGSEQUENCE:
      case Field.BIGIDENTITY:
        if (useLongAsChar())
          writeln(1, "char " + field.useName() + "_ODBC_LONG[19];");
        break;
    }
  }

  static private void generateWithParms(Proc proc, String pad)
  {
    String comma = "  ";
    for (int j = 0; j < proc.inputs.size(); j++)
    {
      Field field = proc.inputs.elementAt(j);
      if ((isSequence(field) && proc.isInsert) || isIdentity(field)
          || field.type == Field.TIMESTAMP || field.type == Field.AUTOTIMESTAMP || field.type == Field.USERSTAMP)
        continue;
      writeln(pad + comma + "const " + cppParm(field));
      comma = ", ";
    }
    for (int j = 0; j < proc.dynamics.size(); j++)
    {
      String s = proc.dynamics.elementAt(j);
      writeln(pad + comma + "const char*   a" + s);
      comma = ", ";
    }
  }

  static private void generateInterface(Table table, Proc proc, String dataStruct)
  {
    placeHolder = new PlaceHolder(proc, paramStyle, "");
    String front = "  { ";
    boolean standardExec = true;
    if (proc.outputs.size() > 0)
    {
      writeln(1, "enum");
      Field field = proc.outputs.elementAt(0);
      String thisOne = field.useName().toUpperCase() + "_OFFSET";
      String lastOne = thisOne;
      String lastSize = cppLength(field);
      writeln(front + TJCStructs.padder(thisOne, 24) + "= 0");
      front = "  , ";
      for (int j = 1; j < proc.outputs.size(); j++)
      {
        field = proc.outputs.elementAt(j);
        thisOne = field.useName().toUpperCase() + "_OFFSET";
        writeln(1, ", " + TJCStructs.padder(thisOne, 24) + "= (" + lastOne + "+" + lastSize + ")");
        lastOne = thisOne;
        lastSize = cppLength(field);
      }
      writeln(1, ", " + TJCStructs.padder("ROWSIZE", 24) + "= (" + lastOne + "+" + lastSize + ")");
      if (proc.isSingle)
        writeln(1, ", " + TJCStructs.padder("NOROWS", 24) + "= 1");
      else if (proc.noRows > 0)
        writeln(1, ", " + TJCStructs.padder("NOROWS", 24) + "= " + proc.noRows);
      else
        writeln(1, ", " + TJCStructs.padder("NOROWS", 24) + "= (24*1024 / ROWSIZE) + 1");
      writeln(1, ", " + TJCStructs.padder("NOBINDS", 24) + "= " + placeHolder.pairs.size());
      writeln(1, ", " + TJCStructs.padder("NODEFINES", 24) + "= " + proc.outputs.size());
      field = proc.outputs.elementAt(0);
      thisOne = field.useName().toUpperCase();
      writeln(1, ", " + TJCStructs.padder(thisOne + "_POS", 24) + "= 0");
      for (int j = 1; j < proc.outputs.size(); j++)
      {
        field = proc.outputs.elementAt(j);
        thisOne = field.useName().toUpperCase();
        writeln(1, ", " + TJCStructs.padder(thisOne + "_POS", 24) + "= " + TJCStructs.padder(thisOne + "_OFFSET", 24) + "* NOROWS");
      }
      writeln(1, "};");
    }
    else if (proc.isMultipleInput)
    {
      int noNulls = 0;
      standardExec = false;
      writeln(1, "enum");
      Field field = proc.inputs.elementAt(0);
      if (isNull(field) || (field.type == Field.CHAR && field.isNull == true) || (field.type == Field.ANSICHAR && field.isNull == true))
        noNulls++;
      String thisOne = field.useName().toUpperCase() + "_OFFSET";
      String lastOne = thisOne;
      String thisSize = field.useName().toUpperCase() + "_SIZE";
      String lastSize = thisSize;
      writeln(front + TJCStructs.padder(thisOne, 24) + "= 0");
      front = "  , ";
      writeln(front + TJCStructs.padder(thisSize, 24) + "= " + cppLength(field));
      for (int j = 1; j < proc.inputs.size(); j++)
      {
        field = proc.inputs.elementAt(j);
        if (isNull(field) || (field.type == Field.CHAR && field.isNull == true) || (field.type == Field.ANSICHAR && field.isNull == true))
          noNulls++;
        thisOne = field.useName().toUpperCase() + "_OFFSET";
        thisSize = field.useName().toUpperCase() + "_SIZE";
        writeln(1, ", " + TJCStructs.padder(thisOne, 24) + "= (" + lastOne + "+" + lastSize + ")");
        writeln(1, ", " + TJCStructs.padder(thisSize, 24) + "= " + cppLength(field));
        lastOne = thisOne;
        lastSize = thisSize;
      }
      writeln(1, ", " + TJCStructs.padder("ROWSIZE", 24) + "= (" + lastOne + "+" + lastSize + ")");
      writeln(1, ", " + TJCStructs.padder("NOBINDS", 24) + "= " + placeHolder.pairs.size());
      writeln(1, ", " + TJCStructs.padder("NONULLS", 24) + "= " + noNulls);
      writeln(1, "};");
      writeln(1, "void Exec(int32 noOf, " + dataStruct + "* Recs);");
    }
    writeln(1, "TJQuery q_;");
    if (standardExec == true)
    {
      writeln(1, "void Exec();");
      writeln(1, "void Exec(" + dataStruct + "& Rec) {*DRec() = Rec;Exec();}");
      boolean skipExecWithParms = false;
      for (int j = 0; j < proc.inputs.size(); j++)
      {
        Field field = proc.inputs.elementAt(j);
        if (field.type == Field.BLOB)// || field.type == Field.BIGXML)
        {
          skipExecWithParms = true;
          break;
        }
      }
      if (skipExecWithParms == false)
        if ((proc.inputs.size() > 0) || proc.dynamics.size() > 0)
        {
          writeln(1, "void Exec(");
          generateWithParms(proc, "  ");
          writeln(1, ");");
        }
    }
    if (proc.outputs.size() > 0)
    {
      writeln(1, "bool Fetch();");
      if (proc.isSingle)
      {
        writeln(1, "bool ReadOne() {Exec();return Fetch();}");
        writeln(1, "bool ReadOne(" + dataStruct + "& Rec) {*DRec() = Rec;Exec();return Fetch();}");
      }
    }
    writeln(1, "T" + table.useName() + proc.upperFirst() + "(TJConnector &conn, char *aFile=__FILE__, long aLine=__LINE__)");
    writeln(1, ": q_(conn)");
    writeln(1, "{Clear();q_.FileAndLine(aFile,aLine);}");
    writeln(1, "" + dataStruct + "* DRec() {return this;}");
    if (proc.outputs.size() > 0)
      writeln(1, "O" + dataStruct.substring(1) + "* ORec() {return this;}");
    if (proc.isStdExtended() == false && proc.extendsStd == true)
    {
      writeln(1, "D" + table.useName() + "* DStd() {return (D" + table.useName() + "*)this;}");
      if (proc.outputs.size() > 0)
        writeln(1, "O" + table.useName() + "* OStd() {return (O" + table.useName() + "*)this;}");
    }
  }

  static private String fileName(String output, String node, String ext)
  {
    return output + node + ext;
  }

  static private String charFieldFlag(Field field)
  {
    if (field.type != Field.CHAR && field.type != Field.ANSICHAR && field.type != Field.TLOB && field.type != Field.XML)
      return "";
    if ((field.type == Field.CHAR || field.type == Field.TLOB || field.type == Field.XML) && field.isNull == true)
      return ", 0, 1";
    if (field.type == Field.ANSICHAR)
      if (field.isNull == true)
        return ", 1, 1";
      else
        return ", 1, 0";
    return ", 0, 0";
  }

  static private boolean isNull(Field field)
  {
    if (field.isNull == false)
      return false;
    return switch (field.type)
    {
      case Field.BOOLEAN, Field.FLOAT, Field.DOUBLE, Field.MONEY, Field.BYTE, Field.SHORT, Field.INT, Field.IDENTITY, Field.SEQUENCE, Field.BLOB, Field.DATE, Field.DATETIME, Field.TIMESTAMP, Field.AUTOTIMESTAMP, Field.TIME -> true;
        default -> false;
    };
  }

  static private String cppLength(Field field)
  {
    return switch (field.type)
    {
      case Field.LONG, Field.BIGSEQUENCE, Field.BIGIDENTITY ->
      {
        if (useLongAsChar())
          yield "19";
        else
          yield "sizeof(SQLLEN)";
      }
      case Field.FLOAT, Field.DOUBLE ->
      {
        if (field.precision > 15)
          yield "" + (field.precision + 3);
        else
          yield "sizeof(double)";
      }
      case Field.BOOLEAN, Field.BYTE, Field.SHORT -> "sizeof(int16)";
      case Field.INT, Field.SEQUENCE, Field.IDENTITY -> "sizeof(int32)";
      case Field.CHAR, Field.ANSICHAR, Field.XML -> format("%d", field.length + 1);
      case Field.UTF8 ->  format("%d", field.length * 3 + 1);
      case Field.UNICODE -> format("%d", field.length * 2 + 4);
      case Field.USERSTAMP -> "64";
      case Field.BLOB, Field.TLOB, Field.IMAGE -> "sizeof(TJBlob<" + field.length + ">)";
      case Field.DATE, Field.TIME, Field.DATETIME, Field.TIMESTAMP -> "8";
      case Field.MONEY -> "21";
        default -> "0";
    };
  }

  static private String cppDirection(Field field)
  {
    if (field.isIn && field.isOut)
      return "SQL_PARAM_INPUT_OUTPUT";
    if (field.isOut)
      return "SQL_PARAM_OUTPUT";
    return "SQL_PARAM_INPUT";
  }

  static private String cppArrayPointer(Field field)
  {
    String offset = field.useName().toUpperCase() + "_OFFSET";
    return switch (field.type)
    {
      case Field.BOOLEAN, Field.BYTE, Field.SHORT ->
          "int16 *" + field.useName() + " = (int16 *)(q_.data + " + offset + " * noOf);";
      case Field.INT, Field.SEQUENCE ->
          "int32 *" + field.useName() + " = (int32 *)(q_.data + " + offset + " * noOf);";
      case Field.LONG, Field.BIGSEQUENCE, Field.BIGIDENTITY ->
          "SQLLEN *" + field.useName() + " = (SQLLEN *)(q_.data + " + offset + " * noOf);";
      case Field.FLOAT, Field.DOUBLE ->
      {
        if (field.precision > 15)
          yield "char *" + field.useName() + " = (char *)(q_.data + " + offset + " * noOf);";
        yield "double *" + field.useName() + " = (double *)(q_.data + " + offset + " * noOf);";
      }
      case Field.MONEY, Field.TLOB, Field.XML, Field.CHAR, Field.ANSICHAR, Field.USERSTAMP ->
          "char *" + field.useName() + " = (char *)(q_.data + " + offset + " * noOf);";
      case Field.DATE ->
          "DATE_STRUCT* " + field.useName() + " = (DATE_STRUCT *)(q_.data + " + offset + " * noOf);";
      case Field.TIME ->
          "TIME_STRUCT* " + field.useName() + " = (TIME_STRUCT *)(q_.data + " + offset + " * noOf);";
      case Field.DATETIME, Field.TIMESTAMP, Field.AUTOTIMESTAMP ->
          "TIMESTAMP_STRUCT* " + field.useName() + " = (TIMESTAMP_STRUCT *)(q_.data + " + offset + " * noOf);";
      case Field.BLOB, Field.IMAGE, Field.UNICODE ->
          "// Blobs Image or UNICODE are not handled here";
        default -> "// not handled here";
    };
  }

  /**
   * Translates field type to cpp data member type
   */
  static private String cppBind(Field field)
  {
    return switch (field.type)
    {
      case Field.LONG, Field.BIGSEQUENCE ->
      {
        if (useLongAsChar())
          yield "q_.AsChar(" + field.useName() + "_ODBC_LONG, " + field.useName() + "), 18";
        else
          yield field.useName();
      }
      case Field.BOOLEAN, Field.BYTE, Field.SHORT, Field.INT, Field.SEQUENCE -> field.useName();
      case Field.FLOAT, Field.DOUBLE -> field.useName() + ", " + (field.precision) + ", " + (field.scale);
      case Field.MONEY -> field.useName() + ", 18, 2";
      case Field.XML, Field.CHAR -> field.useName() + ", " + (field.length);
      case Field.ANSICHAR -> field.useName() + ", " + (field.length + 1);
      case Field.BLOB, Field.TLOB, Field.IMAGE -> "(char*)&" + field.useName() + ", sizeof(" + field.useName() + ".data)";
      case Field.USERSTAMP -> "q_.UserStamp(" + field.useName() + "), 64";
      case Field.DATE -> "q_.Date(" + field.useName() + "_OCIDate, " + field.useName() + ")";
      case Field.TIME -> "q_.Time(" + field.useName() + "_OCIDate, " + field.useName() + ")";
      case Field.DATETIME -> "q_.DateTime(" + field.useName() + "_OCIDate, " + field.useName() + ")";
      case Field.TIMESTAMP -> "q_.TimeStamp(" + field.useName() + "_OCIDate, " + field.useName() + ")";
        default -> field.useName() + ", <unsupported bind1>";
    };
  }

  static private String cppBind(Field field, String tableName, boolean isInsert)
  {
    return switch (field.type)
    {
      case Field.BOOLEAN, Field.BYTE, Field.SHORT, Field.INT ->
          field.useName();
      case Field.SEQUENCE ->
      {
        if (isInsert)
          yield "q_.Sequence(" + field.useName() + ", \"" + tableName + "Seq\")";
        else
          yield field.useName();
      }
      case Field.FLOAT, Field.DOUBLE ->
          field.useName() + ", " + (field.precision) + ", " + (field.scale);
      case Field.MONEY ->
          field.useName() + ", 18, 2";
      case Field.BIGSEQUENCE ->
      {
        if (useLongAsChar())
        {
          if (isInsert)
            yield format("q_.AsChar(%s_ODBC_LONG, q_.Sequence(%s, \"%sSeq\")), 18", field.useName(), field.useName(), tableName);
          else
            yield "q_.AsChar(" + field.useName() + "_ODBC_LONG, " + field.useName() + "), 18";
        }
        else
        {

          if (isInsert)
            yield format("q_.Sequence(%s, \"%sSeq\")", field.useName(), tableName);
          else
            yield field.useName();
        }
      }
      case Field.LONG ->
      {
        if (useLongAsChar())
          yield "q_.AsChar(" + field.useName() + "_ODBC_LONG, " + field.useName() + "), 18";
        else
          yield field.useName();
      }
      case Field.XML, Field.CHAR, Field.ANSICHAR ->
          field.useName() + ", " + (field.length);
      case Field.UTF8 ->
              format("%s, %d", field.useName(), field.length * 3 + 1);
      case Field.UNICODE ->
              format("%s, %d", field.useName(), field.length * 2 + 4);
      case Field.USERSTAMP ->
          "q_.UserStamp(" + field.useName() + "), 8";
      case Field.DATE ->
          "q_.Date(" + field.useName() + "_CLIDate, " + field.useName() + ")";
      case Field.TIME ->
          "q_.Time(" + field.useName() + "_CLITime, " + field.useName() + ")";
      case Field.DATETIME ->
          "q_.DateTime(" + field.useName() + "_CLIDateTime, " + field.useName() + ")";
      case Field.TIMESTAMP, Field.AUTOTIMESTAMP ->
          "q_.TimeStamp(" + field.useName() + "_CLITimeStamp, " + field.useName() + ")";
      case Field.TLOB, Field.BLOB ->
          "(char*)&" + field.useName() + ", sizeof(" + field.useName() + ".data)";
        default ->
        field.useName() + ", <unsupported bind2>";
    };
  }

  /**
   * Translates field type to cpp data member type
   */
  static private String cppDefine(Field field)
  {
    return switch (field.type)
    {
      case Field.BOOLEAN, Field.BYTE, Field.SHORT ->
          "(int16*) (q_.data+" + field.useName().toUpperCase() + "_POS)";
      case Field.INT, Field.IDENTITY, Field.SEQUENCE ->
          "(int32*) (q_.data+" + field.useName().toUpperCase() + "_POS)";
      case Field.LONG, Field.BIGIDENTITY, Field.BIGSEQUENCE ->
          "(SQLLEN*) (q_.data+" + field.useName().toUpperCase() + "_POS)";
      case Field.CHAR, Field.TLOB, Field.XML ->
          "(char*)  (q_.data+" + field.useName().toUpperCase() + "_POS), " + (field.length + 1);
      case Field.UTF8 ->
          format("(unsigned char*) q_.data + %s_POS, %d", field.useName().toUpperCase(), field.length * 3 + 1);
      case Field.UNICODE ->
          format("(unsigned char*) q_.data + %s_POS, %d", field.useName().toUpperCase(), field.length * 2 + 4);
      case Field.ANSICHAR ->
          "(char*)  (q_.data+" + field.useName().toUpperCase() + "_POS), " + (field.length + 1) + ", 1";
      case Field.USERSTAMP ->
          "(char*)  (q_.data+" + field.useName().toUpperCase() + "_POS), 9";
      case Field.BLOB ->
          "(char*)  (q_.data+" + field.useName().toUpperCase() + "_POS), " + (field.length);
      case Field.DATE ->
          "(DATE_STRUCT*)(q_.data+" + field.useName().toUpperCase() + "_POS)";
      case Field.TIME ->
          "(TIME_STRUCT*)(q_.data+" + field.useName().toUpperCase() + "_POS)";
      case Field.DATETIME, Field.TIMESTAMP, Field.AUTOTIMESTAMP ->
          "(TIMESTAMP_STRUCT*)(q_.data+" + field.useName().toUpperCase() + "_POS)";
      case Field.FLOAT, Field.DOUBLE ->
      {
        if (field.precision > 15)
          yield "(char*)  (q_.data+" + field.useName().toUpperCase() + "_POS), " + (field.precision + 3);
        yield "(double*)(q_.data+" + field.useName().toUpperCase() + "_POS)";
      }
      case Field.MONEY ->
          "(char*)  (q_.data+" + field.useName().toUpperCase() + "_POS), 21";
        default ->
        field.useName() + " <unsupported define>";
    };
  }

  /**
   * Translates field type to cpp data member type
   */
  static private String cppGet(Field field)
  {
    return switch (field.type)
    {
      case Field.BOOLEAN, Field.BYTE, Field.SHORT, Field.INT, Field.SEQUENCE, Field.IDENTITY
         , Field.BIGSEQUENCE, Field.BIGIDENTITY, Field.LONG ->
         field.useName() + "," + " q_.data+" + field.useName().toUpperCase() + "_POS";
      case Field.FLOAT, Field.DOUBLE ->
      {
        if (field.precision > 15)
          yield field.useName() + "," + " q_.data+" + field.useName().toUpperCase() + "_POS, " + (field.precision + 3);
        yield field.useName() + "," + " q_.data+" + field.useName().toUpperCase() + "_POS";
      }
      case Field.MONEY ->
         field.useName() + "," + " q_.data+" + field.useName().toUpperCase() + "_POS, 21";
      case Field.CHAR, Field.ANSICHAR, Field.TLOB, Field.XML ->
         field.useName() + "," + " q_.data+" + field.useName().toUpperCase() + "_POS, " + (field.length + 1);
      case Field.UTF8 -> field.useName() + "," + " (unsigned char *) q_.data+" + field.useName().toUpperCase() + "_POS, " + (field.length * 3 + 1);
      case Field.UNICODE -> field.useName() + "," + " (unsigned char *) q_.data+" + field.useName().toUpperCase() + "_POS, " + (field.length * 2 + 4);
      case Field.USERSTAMP ->
         field.useName() + "," + " q_.data+" + field.useName().toUpperCase() + "_POS, 9";
      case Field.BLOB ->
         field.useName() + ".len, " + field.useName() + ".data," +
               " q_.data+" + field.useName().toUpperCase() + "_POS, sizeof(" + field.useName() + ")";
      case Field.DATE ->
         "TJDate(" + field.useName() + ")," + " q_.data+" + field.useName().toUpperCase() + "_POS";
      case Field.TIME ->
         "TJTime(" + field.useName() + ")," + " q_.data+" + field.useName().toUpperCase() + "_POS";
      case Field.DATETIME, Field.TIMESTAMP, Field.AUTOTIMESTAMP ->
         "TJDateTime(" + field.useName() + ")," + " q_.data+" + field.useName().toUpperCase() + "_POS";
      default -> field.useName() + " <unsupported get>";
    };
  }

  static private String cppCopy(Field field)
  {
    return switch (field.type)
    {
      case Field.BOOLEAN, Field.BYTE, Field.SHORT, Field.INT, Field.LONG, Field.SEQUENCE
         , Field.BIGSEQUENCE, Field.BLOB ->
        field.useName() + " = a" + field.useName() + ";";
      case Field.FLOAT, Field.DOUBLE ->
      {
        if (field.precision > 15)
          yield "strncpy(" + field.useName() + ", a" + field.useName() + ", sizeof(" + field.useName() + ")-1);";
        yield field.useName() + " = a" + field.useName() + ";";
      }
      case Field.MONEY, Field.UTF8, Field.UNICODE, Field.CHAR, Field.TLOB, Field.XML
         , Field.DATE, Field.TIME, Field.DATETIME ->
        "memcpy(" + field.useName() + ", a" + field.useName() + ", sizeof(" + field.useName() + ")-1);";
      case Field.ANSICHAR ->
        "memcpy(" + field.useName() + ", a" + field.useName() + ", sizeof(" + field.useName() + "));";
      case Field.USERSTAMP, Field.IDENTITY, Field.TIMESTAMP, Field.AUTOTIMESTAMP ->
        "// " + field.useName() + " -- generated";
      default -> field.useName() + " <unsupported copy>";
    };
  }

  static private String cppArrayCopy(Field field)
  {
    String size = field.useName().toUpperCase() + "_SIZE";
    return switch (field.type)
    {
      case Field.BOOLEAN, Field.BYTE, Field.SHORT, Field.INT, Field.LONG, Field.SEQUENCE, Field.BIGSEQUENCE, Field.BLOB ->
        field.useName() + "[i] = Recs[i]." + field.useName() + ";";
      case Field.FLOAT, Field.DOUBLE ->
      {
        if (field.precision > 15)
          yield "strncpy(&" + field.useName() + "[i*" + size + "], Recs[i]." + field.useName() + ", " + size + "-1);";
        yield field.useName() + "[i] = Recs[i]." + field.useName() + ";";
      }
      case Field.MONEY, Field.CHAR, Field.TLOB, Field.XML ->
        "strncpy(&" + field.useName() + "[i*" + size + "], Recs[i]." + field.useName() + ", " + size + "-1);";
      case Field.DATE ->
        "q_.Date(" + field.useName() + "[i], Recs[i]." + field.useName() + ");";
      case Field.TIME ->
        "q_.Time(" + field.useName() + "[i], Recs[i]." + field.useName() + ");";
      case Field.DATETIME ->
        "q_.DateTime(" + field.useName() + "[i], Recs[i]." + field.useName() + ");";
      case Field.ANSICHAR ->
        "memcpy(&" + field.useName() + "[i*" + size + "], a" + field.useName() + ", " + size + ");";
      case Field.USERSTAMP, Field.IDENTITY ->
        field.useName() + " -- generated";
      case Field.TIMESTAMP ->
        "q_.TimeStamp(" + field.useName() + "[i], Recs[i]." + field.useName() + ");";
      case Field.AUTOTIMESTAMP ->
        "// " + field.useName() + " -- generated";
      default -> field.useName() + " <unsupported array copy>";
    };
  }

  /**
   * Translates field type to cpp data member type
   */
  static private String cppParm(Field field)
  {
    return switch (field.type)
    {
      case Field.BOOLEAN, Field.BYTE, Field.SHORT ->
        "int16  a" + field.useName();
      case Field.INT, Field.SEQUENCE, Field.IDENTITY ->
        "int32   a" + field.useName();
      case Field.LONG, Field.BIGSEQUENCE, Field.BIGIDENTITY ->
        "SQLLEN  a" + field.useName();
      case Field.UTF8 -> "const unsigned char*  a" + field.useName();
      case Field.UNICODE -> "const unsigned char*  a" + field.useName();
      case Field.CHAR, Field.TLOB, Field.XML, Field.ANSICHAR, Field.USERSTAMP, Field.DATE, Field.TIME, Field.DATETIME, Field.TIMESTAMP, Field.AUTOTIMESTAMP, Field.MONEY ->
        "char*  a" + field.useName();
      case Field.FLOAT, Field.DOUBLE ->
      {
        if (field.precision > 15)
          yield "char*  a" + field.useName();
        yield "double a" + field.useName();
      }
      default -> field.useName() + " <unsupported parm>";
    };
  }
}
