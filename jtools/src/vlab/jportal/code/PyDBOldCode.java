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

package vlab.jportal.code;

import vlab.jportal.*;

import java.io.*;
import java.util.Properties;
import java.util.Vector;

import static vlab.jportal.PlaceHolder.*;
import static vlab.jportal.Writer.*;

public class PyDBOldCode extends Generator
{
  private static PrintWriter outLog;
  static private Properties properties;

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
    String fileName = output + "DB_" + table.useName().toUpperCase() + ".py";
    outLog.println("Code: " + fileName);
    try (OutputStream outFile = new FileOutputStream(fileName))
    {
      writer = new PrintWriter(outFile);
      indent_size = 4;
      writeln("# This code was generated, do not modify it, modify it at source and regenerate it.");
      writeln("# see " + table.useName() + " source file");
      writeln();
      writeln(format("from %sDBApi import *", table.useName()));
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

  static private void generateAnnotates(Vector allFields)
  {
    for (int i = 0; i < allFields.size(); i++)
    {
      Field field = (Field) allFields.elementAt(i);
      write(1, format("%s: ", field.useName()));
      switch (field.type)
      {
        case Field.ANSICHAR:
          writeln(format("Char(%d%s%s%s)", field.length + 1, _commanull(field), _commapkey(field)));
          break;
        case Field.AUTOTIMESTAMP:
          writeln(format("TimeStamp(%s%s%s)", _null(field), _pkey(field)));
          break;
        case Field.BIGIDENTITY:
        case Field.BIGSEQUENCE:
        case Field.LONG:
          writeln(format("LongInt(%d%s%s)", field.length, _commanull(field), _commapkey(field)));
          break;
        case Field.BIGXML:
          writeln(format("XMLTYPE(%d%s%s)", field.length + 1, _commanull(field), _commapkey(field)));
          break;
        case Field.BLOB:
          writeln(format("Blob(%d%s%s)", field.length + 1, _commanull(field), _commapkey(field)));
          break;
        case Field.BOOLEAN:
          writeln(format("Boolean(%d%s%s)", field.length, _commanull(field), _commapkey(field)));
          break;
        case Field.BYTE:
          writeln(format("TinyInt(%d%s%s)", field.length, _commanull(field), _commapkey(field)));
          break;
        case Field.CHAR:
          writeln(format("Char(%d%s%s)", field.length + 1, _commanull(field), _commapkey(field)));
          break;
        case Field.DATE:
          writeln(format("Date(%s%s)", _null(field), _pkey(field)));
          break;
        case Field.DATETIME:
          writeln(format("DateTime(%s%s)", _null(field), _pkey(field)));
          break;
        case Field.DOUBLE:
        case Field.FLOAT:
          writeln(format("Float(%d, %d%s%s)", field.precision, field.scale, _commanull(field), _commapkey(field)));
          break;
        case Field.DYNAMIC:
          writeln(format("Unhandled('Dynamic', %d%s%s)", field.length, _commanull(field), _commapkey(field)));
          break;
        case Field.IDENTITY:
        case Field.INT:
        case Field.SEQUENCE:
          writeln(format("Int(%s%s%s)", field.length, _commanull(field), _commapkey(field)));
          break;
        case Field.IMAGE:
          writeln(format("Image(%s%s%s)", field.length + 1, _commanull(field), _commapkey(field)));
          break;
        case Field.MONEY:
          writeln(format("Char(%s%s%s)", field.length + 1, _commanull(field), _commapkey(field)));
          break;
        case Field.SHORT:
          writeln(format("SmallInt(%s%s%s)", field.length, _commanull(field), _commapkey(field)));
          break;
        case Field.STATUS:
          writeln(format("Status(%s%s%s)", field.length, _commanull(field), _commapkey(field)));
          break;
        case Field.TIME:
          writeln(format("Time(%s%s)", _null(field), _pkey(field)));
          break;
        case Field.TIMESTAMP:
          writeln(format("TimeStamp(%s%s)", _null(field), _pkey(field)));
          break;
        case Field.TLOB:
          writeln(format("Clob(%s%s%s)", field.length + 1, _commanull(field), _commapkey(field)));
          break;
        case Field.UID:
          writeln(format("Unhandled('UID', %s%sV)", field.length, _commanull(field), _commapkey(field)));
          break;
        case Field.USERSTAMP:
          writeln(format("UserStamp(%s%s%s)", field.length + 1, _commanull(field), _commapkey(field)));
          break;
        case Field.UTF8:
          writeln(format("Unhandled('UTF8', %s%s%s)", field.length + 1, _commanull(field), _commapkey(field)));
          break;
        case Field.WANSICHAR:
          writeln(format("Unhandled('WANSICHAR', %s%s%s)", field.length + 1, _commanull(field), _commapkey(field)));
          break;
        case Field.WCHAR:
          writeln(format("Unhandled('WCHAR', %s%s%s)", field.length + 1, _commanull(field), _commapkey(field)));
          break;
        case Field.XML:
          writeln(format("XMLTYPE(%s%s%s)", field.length + 1, _commanull(field), _commapkey(field)));
          break;
      }
    }
  }

  static private void generateDataFields(Vector allFields, String superName, String tableName)
  {
    String recName = superName.length() > 0 ? superName : tableName;
    write(1, "__slots__ = [");
    for (int i = 0; i < allFields.size(); i++)
    {
      Field field = (Field) allFields.elementAt(i);
      if (i != 0)
      {
        writeln(",");
        write(2, "");
      }
      write("'" + field.useName() + "'");
    }
    writeln("]");
    writeln(1, "def __init__(self):");
    for (int i = 0; i < allFields.size(); i++)
    {
      Field field = (Field) allFields.elementAt(i);
      if (isNull(field) == true)
        writeln(2, "self." + field.useName() + " = None");
      else
        writeln(2, "self." + field.useName() + " = ''");
    }
    writeln(1, "def _fields(self):");
    writeln(2, "return D" + recName + ".__slots__");
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
      _callDBApi(table, proc);
      //PlaceHolder holder = new PlaceHolder(proc, paramStyle, "");
      //Vector pairs = holder.getPairs();
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
      writeln(2, "self.connect = connect");
      writeln(1, "def set_connect(self, connect):");
      writeln(2, "self.connect = connect");
      _callDBApi(table, proc);
    }
  }

  private static void _callDBApi(Table table, Proc proc)
  {
    writeln(1, format("def exec%s(self):", proc.name));
    writeln(2, format("dbapi = %s%s()", table.useName(), proc.name));
    if (proc.hasNoData())
    {
      writeln(2, format("dbapi.execute(self.connect)"));
      return;
    }
    String ret = "";
    if (proc.outputs.size() > 0)
      ret = "return ";
    writeln(2, format("%sdbapi.execute(self.connect)", ret));
    String prefix = "run";
    String parms = "";
    var code = new StringBuilder();
    for (int i=0; i < proc.inputs.size(); i++)
    {
      Field field = proc.inputs.elementAt(i);
      parms += format(", %s", field.name);
      code.append(format("%sself.%2$s = %2$s\n", indent(2), field.name));
    }
    if (proc.isSingle) prefix = "read";
    else if (proc.outputs.size() > 0) prefix = "load";
    code.append(format("%s%sself.exec%s()\n", indent(2), ret, proc.name));
    writeln(1, format("def %s%s(self%s)", prefix, proc.name, parms));
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
