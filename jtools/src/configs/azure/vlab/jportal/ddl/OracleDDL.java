/// ------------------------------------------------------------------
/// Copyright (c) 1996, 2004 Vincent Risi in Association 
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
/// $Date: 2004/10/18 13:45:44 $
/// $Revision: 411.1 $ // YMM.Revision
/// ------------------------------------------------------------------

package configs.azure.vlab.jportal.ddl;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.io.PrintWriter;

import azure.vlab.jportal.*;
import vlab.jportal.*;

public class OracleDDL extends Generator
{
  private static boolean addExit = false;
  private static boolean dropTablespace = false;

  /**
   * Generates the SQL for ORACLE Table creation.
   */
  public static String description()
  {
    return "Generate Oracle DDL";
  }

  public static String documentation()
  {
    return "Generate Oracle DDL.";
  }

  private static void setFlags(Database database, PrintWriter outLog)
  {
    for (int findex = 0; findex < database.flags.size(); findex++)
    {
      String flag = database.flags.elementAt(findex);
      {
        if (flag.equals("addExit") == true)
          addExit = true;
        else if (flag.equals("dropTablespace") == true)
          dropTablespace = true;
      }
    }
    if (addExit == false)
      outLog.println("-- No addExit flag detected.");
  }

  public static void generate(Database database, String output, PrintWriter outLog)
  {
    try
    {
      String tableOwner = "";
      String fileName;
      setFlags(database, outLog);
      if (database.output.length() > 0)
        fileName = database.output;
      else
        fileName = database.name;
      outLog.println("DDL: " + output + fileName + ".sql");
      try (OutputStream outFile = new FileOutputStream(output + fileName + ".sql"))
      {
        Writer.writer = new PrintWriter(outFile);
        if (database.schema.length() > 0)
          tableOwner = database.schema + ".";
        else if (database.userid.length() > 0)
          tableOwner = database.userid + ".";
        if (database.password.length() > 0)
        {
          if (addExit == false)
            outLog.println("-- An exit added because a CONNECT is generated.");
          Writer.writeln("CONNECT " + database.userid + "/" + database.password + "@" + database.server);
          Writer.writeln();
          addExit = true;
        }
        for (int i = 0; i < database.tables.size(); i++)
          generate(database.tables.elementAt(i));
        for (int i = 0; i < database.views.size(); i++)
          generate(database.views.elementAt(i), null, tableOwner);
        for (int i = 0; i < database.sequences.size(); i++)
          generate(database.sequences.elementAt(i), tableOwner);
        if (addExit == true)
        {
          Writer.writeln("exit");
          Writer.writeln();
        }
        Writer.writer.flush();
      }
    }
    catch (IOException e1)
    {
      outLog.println("Generate Oracle SQL IO Error");
    }
  }

  static String bSO(int i)
  {
    String x = "" + (101 + i);
    return x.substring(1);
  }

  static String fixDefaultValue(Field field)
  {
    int len = field.defaultValue.length();
    switch (field.type)
    {
      case Field.DATE:
        if (len == 8)
          return Writer.format("to_date('%s', 'YYYYMMDD')", field.defaultValue);
        return Writer.format("to_date('%s', 'YYYY-MM-DD')", field.defaultValue);
      case Field.DATETIME:
        if (len == 14)
          return Writer.format("to_date('%s', 'YYYYMMDDHH24MISS')", field.defaultValue);
        if (len >= 19)
          return Writer.format("to_date('%s', 'YYYY-MM-DD HH24:MI:SS')", field.defaultValue.substring(0, 19));
        break;
      case Field.TIME:
        if (len == 6)
          return Writer.format("to_date('%s', 'HH24MISS')", field.defaultValue);
        return Writer.format("to_date('%s', 'HH24:MI:SS')", field.defaultValue);
      case Field.TIMESTAMP:
      case Field.AUTOTIMESTAMP:
        return "CURRENT_TIMESTAMP";
      default:
        return field.defaultValue;
    }
    return field.defaultValue;
  }

  static void generate(Table table)
  {
    String tableOwner = "";
    if (table.database.schema.length() > 0)
      tableOwner = table.database.schema + ".";
    else if (table.database.server.length() > 0)
      tableOwner = table.database.server + ".";
    else if (table.database.userid.length() > 0)
      tableOwner = table.database.userid + ".";
    String comma = "( ";
    boolean hasNotNull = false;
    boolean bigSequence = false;
    if (table.fields.size() > 0)
    {
      Writer.writeln("DROP TABLE " + tableOwner + table.fixEscape() + " CASCADE CONSTRAINTS;");
      Writer.writeln();
      Writer.writeln("CREATE TABLE " + tableOwner + table.fixEscape());
      for (int i = 0; i < table.fields.size(); i++, comma = ", ")
      {
        Field field = table.fields.elementAt(i);
        Writer.writeln(comma + field.fixEscape() + " " + varType(field));
        if (field.defaultValue.length() > 0)
          hasNotNull = true;
        if (field.checkValue.length() > 0)
          hasNotNull = true;
        else if (!field.isNull)
          hasNotNull = true;
        if (field.type == Field.BIGSEQUENCE)
          bigSequence = true;
      }
      Writer.write(")");
      if (table.options.size() > 0)
      {
        for (int i = 0; i < table.options.size(); i++)
        {
          String option = table.options.elementAt(i);
          if (option.toUpperCase().startsWith("TABLESPACE") && dropTablespace == false)
          {
            int n = option.toUpperCase().indexOf("INDEX ");
            Writer.writeln();
            if (n > 0)
            {
              Writer.write(option.substring(0, n - 1));
              table.options.addElement(option.substring(n));
            } else
              Writer.write(option);
          }
        }
      }
      Writer.writeln(";");
      Writer.writeln();
      Writer.writeln("DROP PUBLIC SYNONYM " + table.fixEscape() + ";");
      Writer.writeln();
      Writer.writeln("CREATE PUBLIC SYNONYM " + table.fixEscape() + " FOR " + tableOwner + table.fixEscape() + ";");
      Writer.writeln();
      for (int i = 0; i < table.grants.size(); i++)
      {
        Grant grant = table.grants.elementAt(i);
        generate(grant, tableOwner + table.fixEscape());
      }
      if (table.hasSequence)
      {
        Writer.writeln("DROP SEQUENCE " + tableOwner + table.name + "Seq;");
        Writer.writeln();
        Writer.writeln("CREATE SEQUENCE " + tableOwner + table.name + "Seq");
        Writer.writeln("  MINVALUE 1");
        if (bigSequence == true)
          Writer.writeln("  MAXVALUE 999999999999999999");
        else
          Writer.writeln("  MAXVALUE 999999999");
        Writer.writeln("  CYCLE");
        Writer.writeln("  ORDER;");
        Writer.writeln();
        Writer.writeln("DROP PUBLIC SYNONYM " + table.name + "SEQ;");
        Writer.writeln();
        Writer.writeln("CREATE PUBLIC SYNONYM " + table.name + "SEQ FOR " + tableOwner + table.name + "SEQ;");
        Writer.writeln();
        if (table.grants.size() > 0)
        {
          Grant grant = table.grants.elementAt(0);
          for (int j = 0; j < grant.users.size(); j++)
          {
            String user = grant.users.elementAt(j);
            Writer.writeln("GRANT SELECT ON " + tableOwner + table.name + "SEQ TO " + user + ";");
            Writer.writeln();
          }
        }
      }
      for (int i = 0; i < table.keys.size(); i++)
      {
        Key key = table.keys.elementAt(i);
        if (!key.isPrimary && !key.isUnique)
          generateIndex(table, key);
      }
    }
    for (int i = 0; i < table.views.size(); i++)
    {
      View view = table.views.elementAt(i);
      generate(view, table, tableOwner);
    }
    if (hasNotNull == true)
    {
      Writer.writeln("ALTER TABLE " + tableOwner + table.name);
      Writer.writeln("MODIFY");
      comma = "( ";
      for (int i = 0; i < table.fields.size(); i++, comma = ", ")
      {
        Field field = table.fields.elementAt(i);
        if (field.isNull && field.defaultValue.length() == 0 && field.checkValue.length() == 0)
          continue;
        if (field.defaultValue.length() > 0)
        {
          Writer.writeln(Writer.format("%s%s DEFAULT %s", comma, field.fixEscape(), fixDefaultValue(field)));
          continue;
        }
        Writer.write(comma + field.fixEscape() + " CONSTRAINT " + table.name + "_NN" + bSO(i));
        if (field.checkValue.length() > 0)
          Writer.write(" CHECK (" + field.checkValue + ")");
        else
          Writer.write(" NOT NULL");
        Writer.writeln();
      }
      Writer.writeln(");");
      Writer.writeln();
    }
    if (table.keys.size() > 0)
    {
      String mComma = "( ";
      Writer.writeln("ALTER TABLE " + tableOwner + table.name);
      Writer.writeln("ADD");
      for (int i = 0; i < table.keys.size(); i++)
      {
        Key key = table.keys.elementAt(i);
        if (key.isPrimary)
          generatePrimary(table, key, mComma);
        else if (key.isUnique)
          generateUnique(table, key, mComma);
        mComma = ", ";
      }
      Writer.writeln(");");
      Writer.writeln();
    }
    if (table.links.size() > 0)
    {
      String mComma = "( ";
      Writer.writeln("ALTER TABLE " + tableOwner + table.name);
      Writer.writeln("ADD");
      for (int i = 0; i < table.links.size(); i++)
      {
        Link link = table.links.elementAt(i);
        if (link.linkName.length() == 0)
          link.linkName = table.name + "_FK" + bSO(i);
        generate(link, mComma);
        mComma = ", ";
      }
      Writer.writeln(");");
      Writer.writeln();
    }
    for (int i = 0; i < table.procs.size(); i++)
    {
      Proc proc = table.procs.elementAt(i);
      if (proc.isData)
        generate(proc);
    }
  }

  /**
   * Generates SQL code for ORACLE Primary Key create
   */
  static void generatePrimary(Table table, Key key, String mcomma)
  {
    String comma = "  ( ";
    String keyname = key.name.toUpperCase();
    if (!keyname.contains(table.name.toUpperCase()))
      keyname = table.name.toUpperCase() + "_" + keyname;
    Writer.writeln(mcomma + "CONSTRAINT " + keyname + " PRIMARY KEY");
    for (int i = 0; i < key.fields.size(); i++, comma = "  , ")
    {
      String name = key.fields.elementAt(i);
      Writer.writeln(comma + name);
    }
    Writer.writeln("  )");
    for (int i = 0; i < key.options.size(); i++)
    {
      String option = key.options.elementAt(i);
      if (option.toUpperCase().startsWith("INDEX IN"))
      {
        Writer.write("TABLESPACE " + option.substring(9));
        break;
      }
    }
  }

  /**
   * Generates SQL code for ORACLE Unique Key create
   */
  static void generateUnique(Table table, Key key, String mcomma)
  {
    String comma = "  ( ";
    String keyname = key.name.toUpperCase();
    if (!keyname.contains(table.name.toUpperCase()))
      keyname = table.name.toUpperCase() + "_" + keyname;
    Writer.writeln(mcomma + "CONSTRAINT " + keyname + " UNIQUE");
    for (int i = 0; i < key.fields.size(); i++, comma = "  , ")
    {
      String name = key.fields.elementAt(i);
      Writer.writeln(comma + name);
    }
    Writer.writeln("  )");
    for (int i = 0; i < key.options.size(); i++)
    {
      String option = key.options.elementAt(i);
      if (option.toUpperCase().startsWith("INDEX IN"))
      {
        Writer.write("TABLESPACE " + option.substring(9));
        break;
      }
    }
  }

  /**
   * Generates SQL code for ORACLE Index create
   */
  static void generateIndex(Table table, Key key)
  {
    String tableOwner = "";
    if (table.database.userid.length() > 0)
      tableOwner = table.database.userid + ".";
    String comma = "( ";
    String keyname = key.name.toUpperCase();
    if (!keyname.contains(table.name.toUpperCase()))
      keyname = table.name.toUpperCase() + "_" + keyname;
    Writer.writeln("DROP INDEX " + keyname + ";");
    Writer.writeln("");
    Writer.writeln("CREATE INDEX " + keyname + " ON " + tableOwner + table.name);
    for (int i = 0; i < key.fields.size(); i++, comma = ", ")
    {
      String name = key.fields.elementAt(i);
      Writer.writeln(comma + name);
    }
    Writer.write(")");
    for (int i = 0; i < key.options.size(); i++)
    {
      Writer.writeln();
      String option = key.options.elementAt(i);
      if (option.toUpperCase().startsWith("INDEX IN"))
      {
        Writer.write("TABLESPACE " + option.substring(9));
        break;
      }
    }
    Writer.writeln(";");
    Writer.writeln();
  }

  /**
   * Generates foreign key SQL Code for Oracle
   */
  static void generate(Link link, String mComma)
  {
    String comma = "  ( ";
    Writer.writeln(mComma + "CONSTRAINT " + link.linkName + " FOREIGN KEY");
    for (int i = 0; i < link.fields.size(); i++, comma = "  , ")
    {
      String name = link.fields.elementAt(i);
      Writer.writeln(comma + name);
    }
    Writer.writeln("  ) REFERENCES " + link.name);
    if (link.linkFields.size() > 0)
    {
      comma = "(";
      for (int i = 0; i < link.linkFields.size(); i++)
      {
        String name = link.linkFields.elementAt(i);
        Writer.write(comma + name);
        comma = ", ";
      }
      Writer.write(")");
    }
    if (link.isDeleteCascade)
      Writer.write(" ON DELETE CASCADE");
    //writeln(";");
    Writer.writeln();
  }

  /**
   * Generates grants for Oracle
   */
  static void generate(Grant grant, String object)
  {
    for (int i = 0; i < grant.perms.size(); i++)
    {
      String perm = grant.perms.elementAt(i);
      for (int j = 0; j < grant.users.size(); j++)
      {
        String user = grant.users.elementAt(j);
        Writer.writeln("GRANT " + perm + " ON " + object + " TO " + user + ";");
        Writer.writeln();
      }
    }
  }

  /**
   * Generates views for Oracle
   */
  static void generate(View view, Table table, String tableOwner)
  {
    String viewName = view.name;
    if (table != null)
      viewName = table.useExtra(view.name);
    Writer.writeln("CREATE OR REPLACE FORCE VIEW " + viewName);
    String comma = "( ";
    for (int i = 0; i < view.aliases.size(); i++)
    {
      String alias = (String) view.aliases.elementAt(i);
      Writer.writeln(comma + alias);
      comma = ", ";
    }
    Writer.writeln(") AS");
    Writer.writeln("(");
    for (int i = 0; i < view.lines.size(); i++)
    {
      String line = (String) view.lines.elementAt(i);
      Writer.writeln(line);
    }
    Writer.writeln(");");
    Writer.writeln();
    for (int i = 0; i < view.users.size(); i++)
    {
      String user = (String) view.users.elementAt(i);
      Writer.writeln("GRANT SELECT ON " + viewName + " TO " + user + ";");
    }
    Writer.writeln();
    Writer.writeln("DROP PUBLIC SYNONYM " + viewName + ";");
    Writer.writeln();
    Writer.writeln("CREATE PUBLIC SYNONYM " + viewName + " FOR " + tableOwner + viewName + ";");
    Writer.writeln();
  }

  /**
   * Generates pass through data for Oracle
   */
  static void generate(Proc proc)
  {
    for (int i = 0; i < proc.lines.size(); i++)
    {
      Line l = proc.lines.elementAt(i);
      Writer.writeln(l.line);
    }
    Writer.writeln();
  }

  /**
   * Generates pass through data for Oracle
   */
  static void generate(Sequence sequence, String tableOwner)
  {
    Writer.writeln("DROP SEQUENCE " + sequence.name + ";");
    Writer.writeln();
    Writer.writeln("CREATE SEQUENCE " + sequence.name);
    Writer.writeln("  MINVALUE  " + sequence.minValue);
    Writer.writeln("  MAXVALUE  " + sequence.maxValue);
    Writer.writeln("  INCREMENT BY " + sequence.increment);
    if (sequence.cycleFlag)
      Writer.writeln("  CYCLE");
    if (sequence.orderFlag)
      Writer.writeln("  ORDER");
    Writer.writeln("  START WITH " + sequence.startWith + ";");
    Writer.writeln();
    Writer.writeln("DROP PUBLIC SYNONYM " + sequence.name + ";");
    Writer.writeln();
    Writer.writeln("CREATE PUBLIC SYNONYM " + sequence.name + " FOR " + tableOwner + sequence.name + ";");
    Writer.writeln();
  }

  /**
   * Translates field type to Oracle SQL column types
   */
  static String varType(Field field)
  {
    switch (field.type)
    {
      case Field.BYTE:
        return "NUMBER(3)";
      case Field.SHORT:
        return "NUMBER(5)";
      case Field.INT:
      case Field.SEQUENCE:
        return "NUMBER(10)";
      case Field.LONG:
      case Field.BIGSEQUENCE:
        return "NUMBER(18)";
      case Field.CHAR:
      case Field.USERSTAMP:
        return "VARCHAR2(" + field.length + ")";
      case Field.ANSICHAR:
        return "CHAR(" + field.length + ")";
      case Field.UTF8:
        return Writer.format("NVARCHAR2(%d)", (field.length) * 6);
      case Field.DATE:
      case Field.DATETIME:
      case Field.TIME:
      case Field.TIMESTAMP:
        return "DATE";
      case Field.FLOAT:
      case Field.DOUBLE:
        if (field.scale != 0)
          return "NUMBER(" + field.precision + ", " + field.scale + ")";
        else if (field.precision != 0)
          return "NUMBER(" + field.precision + ")";
        return "NUMBER";
      case Field.BLOB:
        return "BLOB";
      case Field.TLOB:
        return "CLOB";
      case Field.IMAGE:
        return "LONG RAW";
      case Field.UNICODE:
        return Writer.format("NVARCHAR2(%d)", (field.length + 1) * 4);
      case Field.MONEY:
        return "NUMBER(15,2)";
      case Field.IDENTITY:
        return "<not supported>";
      case Field.XML:
      case Field.BIGXML:
        return "XMLTYPE";
      default:
        return "<not yet supported>";
    }
  }
}
