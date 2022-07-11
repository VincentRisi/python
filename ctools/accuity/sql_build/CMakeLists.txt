project (accuity_sql_build)

set (root ${JTOOLS_DIR})
set (logFile ${CMAKE_CURRENT_BINARY_DIR}/build.log)
set (siFiles
  ${root}/src/accuity/sql/si/accuitycontact.si
  ${root}/src/accuity/sql/si/accuitycorrespondent.si
  ${root}/src/accuity/sql/si/accuitycorrespondentsub.si
  ${root}/src/accuity/sql/si/accuitylocation.si
  ${root}/src/accuity/sql/si/accuityofficer.si
  ${root}/src/accuity/sql/si/accuityroutingatt.si
  ${root}/src/accuity/sql/si/accuityroutingcode.si
  ${root}/src/accuity/sql/si/accuityuseroverride.si
  ${root}/src/accuity/sql/si/audits.si
  ${root}/src/accuity/sql/si/bankfile.si  
  )
set (inputList ${root}/src/accuity/inputs.list)
source_group ("SI Files" FILES ${siFiles} ${logFile} ${inputList})
file (WRITE ${inputList})
foreach (file ${siFiles})
  file (APPEND ${inputList} ${file} "\n")
endforeach ()

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
  "-o {root}/out/accuity/sql/ddl/db2 ddl.Db2DDL"
  "-o {root}/out/accuity/sql/ddl/lite3 ddl.Lite3DDL"
  "-o {root}/out/accuity/sql/ddl/mssql -F %mssql=sequence ddl.MSSqlDDL"
  "-o {root}/out/accuity/sql/ddl/mysql ddl.MySqlDDL"
  "-o {root}/out/accuity/sql/ddl/oracle ddl.OracleDDL"
  "-o {root}/out/accuity/sql/ddl/postgre ddl.PostgreDDL"
  "-o {root}/out/accuity/sql/yaml2 code.SwaggerCode"
  "-o {root}/out/accuity/sql/yaml3 code.OpenApiCode"
  "-o {root}/out/accuity/sql/py/dbapi code.PyDBRestCode"
  "-o {root}/out/accuity/sql/py/dbapi code.PyDBOldCode"
  "-o {root}/out/accuity/sql/py/dbapi/db2 -F %vendor=db2 code.PyDBApiCode"
  "-o {root}/out/accuity/sql/py/dbapi/lite3 -F %vendor=lite3 code.PyDBApiCode"
  "-o {root}/out/accuity/sql/py/dbapi/mssql -F %vendor=mssql code.PyDBApiCode"
  "-o {root}/out/accuity/sql/py/dbapi/mysql -F %vendor=mysql code.PyDBApiCode"
  "-o {root}/out/accuity/sql/py/dbapi/odbc -F %vendor=odbc code.PyDBApiCode"
  "-o {root}/out/accuity/sql/py/dbapi/oracle -F %vendor=oracle code.PyDBApiCode"
  "-o {root}/out/accuity/sql/py/dbapi/postgre -F %vendor=postgre code.PyDBApiCode"
  "-o {root}/out/accuity/sql/clish code.CliCCode"
  "-o {root}/out/accuity/sql/msssh -F %mssql=sequence code.MSSqlCCode"
  "-o {root}/out/accuity/sql/myssh code.MySqlCCode"
  "-o {root}/out/accuity/sql/ocish code.OciCCode"
  "-o {root}/out/accuity/sql/pgsh code.PostgreCCode"
  "-o {root}/out/accuity/sql/odbc/db2 -F %odbc=db2 code.OdbcCCode"
  "-o {root}/out/accuity/sql/odbc/mssql -F %odbc=mssql code.OdbcCCode"
  "-o {root}/out/accuity/sql/odbc/mysql -F %odbc=mysql code.OdbcCCode"
  "-o {root}/out/accuity/sql/odbc/oracle -F %odbc=oracle code.OdbcCCode"
  "-o {root}/out/accuity/sql/odbc/postgre -F %odbc=postgre code.OdbcCCode"
  "-o {root}/out/accuity/sql/ii code.IdlPyCode"
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
    SOURCES ${siFiles} ${logFile} ${inputList}
)

set_property(TARGET accuity_sql_build  PROPERTY FOLDER "accuity/sql_build")
