package configs.azure.vlab.jportal.code;

import azure.vlab.jportal.*;
import vlab.jportal.*;

import java.io.FileOutputStream;
import java.io.PrintWriter;
import java.util.Vector;

import static azure.vlab.jportal.Writer.*;

public class KotlinCode extends Generator
{
  public static String description()
  {
    return "generate Kotlin code";
  }

  public static String documentation()
  {
    return "generate Kotlin code";
  }

  static private final byte paramStyle = PlaceHolder.QUESTION;

  public static void generate(Database database, String output, PrintWriter outLog)
  {
    for (int i = 0; i < database.tables.size(); i++)
    {
      Table table = database.tables.elementAt(i);
      generate(table, output, outLog);
    }
  }

  static private String fileName(String output, String node, String ext)
  {
    int p = output.indexOf('\\');
    return output + node + ext;
  }

  static private void generate(Table table, String output, PrintWriter outLog)
  {
    try (PrintWriter outData = new PrintWriter(new FileOutputStream(fileName(output, table.useName(), ".kt"))))
    {
      writer = outData;
      indent_size = 4;
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

  static void generateStdProcs(Table table)
  {
    if (table.database.packageName.length() > 0)
      writeln("package " + table.database.packageName + "");
    writeln("import vlab.jportal.util.*");
    writeln("import java.sql.*");
    writeln(format("class %s(val connector: Connector)", table.useName()));
    writeln("{");
    writeln(1, "var connection: Connection = connector.connection,");
    for (int i = 0; i < table.fields.size(); i++)
    {
      Field field = table.fields.elementAt(i);
      writeln(1, format("var %s = %s,", kotlinVar(field), initKotlinVar(field)));
    }
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
  }

  static void generateOtherProcs(Table table, String output, PrintWriter outLog)
  {
    for (int i = 0; i < table.procs.size(); i++)
    {
      Proc proc = table.procs.elementAt(i);
      if (proc.isData)
        continue;
      if (!proc.isStd && !proc.hasNoData())
      {
        try (PrintWriter outData = new PrintWriter(new FileOutputStream(fileName(output, table.useName() + proc.upperFirst(), ".kt"))))
        {
          writer = outData;
          indent_size = 4;
          if (table.database.packageName.length() > 0)
          {
            writeln("package " + table.database.packageName);
          }
          writeln("import jportal.*");
          writeln("import java.sql.*");
          writeln("// This code was generated, do not modify it, modify it at source and regenerate it.");
          writeln(format("class %s%s(val connector: Connector)", table.useName(), proc.upperFirst()));
          writeln("{");
          writeln(1, "var connection: Connection = connector.connection,");
          for (int j = 0; j < proc.inputs.size(); j++)
          {
            Field field = proc.inputs.elementAt(j);
            writeln(1, format("var %s = %s,", kotlinVar(field), initKotlinVar(field)));
          }
          for (int j = 0; j < proc.outputs.size(); j++)
          {
            Field field = proc.outputs.elementAt(j);
            if (!proc.hasInput(field.name))
            {
              writeln(1, format("var %s = %s,", kotlinVar(field), initKotlinVar(field)));
            }
          }
          for (int j = 0; j < proc.dynamics.size(); j++)
          {
            String s = proc.dynamics.elementAt(j);
            writeln(1, format("var %s = \"\",", s));
          }
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
    }
  }

  static void emitStaticProc(Proc proc)
  {
    writeln(1, "/**");
    writeln(1, "* class method as it has no input or output.");
    writeln(1, "* @exception SQLException is passed through");
    writeln(1, "*/");
    writeln(1, format("static void (Connector connector) throws SQLException", proc.lowerFirst()));
    generateCommand(proc, "statement");
    writeln(2, "PreparedStatement prep = connector.connection.prepareStatement(statement);");
    writeln(2, "prep.executeUpdate();");
    writeln(2, "prep.close();");
    writeln(1, "}");
  }

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
      writeln(2, format("val %s = String.format(%s", name, trip));
    else
      writeln(2, format("val %s = %s", name, trip));
    for (int i = 0; i < lines.size(); i++)
    {
      String string = lines.elementAt(i);
      if (string.charAt(0) == '"')
      {
        String line=string.replaceAll("\"", "").trim();
        if (useBuf)
          line=line.replaceAll("%", "%%");
        if (line.length() > 0)
          writeln(2, line);
      }
      else
        writeln(2, "%s");
    }
    if (useBuf)
      writeln(2, format("%s.trimIndent()%s);", trip, buf.toString()));
    else
      writeln(2, format("%s.trimIndent()", trip));
  }

  static void emitProc(Proc proc)
  {
    String result;
    if (proc.outputs.size() == 0)
      result = "";
    else if (proc.isSingle)
      result = ": Boolean";
    else
      result = ": ResultSet";
    writeln(1, format("fun %s()%s", proc.lowerFirst(), result));
    writeln(1, "{");
    generateCommand(proc, "statement");
    writeln(2, "PreparedStatement prep = connection.prepareStatement(statement)");
    for (int i = 0; i < proc.inputs.size(); i++)
    {
      Field field = proc.inputs.elementAt(i);
      if (proc.isInsert)
      {
        if (field.isSequence)
          writeln(2, "" + field.name + " = connector.getSequence(\"" + proc.table.useName() + "\")");
      }
      if (field.type == Field.TIMESTAMP)
        writeln(2, "" + field.name + " = connector.getTimestamp()");
      if (field.type == Field.USERSTAMP)
        writeln(2, "" + field.name + " = connector.getUserstamp()");
    }
    if (proc.placeHolders.size() > 0)
    {
      for (int ph = 0; ph < proc.placeHolders.size(); ph++)
      {
        String placeHolder = proc.placeHolders.elementAt(ph);
        int i = proc.indexOf(placeHolder);
        Field field = proc.inputs.elementAt(i);
        write(2, "prep.set");
        write(setType(field));
        write("(");
        write(format("%d", ph + 1));
        writeln(", " + field.name + ")");
      }
    } else
    {
      for (int i = 0; i < proc.inputs.size(); i++)
      {
        Field field = proc.inputs.elementAt(i);
        write(2, "prep.set");
        write(setType(field));
        write("(");
        write(format("%d", i + 1));
        writeln(", " + field.name + ")");
      }
    }
    if (proc.outputs.size() > 0)
    {
      writeln(2, "result: ResultSet  = prep.executeQuery()");
      if (!proc.isSingle)
      {
        writeln(2, "return result");
        writeln(1, "}");
        writeln(1, format("fun %s(ResultSet result) : Boolean", proc.lowerFirst()));
        writeln(1, "{");
        writeln(2, "if (!result.next())");
        writeln(2, "{");
        writeln(3, "result.close()");
        writeln(3, "return false");
        writeln(2, "}");
      } else
      {
        writeln(2, "if (!result.next())");
        writeln(2, "{");
        writeln(3, "result.close()");
        writeln(3, "return false");
        writeln(2, "}");
      }
      for (int i = 0; i < proc.outputs.size(); i++)
      {
        Field field = proc.outputs.elementAt(i);
        write(2, "" + field.name + " =  result.get");
        write(setType(field));
        write("(");
        write(format("%d", i + 1));
        writeln(")");
      }
      if (proc.isSingle)
      {
        writeln(2, "result.close()");
        writeln(2, "prep.close()");
      }
      writeln(2, "return true");
    } else
    {
      writeln(2, "prep.executeUpdate()");
      writeln(2, "prep.close()");
    }
    writeln(1, "}");
    if (proc.inputs.size() > 0 || proc.dynamics.size() > 0)
    {
      writeln(1, "fun " + proc.lowerFirst() + "(");
      for (int i = 0; i < proc.inputs.size(); i++)
      {
        Field field = proc.inputs.elementAt(i);
        if ((field.isSequence && proc.isInsert)
                || (field.type == Field.TIMESTAMP)
                || (field.type == Field.USERSTAMP))
          continue;
        if (!field.isPrimaryKey)
          continue;
        writeln(2, format("val %s,", kotlinVar(field)));
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
        writeln(2, format("val %s,", kotlinVar(field)));
      }
      for (int i = 0; i < proc.dynamics.size(); i++)
      {
        String name = proc.dynamics.elementAt(i);
        writeln(2, format("val %s,", name));
      }
      writeln(2, format(") %s", result));
      writeln(2, "{");
      for (int i = 0; i < proc.inputs.size(); i++)
      {
        Field field = proc.inputs.elementAt(i);
        if ((field.isSequence && proc.isInsert)
                || (field.type == Field.TIMESTAMP)
                || (field.type == Field.USERSTAMP))
          continue;
        String usename = field.useName();
        writeln(2, format("this.%1$s = %1$s", usename));
      }
      for (int i = 0; i < proc.dynamics.size(); i++)
      {
        String name = proc.dynamics.elementAt(i);
        writeln(2, format("this.%1$s = %1$s", name));
      }
      if (proc.outputs.size() > 0)
        writeln(2, "return " + proc.lowerFirst() + "()");
      else
        writeln(2, "" + proc.lowerFirst() + "()");
      writeln(1, "}");
    }
  }

  static String kotlinVar(Field field)
  {
    switch (field.type)
    {
      case Field.BYTE:
        return format("%s: Byte", field.useName());
      case Field.SHORT:
        return format("%s: Short", field.useName());
      case Field.INT:
      case Field.SEQUENCE:
      case Field.IDENTITY:
        return format("%s: Int", field.useName());
      case Field.LONG:
        return format("%s: Long", field.useName());
      case Field.CHAR:
      case Field.ANSICHAR:
        return format("%s: String", field.useName());
      case Field.DATE:
        return format("%s: Date", field.useName());
      case Field.DATETIME:
        return format("%s: Timestamp", field.useName());
      case Field.TIME:
        return format("%s: Time", field.useName());
      case Field.TIMESTAMP:
        return format("%s: Timestamp", field.useName());
      case Field.FLOAT:
      case Field.DOUBLE:
        return format("%s: Double", field.useName());
      case Field.BLOB:
      case Field.TLOB:
        return format("%s: String", field.useName());
      case Field.MONEY:
        return format("%s: Double", field.useName());
      case Field.USERSTAMP:
        return format("%s: String", field.useName());
    }
    return format("//:%s: unknown", field.useName());
  }

  static String initKotlinVar(Field field)
  {
    switch (field.type)
    {
      case Field.BYTE:
        return "0";
      case Field.CHAR:
      case Field.ANSICHAR:
        return "\"\"";
      case Field.DATE:
        return "Date(0)";
      case Field.DATETIME:
        return "new Date(0)";
      case Field.FLOAT:
      case Field.DOUBLE:
        return "0.0";
      case Field.BLOB:
      case Field.TLOB:
        return "\"\"";
      case Field.INT:
      case Field.SEQUENCE:
      case Field.IDENTITY:
        return "0";
      case Field.LONG:
        return "0";
      case Field.MONEY:
        return "0.0";
      case Field.SHORT:
        return "0";
      case Field.TIME:
        return "new Time(0)";
      case Field.TIMESTAMP:
        return "new Timestamp(0)";
      case Field.USERSTAMP:
        return "\"\"";
    }
    return format("//:%s: %d unknown", field.useName(), field.type);
  }

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
}
