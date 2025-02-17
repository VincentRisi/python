package configs.azure.vlab.jportal.util;

import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class ConnectorDB2 extends Connector
{
  String userId;

  public ConnectorDB2(String server, String schema, String user, String password)
      throws Throwable
  {
    String url = "jdbc:db2:";
    if (server.length() > 0) url = url + server;
    connect(url, schema, user, password);
  }

  void connect(String url, String schema, String user, String password) throws Throwable
  {
    userId = user;
    Class.forName("COM.ibm.db2.jdbc.app.DB2Driver").newInstance();
    connection = DriverManager.getConnection(url, user, password);
    System.out.println(!connection.isClosed());
    connection.setAutoCommit(false);
    if (schema.length() > 0) {
        PreparedStatement prep = connection.prepareStatement("SET SCHEMA " + schema);
        prep.execute();
    }
  }

  public int getSequence(String table) throws SQLException
  {
    int nextNo;
    PreparedStatement prep = connection.prepareStatement("SELECT NEXTVAL FOR "
        + table + "SEQ from SYSIBM.SYSDUMMY1 WITH UR");
    ResultSet result = prep.executeQuery();
    result.next();
    nextNo = result.getInt(1);
    result.close();
    prep.close();
    return nextNo;
  }

  public long getBigSequence(String table) throws SQLException
  {
    long nextNo;
    PreparedStatement prep = connection.prepareStatement("SELECT NEXTVAL FOR "
        + table + "SEQ from SYSIBM.SYSDUMMY1 WITH UR");
    ResultSet result = prep.executeQuery();
    result.next();
    nextNo = result.getLong(1);
    result.close();
    prep.close();
    return nextNo;
  }

  public int getSequence(String table, String field) throws SQLException
  {
    return getSequence(table);
  }

  public long getBigSequence(String table, String field) throws SQLException
  {
    return getBigSequence(table);
  }

  public String getUserstamp() throws SQLException
  {
    return userId;
  }
  /**
   * returns 4 string array with last element empty string to show a sequence
   */
  public Returning getReturning(String table, String field) throws SQLException
  {
    Returning result = new Returning();
    result.head = "select "+field+" from new table (";
    result.output = "";
    result.sequence = "NEXTVAL FOR " + table + "SEQ,"; 
    result.tail = ")"; 
    result.dropField = "";
    result.doesGeneratedKeys = false;
    return result;
  }
}
