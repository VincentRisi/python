project (accuity_sql_build)

set (root ${JTOOLS_DIR})
set (logFile ${CMAKE_CURRENT_BINARY_DIR}/build.log)

file (READ ${root}/src/inputs.list lines)
separate_arguments(lines)
set (inFiles)
foreach (line ${lines})
  string (REPLACE {root} ${root} newline ${line})
  list (APPEND inFiles ${newline})
endforeach ()
log_info(${inFiles})

# 
# The -F %param and -F %odbc are set as this to make them single usage flags
# The PyDBApiCode and OdbcCode generators have specific code to handle this.
# The -R switch is for the {root} substitutions. These switches are very
# much the same as in the IDEA intellij run configs.
# 
set (switches
  "-l ${logFile}"
  "-R ${JTOOLS_DIR}"
  "-f {root}/src/inputs.list"
  "-o {root}/out/sql/ddl/oracle ddl.OracleDDL"
  "-o {root}/out/sql/yaml2 code.SwaggerCode"
  "-o {root}/out/sql/yaml3 code.OpenApiCode"
  "-o {root}/out/sql/py/dbapi/format"
  "-F %param=format code.PyDBApiCode"
  "-o {root}/out/sql/py/dbapi/named"
  "-F %param=named code.PyDBApiCode"
  "-o {root}/out/sql/py/dbapi/pyformat"
  "-F %param=pyformat code.PyDBApiCode"
  "-o {root}/out/sql/py/dbapi/numeric"
  "-F %param=numeric code.PyDBApiCode"
  "-o {root}/out/sql/py/dbapi/qmark"
  "-F %param=qmark code.PyDBApiCode"
  "-o {root}/out/sql/clish code.CliCCode"
  "-o {root}/out/sql/msssh code.MSSqlCCode"
  "-o {root}/out/sql/myssh code.MySqlCCode"
  "-o {root}/out/sql/ocish code.OciCCode"
  "-o {root}/out/sql/pgsh code.PostgreCCode"
  "-o {root}/out/sql/odbc/db2"
  "-F %odbc=db2 code.OdbcCCode"
  "-o {root}/out/sql/odbc/mssql"
  "-F %odbc=mssql code.OdbcCCode"
  "-o {root}/out/sql/odbc/mysql"
  "-F %odbc=mysql code.OdbcCCode"
  "-o {root}/out/sql/odbc/oracle"
  "-F %odbc=oracle code.OdbcCCode"
  "-o {root}/out/sql/odbc/postgre"
  "-F %odbc=postgre code.OdbcCCode"
  "-o {root}/out/sql/ii code.IdlPyCode"
)
separate_arguments(switches)
log_info("java -jar ${jportal_jar} ${switches}")

add_custom_command(
  OUTPUT  ${logFile}
  COMMAND java -jar ${jportal_jar} ${switches}
  DEPENDS ${inFiles}
  VERBATIM
)

add_custom_target (accuity_sql_build ALL
  DEPENDS ${logFile}
  #SOURCES ${inFiles}
)

set_property(TARGET accuity_sql_build  PROPERTY FOLDER "accuity/sql_build")
