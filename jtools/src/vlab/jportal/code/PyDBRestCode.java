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

import java.io.FileOutputStream;
import java.io.OutputStream;
import java.io.PrintWriter;

import static vlab.jportal.Writer.*;

public class PyDBRestCode extends Generator
{
  private static PrintWriter outLog;
  public static String description()
  {
    return "Generate DBApi Rest Code for Python";
  }
  public static String documentation()
  {
    return "Generate DBApi Rest Code for Python";
  }
  static public void generate(Database database, String output, PrintWriter outLog)
  {
    PyDBRestCode.outLog = outLog;
    try
    {
      for (int i = 0; i < database.tables.size(); i++)
      {
        Table table = database.tables.elementAt(i);
        generateRest(database, table, output);
      }
    }
    catch (Exception ex)
    {
      outLog.println(ex);
      ex.printStackTrace(outLog);
    }
  }
  static private void restInsert(Table table)
  {
    writeln(format("struct DB%sInsert \"%s.sh\"\n", table.useName(), table.useName().toLowerCase()));
    writeln(format("void %1$sInsert(DB%1$sInsert *rec)", table.useName()));
    writeln("{");
    writeln("message: #");
    writeln(format("openapi: post %1$s %1$s", table.useName()));
    writeln("input");
    writeln(1, "rec;");
    writeln("output");
    writeln(1, "rec;");
    writeln("code");
    writeln("PYTHON:");
    writeln(1, "try:");
    writeln(2, "rec.execute(connect)");
    writeln(2, "connect.commit()");
    writeln(1, "except DBError as db:");
    writeln(2, "log_error ('DBError: value:{0} rc:{1} ociErr:{2}'.format(db.value, db.rc, db.ociErr))");
    writeln(2, "connect.rollback()");
    writeln(1, "return rec");
    writeln("endcode");
    writeln("}");
    writeln("");
  }
  static private void restUpdate(Table table)
  {
    writeln(format("struct DB%sUpdate \"%s.sh\"\n", table.useName(), table.useName().toLowerCase()));
    writeln(format("void %1$sUpdate(DB%1$sUpdate *rec)", table.useName()));
    writeln("{");
    writeln("message: #");
    writeln(format("openapi: put %1$s %1$s", table.useName()));
    writeln("input");
    writeln(1, "rec;");
    writeln("output");
    writeln(1, "rec;");
    writeln("code");
    writeln("PYTHON:");
    writeln(1, "try:");
    writeln(2, "rec.execute(connect)");
    writeln(2, "connect.commit()");
    writeln(1, "except DBError as db:");
    writeln(2, "log_error ('DBError: value:{0} rc:{1} ociErr:{2}'.format(db.value, db.rc, db.ociErr))");
    writeln(2, "connect.rollback()");
    writeln(1, "return rec");
    writeln("endcode");
    writeln("}");
    writeln("");
  }
  static private void restDelete(Table table)
  {
    writeln(format("struct DB%sDeleteOne \"%s.sh\"\n", table.useName(), table.useName().toLowerCase()));
    writeln(format("void %1$sDelete(DB%1$sDeleteOne *rec)", table.useName()));
    writeln("{");
    writeln("message: #");
    writeln(format("openapi: delete %1$s %1$s", table.useName()));
    writeln("input");
    writeln(1, "rec;");
    writeln("code");
    writeln("PYTHON:");
    writeln(1, "try:");
    writeln(2, "rec.execute(connect)");
    writeln(2, "connect.commit()");
    writeln(1, "except DBError as db:");
    writeln(2, "log_error ('DBError: value:{0} rc:{1} ociErr:{2}'.format(db.value, db.rc, db.ociErr))");
    writeln(2, "connect.rollback()");
    writeln("endcode");
    writeln("}");
    writeln("");
  }
  static private void writeGet(Table table, Proc proc)
  {
    var builder = new StringBuilder();
    String name;
    if (proc.isStd)
      name = format("%s",table.useName());
    else
      name = format("%s%s", table.useName(), proc.name);
    builder.append(format("openapi: get \"%s", name));
    for (int i=0; i<proc.inputs.size(); i++)
    {
      Field input = proc.inputs.elementAt(i);
      builder.append(format("/%1$s/{%1$s}", input.name));
    }
    builder.append(format("\" %s", table.useName()));
    writeln(builder.toString());
  }
  static private String makeParms(Proc proc)
  {
    var builder = new StringBuilder();
    String comma="";
    for (int i=0; i<proc.inputs.size(); i++)
    {
      Field input = proc.inputs.elementAt(i);
      builder.append(format("%s%s %s", comma, typeof(input), input.name));
      comma = ", ";
    }
    return builder.toString();
  }
  private static String typeof(Field input)
  {
    return switch(input.type)
            {
              case Field.BLOB, Field.DYNAMIC, Field.TLOB, Field.USERSTAMP, Field.UID, Field.XML, Field.WCHAR, Field.WANSICHAR, Field.UTF8, Field.BIGXML, Field.IMAGE, Field.UNICODE -> "unused";
              case Field.BOOLEAN, Field.IDENTITY, Field.INT, Field.SEQUENCE -> "int";
              case Field.BYTE, Field.STATUS -> "byte";
              case Field.CHAR, Field.DATE, Field.DATETIME, Field.MONEY, Field.TIME, Field.TIMESTAMP, Field.ANSICHAR, Field.AUTOTIMESTAMP -> "String";
              case Field.DOUBLE, Field.FLOAT -> "double";
              case Field.LONG, Field.BIGSEQUENCE, Field.BIGIDENTITY -> "long";
              case Field.SHORT -> "short";
              default -> format("type:%d", input.type);
            };
  }
  private static void writeInputs(Table table, Proc proc)
  {
    for (int i=0; i<proc.inputs.size(); i++)
    {
      Field input = proc.inputs.elementAt(i);
      writeln(1, format("%s;", input.name));
    }
  }
  private static void writeSetInputs(Table table, Proc proc)
  {
    for (int i=0; i<proc.inputs.size(); i++)
    {
      Field input = proc.inputs.elementAt(i);
      writeln(2, format("rec.%1$s = %1$s", input.name));
    }
  }
  static private void restGetSingle(Table table, Proc proc)
  {
    writeln(format("struct DB%s%s \"%s.sh\"\n", table.useName(), proc.name, table.useName().toLowerCase()));
    writeln(format("void %1$s%2$s(%3$s, DB%1$s%2$s *rec)", table.useName(), proc.name, makeParms(proc)));
    writeln("{");
    writeln("message: #");
    writeGet(table, proc);
    writeln("input");
    writeInputs(table, proc);
    writeln("output");
    writeln(1, "rec;");
    writeln("code");
    writeln("PYTHON:");
    writeln(1, "try:");
    writeSetInputs(table, proc);
    writeln(2, "rec.execute(connect)");
    //writeln(2, "connect.commit()");
    writeln(1, "except DBError as db:");
    writeln(2, "log_error ('DBError: value:{0} rc:{1} ociErr:{2}'.format(db.value, db.rc, db.ociErr))");
    //writeln(2, "connect.rollback()");
    writeln(1, "return rec");
    writeln("endcode");
    writeln("}");
    writeln("");
  }
  static private void restGetMultiple(Table table, Proc proc)
  {
    writeln(format("struct DB%s%s \"%s.sh\"\n", table.useName(), proc.name, table.useName().toLowerCase()));
    if (proc.inputs.size() > 0)
       writeln(format("void %1$s%2$s(%3$s, int32* noOf, DB%1$s%2$s*& recs)", table.useName(), proc.name, makeParms(proc)));
    else
      writeln(format("void %1$s%2$s(int32* noOf, DB%1$s%2$s*& recs)", table.useName(), proc.name));
    writeln("{");
    writeln("message: #");
    writeGet(table, proc);
    if (proc.inputs.size() > 0)
    {
      writeln("input");
      writeInputs(table, proc);
    }
    writeln("output");
    writeln(1, "noOf;");
    writeln(1, "recs size(noOf);");
    writeln("code");
    writeln("PYTHON:");
    writeln(1, "try:");
    writeln(2, format("rec = DB%s%s()", table.useName(), proc.name));
    if (proc.inputs.size() > 0)
      writeSetInputs(table, proc);
    writeln(2, "recs = rec.execute(connect)");
    writeln(1, "except DBError as db:");
    writeln(2, "log_error ('DBError: value:{0} rc:{1} ociErr:{2}'.format(db.value, db.rc, db.ociErr))");
    writeln(1, "return recs");
    writeln("endcode");
    writeln("}");
    writeln("");
  }
  static private void restPosts(Table table, Proc proc)
  {
    writeln(format("struct DB%s%s \"%s.sh\"\n", table.useName(), proc.name, table.useName().toLowerCase()));
    writeln(format("void %1$s%2$s(DB%1$s%2$s* rec)", table.useName(), proc.name));
    writeln("{");
    writeln("message: #");
    String name;
    if (proc.isStd)
      name = format("%s",table.useName());
    else
      name = format("%s%s", table.useName(), proc.name);
    writeln(format("openapi: post %s %s", name, table.useName()));
    writeln("input");
    writeln(1, "rec;");
    writeln("output");
    writeln(1, "rec;");
    writeln("code");
    writeln("PYTHON:");
    writeln(1, "try:");
    writeln(2, "rec.execute(connect)");
    writeln(2, "connect.commit()");
    writeln(1, "except DBError as db:");
    writeln(2, "log_error ('DBError: value:{0} rc:{1} ociErr:{2}'.format(db.value, db.rc, db.ociErr))");
    writeln(2, "connect.rollback()");
    writeln(1, "return rec");
    writeln("endcode");
    writeln("}");
    writeln("");
  }

  static private void generateRest(Database database, Table table, String output) throws Exception
  {
    outLog.println("Code: " + output + table.useName() + ".ii");
    try (OutputStream outFile = new FileOutputStream(output + table.useName() + ".ii"))
    {
      writer = new PrintWriter(outFile);
      indent_size = 4;
      writeln("// This code was generated, do not modify it, modify it at source and regenerate it.");
      writeln("// see " + table.useName() + " source file");
      writeln();
      for (int i = 0; i < table.procs.size(); i++)
      {
        Proc proc = table.procs.elementAt(i);
        if (proc.name.equalsIgnoreCase("insert"))
        {
          restInsert(table);
          continue;
        }
        if (proc.name.equalsIgnoreCase("update"))
        {
          restUpdate(table);
          continue;
        }
        if (proc.name.equalsIgnoreCase("deleteone"))
        {
          restDelete(table);
          continue;
        }
        if (proc.outputs.size() > 0)
        {
          if (proc.isSingle)
          {
            restGetSingle(table, proc);
            continue;
          }
          else
          {
            restGetMultiple(table, proc);
            continue;
          }

        }
        restPosts(table, proc);
      }
      writer.flush();
    }
  }

}
