project (gps_sql_build)

set (root ${JTOOLS_DIR})
set (logFile ${CMAKE_CURRENT_BINARY_DIR}/build.log)
set (siFiles
  ${root}/src/gps/sql/si/drivers.si
  ${root}/src/gps/sql/si/lookup.si
  ${root}/src/gps/sql/si/message.si
  ${root}/src/gps/sql/si/queue.si
  ${root}/src/gps/sql/si/queuetype.si
  ${root}/src/gps/sql/si/sourcesystem.si
  ${root}/src/gps/sql/si/streams.si
  ${root}/src/gps/sql/si/streamtype.si
  )
set (inputList ${root}/src/gps/inputs.list)
source_group ("SI Files" FILES ${siFiles} ${logFile} ${inputList})
file (WRITE ${inputList})
foreach (file ${siFiles})
  file (APPEND ${inputList} ${file} "\n")
endforeach ()
log_info ("XXXXXXXXXXX" ${inputList})
log_info ("XXXXXXXXXXX" ${logFile})

# 
# The -F %param and -F %odbc are set as this to make them single usage flags
# The PyDBApiCode and OdbcCode generators have specific code to handle this.
# The -R switch is for the {root} substitutions. These switches are very
# much the same as in the IDEA intellij run configs.
# 
set (switches
  "-l ${logFile}"
  "-R ${JTOOLS_DIR}"
  "-f ${inputList}"
  # the switches above are parsed first and the compile is done 
  # the switches below are parsed after the compile and are processed for each input
  # in order -o dir
  #          -f set flag 
  #          -l would change logging
  #          generator
  "-o {root}/out/gps/sql/ddl/oracle ddl.OracleDDL"
  "-o {root}/out/gps/sql/ddl/lite3 ddl.Lite3DDL"
  "-o {root}/out/gps/sql/ddl/mssql ddl.MSSqlDDL"
  "-o {root}/out/gps/sql/yaml2 code.SwaggerCode"
  "-o {root}/out/gps/sql/yaml3 code.OpenApiCode"
  "-o {root}/out/gps/sql/py/dbapi/format -F %param=format code.PyDBApiCode"
  "-o {root}/out/gps/sql/py/dbapi/named -F %param=named code.PyDBApiCode"
  "-o {root}/out/gps/sql/py/dbapi/pyformat -F %param=pyformat code.PyDBApiCode"
  "-o {root}/out/gps/sql/py/dbapi/numeric -F %param=numeric code.PyDBApiCode"
  "-o {root}/out/gps/sql/py/dbapi/qmark -F %param=qmark code.PyDBApiCode"
  "-o {root}/out/gps/sql/clish code.CliCCode"
  "-o {root}/out/gps/sql/msssh code.MSSqlCCode"
  "-o {root}/out/gps/sql/myssh code.MySqlCCode"
  "-o {root}/out/gps/sql/ocish code.OciCCode"
  "-o {root}/out/gps/sql/pgsh code.PostgreCCode"
  "-o {root}/out/gps/sql/odbc/db2 -F %odbc=db2 code.OdbcCCode"
  "-o {root}/out/gps/sql/odbc/mssql -F %odbc=mssql code.OdbcCCode"
  "-o {root}/out/gps/sql/odbc/mysql -F %odbc=mysql code.OdbcCCode"
  "-o {root}/out/gps/sql/odbc/oracle -F %odbc=oracle code.OdbcCCode"
  "-o {root}/out/gps/sql/odbc/postgre -F %odbc=postgre code.OdbcCCode"
  "-o {root}/out/gps/sql/ii code.IdlPyCode"
)
separate_arguments(switches)
log_info("java -jar ${jportal_jar} ${switches}")

add_custom_command(
  OUTPUT  ${logFile}
  COMMAND java -jar ${jportal_jar} ${switches}
  DEPENDS ${inFiles}
  VERBATIM
)

add_custom_target (gps_sql_build ALL
  DEPENDS ${logFile}
    SOURCES ${siFiles} ${logFile} ${inputList}
)

set_property(TARGET gps_sql_build  PROPERTY FOLDER "gps/sql_build")
