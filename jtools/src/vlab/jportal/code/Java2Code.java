///
/// System : JPortal
/// $Source: /main/nedcor/cvsroot/dev/jportal/Java2Code.java,v $
/// $Author: vince $
/// $Date: 2003/02/12 16:02:30 $
/// $Revision: 1.4 $
///

package vlab.jportal.code;

import java.io.FileOutputStream;
import java.io.PrintWriter;
import java.util.Vector;
import static vlab.jportal.PlaceHolder.QUESTION;
import static vlab.jportal.Writer.*;
import vlab.jportal.*;

public class Java2Code extends Generator
{
  /**
  * Generates the procedure classes for each table present.
  */
  public static String description()
  {
    return "generate Java2 code";
  }
  public static String documentation()
  {
    return "generate Java2 code";
  }
  static private byte paramStyle = QUESTION;
  public static void generate(Database database, String output, PrintWriter outLog)
  {
    for (int i=0; i<database.tables.size(); i++)
    {
      Table table = (Table) database.tables.elementAt(i);
      generate(table, output, outLog);
    }
  }
  /**
  * Build of standard and user defined procedures
  */
  static private String fileName(String output, String node, String ext)
  {
    int p = output.indexOf('\\');
    return output + node + ext;
  }
  static private void generate(Table table, String output, PrintWriter outLog)
  {
    try (PrintWriter outData = new PrintWriter(new FileOutputStream(fileName(output, table.useName(), ".java"))))
    {
      writer = outData;
      indent_size = 2;
      writeln("// This code was generated, do not modify it, modify it at source and regenerate it.");
      generateStdProcs(table);
      generateOtherProcs(table, output, outLog);
      writeln("}");
    }
    catch (Exception ex)
    {
      outLog.println(ex);
      ex.printStackTrace(outLog);
    }
  }
  /**
  * Build of all required standard procedures
  */
  static void generateStdProcs(Table table)
  {
    if (table.database.packageName.length() > 0)
      writeln("package " + table.database.packageName + ";");
    writeln("import jportal.*;");
    writeln("import java.sql.*;");
    writeln("/**");
    for (int i=0; i < table.comments.size(); i++)
    {
      String s = (String) table.comments.elementAt(i);
      writeln("*"+s);
    }
    writeln("* This code was generated, do not modify it, modify it at source and regenerate it.");
    writeln("*/");
    writeln("public class "+table.useName());
    writeln("{");
    writeln(1, "Connector connector;");
    writeln(1, "Connection connection;");
    for (int i=0; i<table.fields.size(); i++)
    {
      Field field = (Field) table.fields.elementAt(i);
      if (field.comments.size() > 0)
      {
        writeln(1, "/**");
        for (int c=0; c < field.comments.size(); c++)
        {
          String s = (String) field.comments.elementAt(c);
          writeln(1, "*"+s);
        }
        writeln(1, "*/");
      }
      writeln(1, "public "+javaVar(field)+";");
    }
    writeln(1, "/**");
    writeln(1, "* @param Connector for specific database");
    writeln(1, "*/");
    writeln(1, "public "+table.useName()+"(Connector connector)");
    writeln(1, "{");
    writeln(2, "this.connector = connector;");
    writeln(2, "connection = connector.connection;");
    for (int i=0; i<table.fields.size(); i++)
    {
      Field field = (Field) table.fields.elementAt(i);
      writeln(2, ""+initJavaVar(field));
    }
    writeln(1, "}");
    for (int i=0; i<table.procs.size(); i++)
    {
      Proc proc = (Proc) table.procs.elementAt(i);
      if (proc.isData)
        continue;
      if (proc.isStd)
        emitProc(proc, 2, false);
      else if (proc.hasNoData())
        emitStaticProc(proc);
    }
  }
  /**
  * Build of user defined procedures
  */
  static void generateOtherProcs(Table table, String output, PrintWriter outLog)
  {
    for (int i=0; i<table.procs.size(); i++)
    {
      Proc proc = (Proc) table.procs.elementAt(i);
      if (proc.isData)
        continue;
      if (!proc.isStd && !proc.hasNoData())
      {
        writeln(1, "/**");
        for (int j=0; j<proc.comments.size(); j++)
        {
          String comment = (String) proc.comments.elementAt(j);
          writeln(1, "*"+comment);
        }
        writeln(1, "*/");
        writeln(1, "public class " + proc.upperFirst());
        writeln(1, "{");
        for (int j=0; j<proc.inputs.size(); j++)
        {
          Field field = (Field) proc.inputs.elementAt(j);
          writeln(2, "/**");
          for (int c=0; c < field.comments.size(); c++)
          {
            String s = (String) field.comments.elementAt(c);
            writeln(2, "*"+s);
          }
          if (!proc.hasOutput(field.name))
            writeln(2, "* (input)");
          else
            writeln(2, "* (input/output)");
          writeln(2, "*/");
          writeln(2, "public "+javaVar(field)+";");
        }
        for (int j=0; j<proc.outputs.size(); j++)
        {
          Field field = (Field) proc.outputs.elementAt(j);
          if (!proc.hasInput(field.name))
          {
            writeln(2, "/**");
            for (int c=0; c < field.comments.size(); c++)
            {
              String s = (String) field.comments.elementAt(c);
              writeln(2, "*"+s);
            }
            writeln(2, "* (output)");
            writeln(2, "*/");
            writeln(2, "public "+javaVar(field)+";");
          }
        }
        for (int j=0; j<proc.dynamics.size(); j++)
        {
          String s = (String) proc.dynamics.elementAt(j);
          writeln(2, "/**");
          writeln(2, "* (dynamic)");
          writeln(2, "*/");
          writeln(2, "public String "+s+";");
        }
        writeln(2, "public " + proc.upperFirst()+"()");
        writeln(2, "{");
        for (int j=0; j<proc.inputs.size(); j++)
        {
          Field field = (Field) proc.inputs.elementAt(j);
          writeln(3, ""+initJavaVar(field));
        }
        for (int j=0; j<proc.outputs.size(); j++)
        {
          Field field = (Field) proc.outputs.elementAt(j);
          if (!proc.hasInput(field.name))
            writeln(3, ""+initJavaVar(field));
        }
        for (int j=0; j<proc.dynamics.size(); j++)
        {
          String s = (String) proc.dynamics.elementAt(j);
          writeln(3, ""+s+" = \"\";");
        }
        writeln(2, "}");
        emitProc(proc, 2, true);
        writeln(1, "}");
        writeln(1, "public "+proc.upperFirst()+" "+proc.lowerFirst()+" = new "+proc.upperFirst()+"();");
      }
    }
  }
  /**
  *
  */
  static private void generateCommand(Proc proc, String name)
  {
    PlaceHolder holder = new PlaceHolder(proc, paramStyle, "");
    Vector<String> lines = holder.getLines();
    String trip = "\"\"\"";
    var buf = new StringBuffer();
    boolean useBuf = false;
    String comma = "";
    for (int i = 0; i < lines.size(); i++)
    {
      String string = lines.elementAt(i);
      if (string.charAt(0) != '"')
      {
        useBuf = true;
        buf.append(format(", %s", string.trim()));
      }
    }
    if (useBuf)
      writeln(3, format("%s = String.format(%s", name, trip));
    else
      writeln(3, format("%s = %s", name, trip));
    for (int i = 0; i < lines.size(); i++)
    {
      String string = lines.elementAt(i);
      if (string.charAt(0) == '"')
        writeln(string.replaceAll("\"", ""));
      else
        writeln("%s");
    }
    if (useBuf)
      writeln(format("%s%s);", trip, buf.toString()));
    else
      writeln(format("%s;", trip));
  }
  /**
  * Emits a static or class method
  */
  static void emitStaticProc(Proc proc)
  {
    writeln(1, "/**");
    writeln(1, "* class method as it has no input or output.");
    writeln(1, "* @exception SQLException is passed through");
    writeln(1, "*/");
    writeln(1, "public static void "+proc.lowerFirst()+"(Connector connector) throws SQLException");
    writeln(1, "{");
    generateCommand(proc, "statement");
    writeln(2, "PreparedStatement prep = connector.connection.prepareStatement(statement);");
    writeln(2, "prep.executeUpdate();");
    writeln(2, "prep.close();");
    writeln(1, "}");
  }
  /** Emits class method for processing the database activity */
  static void emitProc(Proc proc, int indent, boolean useRun)
  {
    writeln(indent, "/**");
    if (proc.comments.size() > 0)
    {
      for (int i=0; i<proc.comments.size(); i++)
      {
        String comment = (String) proc.comments.elementAt(i);
        writeln(indent, "*"+comment);
      }
    }
    if (proc.outputs.size() == 0)
      writeln(indent, "* Returns no output.");
    else if (proc.isSingle)
    {
      writeln(indent, "* Returns at most one record.");
      writeln(indent, "* @return true if a record is found");
    }
    else
    {
      writeln(indent, "* Returns any number of records.");
      writeln(indent, "* @return result set of records found");
    }
    writeln(indent, "* @exception SQLException is passed through");
    writeln(indent, "*/");
    String procName = "run";
    if (useRun == false)
      procName = proc.lowerFirst();
    if (proc.outputs.size() == 0)
      writeln(indent, "public void "+procName+"() throws SQLException");
    else if (proc.isSingle)
      writeln(indent, "public boolean "+procName+"() throws SQLException");
    else
      writeln(indent, "public Query "+procName+"() throws SQLException");
    writeln(indent, "{");
    generateCommand(proc, "statement");
    writeln(indent+1, "PreparedStatement prep = connection.prepareStatement(statement);");
    for (int i=0; i<proc.inputs.size(); i++)
    {
      Field field = (Field) proc.inputs.elementAt(i);
      if (proc.isInsert)
      {
        if (field.isSequence)
          writeln(indent+1, ""+field.useName()+" = connector.getSequence(\""+proc.table.name+"\");");
      }
      if (field.type == field.TIMESTAMP)
        writeln(indent+1, ""+field.useName()+" = connector.getTimestamp();");
      if (field.type == field.USERSTAMP)
        writeln(indent+1, ""+field.useName()+" = connector.getUserstamp();");
    }
    if (proc.placeHolders.size() > 0)
    {
      for (int ph=0; ph<proc.placeHolders.size(); ph++)
      {
        String placeHolder = (String) proc.placeHolders.elementAt(ph);
        int i = proc.indexOf(placeHolder);
        Field field = (Field) proc.inputs.elementAt(i);
        write(indent+1, "prep.set");
        write(setType(field));
        write(format("(%d", ph+1));
        writeln(", "+field.useName()+");");
      }
    }
    else
    {
      for (int i=0; i<proc.inputs.size(); i++)
      {
        Field field = (Field) proc.inputs.elementAt(i);
        write(indent+1, "prep.set");
        write(setType(field));
        write(format("(%d", i+1));
        writeln(", "+field.useName()+");");
      }
    }
    if (proc.outputs.size() > 0)
    {
      writeln(indent+1, "ResultSet result = prep.executeQuery();");
      if (!proc.isSingle)
      {
        writeln(indent+1, "Query query = new Query(prep, result);");
        writeln(indent+1, "return query;");
        writeln(indent, "}");
        writeln(indent, "/**");
        writeln(indent, "* Returns the next record in a result set.");
        writeln(indent, "* @param result The result set for the query.");
        writeln(indent, "* @return true while records are found.");
        writeln(indent, "* @exception SQLException is passed through");
        writeln(indent, "*/");
        writeln(indent, "public boolean "+procName+"(Query query) throws SQLException");
        writeln(indent, "{");
        writeln(indent+1, "if (!query.result.next())");
        writeln(indent+1, "{");
        writeln(indent+2, "query.close();");
        writeln(indent+2, "return false;");
        writeln(indent+1, "}");
        writeln(indent+1, "ResultSet result = query.result;");
      }
      else
      {
        writeln(indent+1, "if (!result.next())");
        writeln(indent+1, "{");
        writeln(indent+2, "result.close();");
        writeln(indent+2, "prep.close();");
        writeln(indent+2, "return false;");
        writeln(indent+1, "}");
      }
      for (int i=0; i<proc.outputs.size(); i++)
      {
        Field field = (Field) proc.outputs.elementAt(i);
        write(indent+1, ""+field.useName()+" =  result.get");
        write(setType(field));
        write(format("(%d", i+1));
        writeln(");");
      }
      if (proc.isSingle)
      {
        writeln(indent+1, "result.close();");
        writeln(indent+1, "prep.close();");
      }
      writeln(indent+1, "return true;");
    }
    else
    {
      writeln(indent+1, "prep.executeUpdate();");
      writeln(indent+1, "prep.close();");
    }
    writeln(indent, "}");
    if (proc.inputs.size() > 0 || proc.dynamics.size() > 0)
    {
      writeln(indent, "/**");
      if (proc.outputs.size() == 0)
        writeln(indent, "* Returns no records.");
      else if (proc.isSingle)
      {
        writeln(indent, "* Returns at most one record.");
        writeln(indent, "* @return true if a record is returned.");
      }
      else
      {
        writeln(indent, "* Returns any number of records.");
        writeln(indent, "* @return result set of records found");
      }
      for (int i=0; i<proc.inputs.size(); i++)
      {
        Field field = (Field) proc.inputs.elementAt(i);
        if ((field.isSequence && proc.isInsert)
        || (field.type == field.TIMESTAMP)
        || (field.type == field.USERSTAMP))
          continue;
        if (!field.isPrimaryKey)
          continue;
        writeln(indent, "* @param "+field.useName()+" key input.");
      }
      for (int i=0; i<proc.inputs.size(); i++)
      {
        Field field = (Field) proc.inputs.elementAt(i);
        if ((field.isSequence && proc.isInsert)
        || (field.type == field.TIMESTAMP)
        || (field.type == field.USERSTAMP))
          continue;
        if (field.isPrimaryKey)
          continue;
        writeln(indent, "* @param "+field.useName()+" input.");
      }
      for (int i=0; i<proc.dynamics.size(); i++)
      {
        String name = (String) proc.dynamics.elementAt(i);
        writeln(indent, "* @param "+proc.name+" dynamic input.");
      }
      writeln(indent, "* @exception SQLException is passed through");
      writeln(indent, "*/");
      if (proc.outputs.size() == 0)
        writeln(indent, "public void "+procName+"(");
      else if (proc.isSingle)
        writeln(indent, "public boolean "+procName+"(");
      else
        writeln(indent, "public Query "+procName+"(");
      String comma = "";
      for (int i=0; i<proc.inputs.size(); i++)
      {
        Field field = (Field) proc.inputs.elementAt(i);
        if ((field.isSequence && proc.isInsert)
        || (field.type == field.TIMESTAMP)
        || (field.type == field.USERSTAMP))
          continue;
        if (!field.isPrimaryKey)
          continue;
        writeln(indent, comma+javaVar(field));
        comma = ", ";
      }
      for (int i=0; i<proc.inputs.size(); i++)
      {
        Field field = (Field) proc.inputs.elementAt(i);
        if ((field.isSequence && proc.isInsert)
        || (field.type == field.TIMESTAMP)
        || (field.type == field.USERSTAMP))
          continue;
        if (field.isPrimaryKey)
          continue;
        writeln(indent, comma+javaVar(field));
        comma = ", ";
      }
      for (int i=0; i<proc.dynamics.size(); i++)
      {
        String name = (String) proc.dynamics.elementAt(i);
        writeln(indent, comma+"String "+name);
        comma = ", ";
      }
      writeln(indent, ") throws SQLException");
      writeln(indent, "{");
      for (int i=0; i<proc.inputs.size(); i++)
      {
        Field field = (Field) proc.inputs.elementAt(i);
        if ((field.isSequence && proc.isInsert)
        || (field.type == field.TIMESTAMP)
        || (field.type == field.USERSTAMP))
          continue;
        String usename = field.useName();
        writeln(indent+1, "this."+usename+" = "+usename+";");
      }
      for (int i=0; i<proc.dynamics.size(); i++)
      {
        String name = (String) proc.dynamics.elementAt(i);
        writeln(indent+1, "this."+name+" = "+name+";");
      }
      if (proc.outputs.size() > 0)
        writeln(indent+1, "return "+procName+"();");
      else
        writeln(indent+1, ""+procName+"();");
      writeln(indent, "}");
    }
  }
  /**
  * Translates field type to java data member type
  */
  static String javaVar(Field field)
  {
    switch(field.type)
    {
    case Field.BYTE:
      return "byte "+ field.useName();
    case Field.SHORT:
      return "short "+ field.useName();
    case Field.INT:
    case Field.SEQUENCE:
    case Field.IDENTITY:
      return "int "+ field.useName();
    case Field.LONG:
      return "long "+ field.useName();
    case Field.CHAR:
    case Field.ANSICHAR:
      return "String "+ field.useName();
    case Field.DATE:
      return "Date "+ field.useName();
    case Field.DATETIME:
      return "Date "+ field.useName();
    case Field.TIME:
      return "Time "+ field.useName();
    case Field.TIMESTAMP:
      return "Timestamp "+ field.useName();
    case Field.FLOAT:
    case Field.DOUBLE:
      return "double "+ field.useName();
    case Field.BLOB:
    case Field.TLOB:
      return "String "+ field.useName();
    case Field.MONEY:
      return "double "+ field.useName();
    case Field.USERSTAMP:
      return "String "+ field.useName();
    }
    return "unknown";
  }
  /**
  * returns the data member initialisation code (not always neccessary in java but
  * still we do it)
  */
  static String initJavaVar(Field field)
  {
    switch(field.type)
    {
    case Field.BYTE:
      return field.useName() +" = 0;";
    case Field.CHAR:
    case Field.ANSICHAR:
      return field.useName() +" = \"\";";
    case Field.DATE:
      return field.useName() +" = new Date(0);";
    case Field.DATETIME:
      return field.useName() +" = new Date(0);";
    case Field.FLOAT:
    case Field.DOUBLE:
      return field.useName() +" = 0.0;";
    case Field.BLOB:
    case Field.TLOB:
      return field.useName() +" = \"\";";
    case Field.INT:
    case Field.SEQUENCE:
    case Field.IDENTITY:
      return field.useName() +" = 0;";
    case Field.LONG:
      return field.useName() +" = 0;";
    case Field.MONEY:
      return field.useName() +" = 0.0;";
    case Field.SHORT:
      return field.useName() +" = 0;";
    case Field.TIME:
      return field.useName() +" = new Time(0);";
    case Field.TIMESTAMP:
      return field.useName() +" = new Timestamp(0);";
    case Field.USERSTAMP:
      return field.useName() +" = \"\";";
    }
    return "unknown";
  }
  /**
  * JDBC get and set type for field data transfers
  */
  static String setType(Field field)
  {
    switch(field.type)
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
}
