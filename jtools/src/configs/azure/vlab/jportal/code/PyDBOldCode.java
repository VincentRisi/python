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

import azure.vlab.jportal.*;
import vlab.jportal.*;

import java.io.*;
import java.util.Properties;

import static azure.vlab.jportal.Writer.*;

public class PyDBOldCode extends Generator
{
  private static PrintWriter outLog;
  static private Properties properties;
  private static boolean dbapiLowercase = false;
  private static boolean dbapiUppercase = false;

  public static String description()
  {
    return "Generate DBOLd Code for DBApi";
  }

  public static String documentation()
  {
    return "Generate DBOld Code for DBApi";
  }

  static public void generate(Database database, String output, PrintWriter outLog)
  {
    PyDBOldCode.outLog = outLog;
    try
    {
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
      for (int i = database.flags.size() - 1; i >= 0; i--)
      {
        String flag = database.flags.elementAt(i);
        flag = flag.toLowerCase();
        boolean dropParameter = false;
        if (flag.startsWith("%"))
        {
          flag = flag.substring(1);
          dropParameter = true;
        }
        if (flag.equals("dbapi=lowercase"))
          dbapiLowercase = true;
        if (flag.equals("dbapi=uppercase"))
          dbapiUppercase = true;
        if (dropParameter)
          database.flags.remove(i);
      }
      for (int i = 0; i < database.tables.size(); i++)
      {
        Table table = database.tables.elementAt(i);
        generateDB(table, output);
      }
    }
    catch (Exception ex)
    {
      outLog.println(ex);
      ex.printStackTrace(outLog);
    }
  }
  private static void generateDB(Table table, String output) throws Exception
  {
    String dbapiTableName = table.useName();
    if (dbapiLowercase) dbapiTableName = table.useName().toLowerCase();
    else if (dbapiUppercase) dbapiTableName = table.useName().toUpperCase();
    String fileName = output + "DB_" + table.useName().toUpperCase() + ".py";
    outLog.println("Code: " + fileName);
    try (OutputStream outFile = new FileOutputStream(fileName))
    {
      writer = new PrintWriter(outFile);
      indent_size = 4;
      writeln("# This code was generated, do not modify it, modify it at source and regenerate it.");
      writeln("# see " + table.useName() + " source file");
      writeln();
      writeln(format("from %sDBApi import *", dbapiTableName));
      writeln();
      generateDBEnums(table);
      generateDBCode(table);
      writer.flush();
    }
  }

  static private String getProperty(String propName, String propDefault)
  {
    if (properties == null)
      return propDefault;
    String propValue = properties.getProperty(propName);
    if (propValue == null)
      return propDefault;
    return propName + "=" + propValue;
  }

  static private boolean getProperty(String propName, boolean propDefault)
  {
    if (properties == null)
      return propDefault;
    String propValue = properties.getProperty(propName);
    if (propValue == null)
      return propDefault;
    return propValue.equalsIgnoreCase("true");
  }

  static private String _commanull(Field field)
  {
    if (field.isNull) return (", null=True");
    return "";
  }

  static private String _commapkey(Field field)
  {
    if (field.isPrimaryKey) return (", pkey=True");
    return "";
  }

  static private String _null(Field field)
  {
    if (field.isNull) return ("null=True");
    return "";
  }

  static private String _pkey(Field field)
  {
    if (field.isPrimaryKey)
      if (field.isNull)
        return (", pkey=True");
      else
        return ("pkey=True");
    return "";
  }

  static private void generateDBEnums(Table table)
  {
    for (int i = 0; i < table.fields.size(); i++)
    {
      Field field = table.fields.elementAt(i);
      generateDBEnums(table.useName() + field.useName(), field);
    }
  }

  static private void generateDBEnums(String baseName, Field field)
  {
    if (field.enums.size() > 0)
    {
      generateDBEnumsAsDict(baseName, field);
      writeln();
    }
  }

  static private void generateDBEnumsAsDict(String baseName, Field field)
  {
    if (field.enums.size() > 0)
      writeln(format("%1$sConst = %1$s", baseName));
  }

  static private void generateDBCode(Table table)
  {
    String parent = "";
    String current = "";
    writeln(format("class DB%1$s(D%1$s):", table.useName()));
    writeln(1, "def __init__(self, connect):");
    writeln(2, format("D%s.__init__(self)", table.useName()));
    writeln(2, "self.connect = connect");
    writeln(1, "def set_connect(self, connect):");
    writeln(2, "self.connect = connect");
    for (int i = 0; i < table.procs.size(); i++)
    {
      Proc proc = table.procs.elementAt(i);
      if (proc.isData)
        continue;
      if (proc.isStd == false && proc.isStdExtended() == false && proc.hasNoData() == false)
        continue;
      callDBApiIO(table, proc);
    }
    for (int i = 0; i < table.procs.size(); i++)
    {
      Proc proc = table.procs.elementAt(i);
      if (proc.isData)
        continue;
      if (proc.isStd || proc.isStdExtended() || proc.hasNoData())
        continue;
      writeln();
      writeln(format("class DB%1$s%2$s(D%1$s%2$s):", table.useName(), proc.name));
      writeln(1, "def __init__(self, connect):");
      writeln(2, format("D%s%s.__init__(self)", table.useName(), proc.name));
      writeln(2, "self.connect = connect");
      writeln(1, "def set_connect(self, connect):");
      writeln(2, "self.connect = connect");
      callDBApiIO(table, proc);
    }
  }

  private static void callDBApiIO(Table table, Proc proc)
  {
    String withParms = "run";
    String hasData = "exec";
    if (proc.isSingle)
    {
      if (proc.isInsert)
        withParms = "run";
      else
        withParms = "read";
    }
    else if (proc.outputs.size() > 0)
    {
      hasData = "load";
      withParms = "exec";
    }
    if (proc.hasNoData())
      hasData = "run";
    writeln(1, format("def %s%s(self):", hasData, proc.name));
    writeln(2, format("dbapi = %s%s()", table.useName(), proc.name));
    for (Field field: proc.inputs)
    {
      switch(field.type)
      {
        case Field.IDENTITY, Field.BIGIDENTITY -> { if (proc.isInsert == false) writeln(2, format("dbapi.%1$s = self.%1$s", field.useName()));}
        case Field.SEQUENCE, Field.BIGSEQUENCE -> { if (proc.isInsert == false || proc.hasReturning == false) writeln(2, format("dbapi.%1$s = self.%1$s", field.useName()));}
        case Field.TIMESTAMP, Field.USERSTAMP -> {}
        case Field.DATETIME -> writeln(2, format("dbapi.%1$s = dbapi_util.to_date14(self.%1$s)", field.useName()));
        case Field.DATE -> writeln(2, format("dbapi.%1$s = dbapi_util.to_date8(self.%1$s)", field.useName()));
        case Field.TIME -> writeln(2, format("dbapi.%1$s = dbapi_util.to_time6(self.%1$s)", field.useName()));
        default -> writeln(2, format("dbapi.%1$s = self.%1$s", field.useName()));
      };
    }
    for (String dynamic: proc.dynamics)
      writeln(2, format("dbapi.%1$s = self.%1$s", dynamic));
    if (proc.hasNoData())
    {
      writeln(2, format("dbapi.execute(self.connect)"));
      return;
    }
    String ret = "";
    String res = "";
    String execute="execute";
    if (proc.outputs.size() > 0)
    {
      if (proc.isSingle == false)
          res = "records = ";
      else
      {
        res = "rc, record = ";
        execute = "readone";
      }
      ret = "return ";
    }
    writeln(2, format("%sdbapi.%s(self.connect)", res, execute));
    if (proc.isSingle)
    {
      writeln(2, "if rc == False: return 0");
      for (Field field: proc.outputs)
      {
        switch(field.type)
        {
          case Field.DATETIME, Field.TIMESTAMP -> writeln(2, format("self.%1$s = dbapi_util.to_char14(record.%1$s)", field.useName()));
          case Field.DATE -> writeln(2, format("self.%1$s = dbapi_util.to_char8(record.%1$s)", field.useName()));
          case Field.TIME -> writeln(2, format("self.%1$s = dbapi_util.to_char6(record.%1$s)", field.useName()));
          default -> writeln(2, format("self.%1$s = record.%1$s", field.useName()));
        };
      }
      writeln(2, "return 1");
    }
    else if (ret.length() > 0)
    {
      writeln(2, "others = list()");
      writeln(2, "for rec in records:");
      if (proc.isStd || proc.isStdExtended())
        writeln(3, format("other = D%s()", table.useName()));
      else
        writeln(3, format("other = D%s%s()", table.useName(), proc.name));
      for (Field field: proc.outputs)
      {
        switch(field.type)
        {
          case Field.DATETIME, Field.TIMESTAMP -> writeln(3, format("other.%1$s = dbapi_util.to_char14(rec.%1$s)", field.useName()));
          case Field.DATE -> writeln(3, format("other.%1$s = dbapi_util.to_char8(rec.%1$s)", field.useName()));
          case Field.TIME -> writeln(3, format("other.%1$s = dbapi_util.to_char6(rec.%1$s)", field.useName()));
          default -> writeln(3, format("other.%1$s = rec.%1$s", field.useName()));
        };
      }
      for (Field field: proc.inputs)
      {
        if (proc.hasOutput(field.name)) continue;
        switch(field.type)
        {
          case Field.DATETIME, Field.TIMESTAMP -> writeln(3, format("other.%1$s = dbapi_util.to_char14(rec.%1$s)", field.useName()));
          case Field.DATE -> writeln(3, format("other.%1$s = dbapi_util.to_char8(rec.%1$s)", field.useName()));
          case Field.TIME -> writeln(3, format("other.%1$s = dbapi_util.to_char6(rec.%1$s)", field.useName()));
          default -> writeln(3, format("other.%1$s = rec.%1$s", field.useName()));
        };
      }
      writeln(3, "others.append(other)");
      writeln(2, "return others");
    }
    String parms = "";
    var code = new StringBuilder();
    for (Field field: proc.inputs)
    {
      if (proc.isInsert && (field.type == Field.SEQUENCE || field.type == Field.IDENTITY
      || field.type == Field.BIGSEQUENCE || field.type == Field.BIGIDENTITY
      || field.type == Field.TIMESTAMP || field.type == Field.USERSTAMP))
        continue;
      if (proc.isUpdate && (field.type == Field.TIMESTAMP || field.type == Field.USERSTAMP))
        continue;
      parms += format(", %s", field.useName());
      switch (field.type)
      {
        case Field.DATETIME, Field.TIMESTAMP -> code.append(format("%sself.%2$s = dbapi_util.to_char14(%2$s)\n", indent(2), field.useName()));
        case Field.DATE -> code.append(format("%sself.%2$s = dbapi_util.to_char8(%2$s)\n", indent(2), field.useName()));
        case Field.TIME -> code.append(format("%sself.%2$s = dbapi_util.to_char6(%2$s)\n", indent(2), field.useName()));
        default -> code.append(format("%sself.%2$s = %2$s\n", indent(2), field.useName()));
      }
    }
    code.append(format("%s%sself.%s%s()\n", indent(2), ret, hasData, proc.name));
    writeln(1, format("def %s%s(self%s):", withParms, proc.name, parms));
    write(code.toString());
  }

  static private boolean isNull(Field field)
  {
    if (field.isNull == false)
      return false;
    return switch (field.type)
            {
              case Field.BOOLEAN, Field.FLOAT, Field.DOUBLE, Field.MONEY, Field.BYTE, Field.SHORT, Field.INT, Field.LONG, Field.IDENTITY, Field.SEQUENCE, Field.BIGIDENTITY, Field.BIGSEQUENCE, Field.BLOB, Field.DATE, Field.DATETIME, Field.TIMESTAMP, Field.TIME -> true;
              default -> false;
            };
  }
}
