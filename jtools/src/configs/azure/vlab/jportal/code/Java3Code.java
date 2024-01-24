/// ------------------------------------------------------------------
/// Copyright (c) 1996, 2007 Vincent Risi in Association 
///                          with Barone Budge and Dominick 
/// All rights reserved. 
/// This program and the accompanying materials are made available 
/// under the terms of the Common Public License v1.0 
/// which accompanies this distribution and is available at 
/// http://www.eclipse.org/legal/cpl-v10.html 
/// Contributors:
///    Vincent Risi
/// ------------------------------------------------------------------
/// System : JPortal
/// ------------------------------------------------------------------
package configs.azure.vlab.jportal.code;

import java.io.FileOutputStream;
import java.io.PrintWriter;
import java.util.Vector;

import static azure.vlab.jportal.Writer.*;

import azure.vlab.jportal.*;
import vlab.jportal.*;

public class Java3Code extends Generator
{
  /**
   * Generates the procedure classes for each table present.
   */
  public static String description()
  {
    return "generate Java3 code";
  }

  public static String documentation()
  {
    return "generate Java3 code";
  }

  static private byte paramStyle = PlaceHolder.QUESTION;

  public static void generate(Database database, String output, PrintWriter outLog)
  {
    for (int i = 0; i < database.tables.size(); i++)
    {
      Table table = database.tables.elementAt(i);
      generateStructs(table, output, outLog);
      generate(table, output, outLog);
    }
  }

  static void generateStructs(Table table, String output, PrintWriter outLog)
  {
    generateStdProcStruct(table, output, outLog);
    generateOtherProcStructs(table, output, outLog);
  }

  static private String fileName(String output, String node, String ext)
  {
    int p = output.indexOf('\\');
    return output + node + ext;
  }

  static void generateStdProcStruct(Table table, String output, PrintWriter outLog)
  {
    try (PrintWriter outData = new PrintWriter(new FileOutputStream(fileName(output, table.useName(), "Struct.java"))))
    {
      writer = outData;
      indent_size = 2;
      if (table.database.packageName.length() > 0)
      {
        writeln("package " + table.database.packageName + ";");
        writeln();
      }
      writeln("import java.io.Serializable;");
      writeln("import java.sql.*;");
      writeln();
      writeln("/**");
      for (int i = 0; i < table.comments.size(); i++)
      {
        String s = table.comments.elementAt(i);
        writeln(" *" + s);
      }
      writeln(" * This code was generated, do not modify it, modify it at source and regenerate it.");
      writeln(" */");
      writeln("public class " + table.useName() + "Struct implements Serializable");
      writeln("{");
      for (int i = 0; i < table.fields.size(); i++)
      {
        Field field = table.fields.elementAt(i);
        if (field.comments.size() > 0)
        {
          writeln(1, "/**");
          for (int c = 0; c < field.comments.size(); c++)
          {
            String s = field.comments.elementAt(c);
            writeln(1, " *" + s);
          }
          writeln(1, " */");
        }
        writeln(1, "public " + javaVar(field) + ";");
      }
      writeln(1, "public " + table.useName() + "Struct()");
      writeln(1, "{");
      int maxSize = 0;
      for (int i = 0; i < table.fields.size(); i++)
      {
        Field field = table.fields.elementAt(i);
        if (field.useName().length() > maxSize)
          maxSize = field.useName().length();
        writeln(2, "" + initJavaVar(field));
      }
      writeln(1, "}");
      writeln(1, "public String toString()");
      writeln(1, "{");
      writeln(2, "String CRLF = (String) System.getProperty(\"line.separator\");");
      for (int i = 0; i < table.fields.size(); i++)
      {
        if (i == 0)
          write("    return ");
        else
          write("         + ");
        Field field = table.fields.elementAt(i);
        int no = maxSize - field.useName().length();
        writeln("\"  " + field.useName() + padded(no + 1) + ": \" + " + field.useName() + " + CRLF");
      }
      writeln(2, ";");
      writeln(1, "}");
      writeln("}");
      outData.flush();
    }


    catch (Exception ex)
    {
      outLog.println(ex);
      ex.printStackTrace(outLog);
    }
  }

  static void generateOtherProcStructs(Table table, String output, PrintWriter outLog)
  {
    for (int i = 0; i < table.procs.size(); i++)
    {
      Proc proc = table.procs.elementAt(i);
      if (proc.isData)
        continue;
      if (!proc.isStd && !proc.hasNoData())
        generateOtherProcStruct(table, proc, output, outLog);
    }
  }

  static void generateOtherProcStruct(Table table, Proc proc, String output, PrintWriter outLog)
  {
    try (PrintWriter outData = new PrintWriter(new FileOutputStream(fileName(output, table.useName() + proc.upperFirst(), "Struct.java"))))
    {
      writer = outData;
      indent_size = 2;
      //PrintWriter outData = new PrintWriter(outFile);
      if (table.database.packageName.length() > 0)
      {
        writeln("package " + table.database.packageName + ";");
        writeln();
      }
      writeln("import java.io.Serializable;");
      writeln("import java.sql.*;");
      writeln();
      writeln("/**");
      for (int j = 0; j < proc.comments.size(); j++)
      {
        String comment = proc.comments.elementAt(j);
        writeln(" *" + comment);
      }
      writeln(" */");
      writeln("public class " + table.useName() + proc.upperFirst() + "Struct implements Serializable");
      writeln("{");
      int maxSize = 0;
      for (int j = 0; j < proc.inputs.size(); j++)
      {
        Field field = proc.inputs.elementAt(j);
        if (field.useName().length() > maxSize)
          maxSize = field.useName().length();
        writeln(1, "/**");
        for (int c = 0; c < field.comments.size(); c++)
        {
          String s = field.comments.elementAt(c);
          writeln(1, " *" + s);
        }
        if (!proc.hasOutput(field.name))
          writeln(1, " * (input)");
        else
          writeln(1, " * (input/output)");
        writeln(1, " */");
        writeln(1, "public " + javaVar(field) + ";");
      }
      for (int j = 0; j < proc.outputs.size(); j++)
      {
        Field field = proc.outputs.elementAt(j);
        if (field.useName().length() > maxSize)
          maxSize = field.useName().length();
        if (!proc.hasInput(field.name))
        {
          writeln(1, "/**");
          for (int c = 0; c < field.comments.size(); c++)
          {
            String s = field.comments.elementAt(c);
            writeln(1, " *" + s);
          }
          writeln(1, " * (output)");
          writeln(1, " */");
          writeln(1, "public " + javaVar(field) + ";");
        }
      }
      for (int j = 0; j < proc.dynamics.size(); j++)
      {
        String s = proc.dynamics.elementAt(j);
        if (s.length() > maxSize)
          maxSize = s.length();
        writeln(1, "/**");
        writeln(1, " * (dynamic)");
        writeln(1, " */");
        writeln(1, "public String " + s + ";");
      }
      writeln(1, "public " + table.useName() + proc.upperFirst() + "Struct()");
      writeln(1, "{");
      for (int j = 0; j < proc.inputs.size(); j++)
      {
        Field field = proc.inputs.elementAt(j);
        writeln(2, "" + initJavaVar(field));
      }
      for (int j = 0; j < proc.outputs.size(); j++)
      {
        Field field = proc.outputs.elementAt(j);
        if (!proc.hasInput(field.name))
          writeln(2, "" + initJavaVar(field));
      }
      for (int j = 0; j < proc.dynamics.size(); j++)
      {
        String s = proc.dynamics.elementAt(j);
        writeln(2, "" + s + " = \"\";");
      }
      writeln(1, "}");
      writeln(1, "public String toString()");
      writeln(1, "{");
      writeln(2, "String CRLF = (String) System.getProperty(\"line.separator\");");
      String ret = "    return ";
      for (int j = 0; j < proc.inputs.size(); j++)
      {
        write(ret);
        ret = "         + ";
        Field field = proc.inputs.elementAt(j);
        int no = maxSize - field.useName().length();
        writeln("\"  " + field.useName() + padded(no + 1) + ": \" + " + field.useName() + " + CRLF");
      }
      for (int j = 0; j < proc.outputs.size(); j++)
      {
        Field field = proc.outputs.elementAt(j);
        if (!proc.hasInput(field.name))
        {
          write(ret);
          ret = "         + ";
          int no = maxSize - field.useName().length();
          writeln("\"  " + field.useName() + padded(no + 1) + ": \" + " + field.useName() + " + CRLF");
        }
      }
      for (int j = 0; j < proc.dynamics.size(); j++)
      {
        String s = proc.dynamics.elementAt(j);
        write(ret);
        ret = "         + ";
        int no = maxSize - s.length();
        writeln("\"  " + s + padded(no + 1) + ": \" + " + s + " + CRLF");
      }
      writeln(2, ";");
      writeln(1, "}");
      writeln("}");
      outData.flush();
    }


    catch (Exception ex)
    {
      outLog.println(ex);
      ex.printStackTrace(outLog);
    }
  }

  /**
   * Build of standard and user defined procedures
   */
  static void generate(Table table, String output, PrintWriter outLog)
  {
    generateStdProcs(table, output, outLog);
    generateOtherProcs(table, output, outLog);
  }

  /**
   * Build of all required standard procedures
   */
  static private String extendsName;

  static void generateStdProcs(Table table, String output, PrintWriter outLog)
  {
    try (PrintWriter outData = new PrintWriter(new FileOutputStream(fileName(output, table.useName(), ".java"))))
    {
      writer = outData;
      indent_size = 2;
      if (table.database.packageName.length() > 0)
      {
        writeln("package " + table.database.packageName + ";");
        writeln("");
      }
      writeln("import bbd.jportal.*;");
      writeln("import java.sql.*;");
      writeln("import java.util.*;");
      writeln("");
      writeln("/**");
      for (int i = 0; i < table.comments.size(); i++)
      {
        String s = table.comments.elementAt(i);
        writeln(" *" + s);
      }
      writeln(" * This code was generated, do not modify it, modify it at source and regenerate it.");
      writeln(" */");
      extendsName = table.useName() + "Struct";
      writeln("public class " + table.useName() + " extends " + extendsName);
      writeln("{");
      writeln(1, "Connector connector;");
      writeln(1, "Connection connection;");
      writeln(1, "/**");
      writeln(1, " * @param Connector for specific database");
      writeln(1, " */");
      writeln(1, "public " + table.useName() + "(Connector connector)");
      writeln(1, "{");
      writeln(2, "super();");
      writeln(2, "this.connector = connector;");
      writeln(2, "connection = connector.connection;");
      writeln(1, "}");
      for (int i = 0; i < table.procs.size(); i++)
      {
        Proc proc = table.procs.elementAt(i);
        if (proc.isData)
          continue;
        if (proc.isStd)
          emitProc(proc);
        else if (proc.hasNoData())
          emitStaticProc(proc);
      }
      writeln("}");
      outData.flush();
    }
    catch (Exception ex)
    {
      outLog.println(ex);
      ex.printStackTrace(outLog);
    }
  }

  /**
   * Build of user defined procedures
   */
  static void generateOtherProcs(Table table, String output, PrintWriter outLog)
  {
    for (int i = 0; i < table.procs.size(); i++)
    {
      Proc proc = table.procs.elementAt(i);
      if (proc.isData)
        continue;
      if (!proc.isStd && !proc.hasNoData())
        generateOtherProc(table, proc, output, outLog);
    }
  }

  static void generateOtherProc(Table table, Proc proc, String output, PrintWriter outLog)
  {
    try (PrintWriter outData = new PrintWriter(new FileOutputStream(fileName(output, table.useName() + proc.upperFirst(), ".java"))))
    {
      writer = outData;
      indent_size = 2;
      if (table.database.packageName.length() > 0)
      {
        writeln("package " + table.database.packageName + ";");
        writeln("");
      }
      writeln("import bbd.jportal.*;");
      writeln("import java.sql.*;");
      writeln("import java.util.*;");
      writeln("");
      writeln("/**");
      for (int j = 0; j < proc.comments.size(); j++)
      {
        String comment = proc.comments.elementAt(j);
        writeln(" *" + comment);
      }
      writeln(" */");
      extendsName = table.useName() + proc.upperFirst() + "Struct";
      writeln("public class " + table.useName() + proc.upperFirst() + " extends " + extendsName);
      writeln("{");
      writeln(1, "Connector connector;");
      writeln(1, "Connection connection;");
      writeln(1, "public " + table.useName() + proc.upperFirst() + "(Connector connector)");
      writeln(1, "{");
      writeln(2, "super();");
      writeln(2, "this.connector = connector;");
      writeln(2, "connection = connector.connection;");
      writeln(1, "}");
      emitProc(proc);
      writeln("}");
      outData.flush();
    }
    catch (Exception ex)
    {
      outLog.println(ex);
      ex.printStackTrace(outLog);
    }
  }

  /**
   *
   */
  static PlaceHolder placeHolders;

  /**
   * Emits a static or class method
   */
  static void emitStaticProc(Proc proc)
  {
    writeln(1, "/**");
    writeln(1, " * class method as it has no input or output.");
    writeln(1, " * @exception SQLException is passed through");
    writeln(1, " */");
    writeln(1, "public static void " + proc.lowerFirst() + "(Connector connector) throws SQLException");
    writeln(1, "{");
    placeHolders = new PlaceHolder(proc, PlaceHolder.QUESTION, "");
    Vector lines = placeHolders.getLines();
    generateCommand(lines);
    writeln(2, "PreparedStatement prep = connector.connection.prepareStatement(statement);");
    writeln(2, "prep.executeUpdate();");
    writeln(2, "prep.close();");
    writeln(1, "}");
  }

  private static void generateCommand(Vector lines)
  {
    String trip = "\"\"\"";
    var buf = new StringBuffer();
    boolean useBuf = false;
    String comma = "";
    for (int i = 0; i < lines.size(); i++)
    {
      String string = (String) lines.elementAt(i);
      if (string.charAt(0) != '"')
      {
        useBuf = true;
        buf.append(format(", %s", string.trim()));
      }
    }
    if (useBuf)
      writeln(2, format("String statement = String.format(%s", trip));
    else
      writeln(2, format("String statement = %s", trip));
    String plus = "    ";
    for (int i = 0; i < lines.size(); i++)
    {
      //writeln(plus+ lines.elementAt(i).replace());
      String string = (String) lines.elementAt(i);
      if (string.charAt(0) == '"')
        writeln(string.replaceAll("\"", ""));
      else
        writeln("%s");
      //plus = "    +";
    }
    if (useBuf)
      writeln(format("%s%s);", trip, buf.toString()));
    else
      writeln(format("%s;", trip));
  }

  /**
   * Emits class method for processing the database activity
   */
  static void emitProc(Proc proc)
  {              //  12345
    writeln(1, "/**");
    if (proc.comments.size() > 0)
    {
      for (int i = 0; i < proc.comments.size(); i++)
      {
        String comment = proc.comments.elementAt(i);
        writeln(2, "*" + comment);
      }
    }
    if (proc.outputs.size() == 0)
      writeln(1, " * Returns no output.");
    else if (proc.isSingle)
    {
      writeln(1, " * Returns at most one record.");
      writeln(1, " * @return true if a record is found");
    } else
    {
      writeln(1, " * Returns any number of records.");
      writeln(1, " * @return result set of records found");
    }
    writeln(1, " * @exception SQLException is passed through");
    writeln(1, " */");
    String procName = proc.lowerFirst();
    if (proc.outputs.size() == 0)
      writeln(1, "public void " + procName + "() throws SQLException");
    else if (proc.isSingle)
      writeln(1, "public boolean " + procName + "() throws SQLException");
    else
      writeln(1, "public Query " + procName + "() throws SQLException");
    writeln(1, "{");
    placeHolders = new PlaceHolder(proc, PlaceHolder.QUESTION, "");
    Vector lines = placeHolders.getLines();
    generateCommand(lines);
    writeln(2, "PreparedStatement prep = connection.prepareStatement(statement);");
    for (int i = 0; i < proc.inputs.size(); i++)
    {
      Field field = proc.inputs.elementAt(i);
      if (proc.isInsert)
      {
        if (field.isSequence)
          writeln(2, "" + field.useName() + " = connector.getSequence(\"" + proc.table.name + "\");");
      }
      if (field.type == Field.TIMESTAMP)
        writeln(2, "" + field.useName() + " = connector.getTimestamp();");
      if (field.type == Field.USERSTAMP)
        writeln(2, "" + field.useName() + " = connector.getUserstamp();");
    }
    Vector pairs = placeHolders.getPairs();
    for (int i = 0; i < pairs.size(); i++)
    {
      PlaceHolderPairs pair = (PlaceHolderPairs) pairs.elementAt(i);
      Field field = pair.field;
      write("    prep.set");
      write(setType(field));
      write("(");
      write(format("%d", i + 1));
      writeln(", " + field.useName() + ");");
    }
    if (proc.outputs.size() > 0)
    {
      if (proc.noRows > 0)
        writeln(2, "prep.setFetchSize(" + proc.noRows + ");");
      writeln(2, "ResultSet result = prep.executeQuery();");
      if (!proc.isSingle)
      {
        writeln(2, "Query query = new Query(prep, result);");
        writeln(2, "return query;");
        writeln(1, "}");
        writeln(1, "/**");
        writeln(1, " * Returns the next record in a result set.");
        writeln(1, " * @param result The result set for the query.");
        writeln(1, " * @return true while records are found.");
        writeln(1, " * @exception SQLException is passed through");
        writeln(1, " */");
        writeln(1, "public boolean " + procName + "(Query query) throws SQLException");
        writeln(1, "{");
        writeln(2, "if (!query.result.next())");
        writeln(2, "{");
        writeln(3, "query.close();");
        writeln(3, "return false;");
        writeln(2, "}");
        writeln(2, "ResultSet result = query.result;");
      } else
      {
        writeln(2, "if (!result.next())");
        writeln(2, "{");
        writeln(3, "result.close();");
        writeln(3, "prep.close();");
        writeln(3, "return false;");
        writeln(2, "}");
      }
      for (int i = 0; i < proc.outputs.size(); i++)
      {
        Field field = proc.outputs.elementAt(i);
        write("    " + field.useName() + " =  result.get");
        write(setType(field));
        write("(");
        write(format("%d", i + 1));
        writeln(");");
      }
      if (proc.isSingle)
      {
        writeln(2, "result.close();");
        writeln(2, "prep.close();");
      }
      writeln(2, "return true;");
    } else
    {
      writeln(2, "prep.executeUpdate();");
      writeln(2, "prep.close();");
    }
    writeln(1, "}");

    if (proc.outputs.size() > 0 && !proc.isSingle)
    {
      writeln(1, "/**");
      writeln(1, " * Returns all the records in a result set as array of " + extendsName + ".");
      writeln(1, " * @return array of " + extendsName + ".");
      writeln(1, " * @exception SQLException is passed through");
      writeln(1, " */");
      writeln(1, "public " + extendsName + "[] " + procName + "Load() throws SQLException");
      writeln(1, "{");
      writeln(2, "Vector recs = new Vector();");
      writeln(2, "Query query = " + procName + "();");
      writeln(2, "while (" + procName + "(query) == true)");
      writeln(2, "{");
      writeln(3, "" + extendsName + " rec = new " + extendsName + "();");
      for (int i = 0; i < proc.outputs.size(); i++)
      {
        Field field = proc.outputs.elementAt(i);
        writeln(3, "rec." + field.useName() + " = " + field.useName() + ";");
      }
      writeln(3, "recs.addElement(rec);");
      writeln(2, "}");
      writeln(2, "" + extendsName + "[] result = new " + extendsName + "[recs.size()];");
      writeln(2, "for (int i=0; i<recs.size();i++)");
      writeln(3, "result[i] = (" + extendsName + ")recs.elementAt(i); ");
      writeln(2, "return result;");
      writeln(1, "}");
    }
    if (proc.inputs.size() > 0 || proc.dynamics.size() > 0)
    {
      writeln(1, "/**");
      if (proc.outputs.size() == 0)
        writeln(1, " * Returns no records.");
      else if (proc.isSingle)
      {
        writeln(1, " * Returns at most one record.");
        writeln(1, " * @return true if a record is returned.");
      } else
      {
        writeln(1, " * Returns any number of records.");
        writeln(1, " * @return result set of records found");
      }
      for (int i = 0; i < proc.inputs.size(); i++)
      {
        Field field = proc.inputs.elementAt(i);
        if ((field.isSequence && proc.isInsert)
                || (field.type == Field.TIMESTAMP)
                || (field.type == Field.USERSTAMP))
          continue;
        if (!field.isPrimaryKey)
          continue;
        writeln(1, " * @param " + field.useName() + " key input.");
      }
      for (int i = 0; i < proc.inputs.size(); i++)
      {
        Field field = proc.inputs.elementAt(i);
        if ((field.isSequence && proc.isInsert)
                || (field.type == Field.TIMESTAMP)
                || (field.type == Field.USERSTAMP))
          continue;
        if (field.isPrimaryKey)
          continue;
        writeln(1, " * @param " + field.useName() + " input.");
      }
      for (int i = 0; i < proc.dynamics.size(); i++)
        writeln(1, " * @param " + proc.name + " dynamic input.");
      writeln(1, " * @exception SQLException is passed through");
      writeln(1, " */");
      if (proc.outputs.size() == 0)
        writeln(1, "public void " + procName + "(");
      else if (proc.isSingle)
        writeln(1, "public boolean " + procName + "(");
      else
        writeln(1, "public Query " + procName + "(");
      String comma = "    ";
      for (int i = 0; i < proc.inputs.size(); i++)
      {
        Field field = proc.inputs.elementAt(i);
        if ((field.isSequence && proc.isInsert)
                || (field.type == Field.TIMESTAMP)
                || (field.type == Field.USERSTAMP))
          continue;
        if (!field.isPrimaryKey)
          continue;
        writeln(comma + javaVar(field));
        comma = "  , ";
      }
      for (int i = 0; i < proc.inputs.size(); i++)
      {
        Field field = proc.inputs.elementAt(i);
        if ((field.isSequence && proc.isInsert)
                || (field.type == Field.TIMESTAMP)
                || (field.type == Field.USERSTAMP))
          continue;
        if (field.isPrimaryKey)
          continue;
        writeln(comma + javaVar(field));
        comma = "  , ";
      }
      for (int i = 0; i < proc.dynamics.size(); i++)
      {
        String name = proc.dynamics.elementAt(i);
        writeln(comma + "String " + name);
        comma = "  , ";
      }
      writeln(1, ") throws SQLException");
      writeln(1, "{");
      for (int i = 0; i < proc.inputs.size(); i++)
      {
        Field field = proc.inputs.elementAt(i);
        if ((field.isSequence && proc.isInsert)
                || (field.type == Field.TIMESTAMP)
                || (field.type == Field.USERSTAMP))
          continue;
        String usename = field.useName();
        writeln(2, "this." + usename + " = " + usename + ";");
      }
      for (int i = 0; i < proc.dynamics.size(); i++)
      {
        String name = proc.dynamics.elementAt(i);
        writeln(2, "this." + name + " = " + name + ";");
      }
      if (proc.outputs.size() > 0)
        writeln(2, "return " + procName + "();");
      else
        writeln(2, "" + procName + "();");
      writeln(1, "}");
    }
  }

  /**
   * Translates field type to java data member type
   */
  static String javaVar(Field field)
  {
    switch (field.type)
    {
      case Field.BYTE:
        return "byte " + field.useName();
      case Field.SHORT:
        return "short " + field.useName();
      case Field.INT:
      case Field.SEQUENCE:
      case Field.IDENTITY:
        return "int " + field.useName();
      case Field.LONG:
        return "long " + field.useName();
      case Field.CHAR:
      case Field.ANSICHAR:
        return "String " + field.useName();
      case Field.DATE:
        return "Date " + field.useName();
      case Field.DATETIME:
        return "Date " + field.useName();
      case Field.TIME:
        return "Time " + field.useName();
      case Field.TIMESTAMP:
        return "Timestamp " + field.useName();
      case Field.FLOAT:
      case Field.DOUBLE:
        return "double " + field.useName();
      case Field.BLOB:
      case Field.TLOB:
        return "String " + field.useName();
      case Field.MONEY:
        return "double " + field.useName();
      case Field.USERSTAMP:
        return "String " + field.useName();
    }
    return "unknown";
  }

  /**
   * returns the data member initialisation code (not always neccessary in java but
   * still we do it)
   */
  static String initJavaVar(Field field)
  {
    switch (field.type)
    {
      case Field.BYTE:
        return field.useName() + " = 0;";
      case Field.CHAR:
      case Field.ANSICHAR:
        return field.useName() + " = \"\";";
      case Field.DATE:
        return field.useName() + " = new Date(0);";
      case Field.DATETIME:
        return field.useName() + " = new Date(0);";
      case Field.FLOAT:
      case Field.DOUBLE:
        return field.useName() + " = 0.0;";
      case Field.BLOB:
      case Field.TLOB:
        return field.useName() + " = \"\";";
      case Field.INT:
      case Field.SEQUENCE:
      case Field.IDENTITY:
        return field.useName() + " = 0;";
      case Field.LONG:
        return field.useName() + " = 0;";
      case Field.MONEY:
        return field.useName() + " = 0.0;";
      case Field.SHORT:
        return field.useName() + " = 0;";
      case Field.TIME:
        return field.useName() + " = new Time(0);";
      case Field.TIMESTAMP:
        return field.useName() + " = new Timestamp(0);";
      case Field.USERSTAMP:
        return field.useName() + " = \"\";";
    }
    return "unknown";
  }

  /**
   * JDBC get and set type for field data transfers
   */
  static String setType(Field field)
  {
    switch (field.type)
    {
      case Field.BYTE:
        return "Byte";
      case Field.CHAR:
      case Field.ANSICHAR:
        return "String";
      case Field.DATE:
        return "Date";
      case Field.DATETIME:
        return "Date";
      case Field.FLOAT:
      case Field.DOUBLE:
        return "Double";
      case Field.BLOB:
      case Field.TLOB:
        return "String";
      case Field.INT:
      case Field.SEQUENCE:
      case Field.IDENTITY:
        return "Int";
      case Field.LONG:
        return "Long";
      case Field.MONEY:
        return "Double";
      case Field.SHORT:
        return "Short";
      case Field.TIME:
        return "Time";
      case Field.TIMESTAMP:
        return "Timestamp";
      case Field.USERSTAMP:
        return "String";
    }
    return "unknown";
  }

  static String padString = "                                                         ";

  private static String padded(int size)
  {
    if (size == 0)
      return "";
    if (size > padString.length())
      size = padString.length();
    return padString.substring(0, size);
  }
}
