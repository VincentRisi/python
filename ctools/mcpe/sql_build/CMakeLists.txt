project (mcpe_sql_build)

set (root ${JTOOLS_DIR})
set (logFile ${CMAKE_CURRENT_BINARY_DIR}/build.log)
set (siFiles
  ${root}/src/mcpe/sql/si/accuitycontact.si
  ${root}/src/mcpe/sql/si/accuitycorrespondent.si
  ${root}/src/mcpe/sql/si/accuitylocation.si
  ${root}/src/mcpe/sql/si/accuityofficer.si
  ${root}/src/mcpe/sql/si/accuityroutingatt.si
  ${root}/src/mcpe/sql/si/audits.si
  ${root}/src/mcpe/sql/si/bankaccproc.si
  ${root}/src/mcpe/sql/si/bankcorrespondents.si
  ${root}/src/mcpe/sql/si/bankfile.si
  ${root}/src/mcpe/sql/si/comments.si
  ${root}/src/mcpe/sql/si/country.si
  ${root}/src/mcpe/sql/si/dates.si
  ${root}/src/mcpe/sql/si/exclusions.si
  ${root}/src/mcpe/sql/si/figcorrbankproc.si
  ${root}/src/mcpe/sql/si/finidcorrespondentrouting.si
  ${root}/src/mcpe/sql/si/group.si
  ${root}/src/mcpe/sql/si/lookup.si
  ${root}/src/mcpe/sql/si/message.si
  ${root}/src/mcpe/sql/si/persistent.si
  ${root}/src/mcpe/sql/si/reply.si
  ${root}/src/mcpe/sql/si/response.si
  ${root}/src/mcpe/sql/si/routing.si
  ${root}/src/mcpe/sql/si/scriptprocs.si
  ${root}/src/mcpe/sql/si/scriptsgroup.si
  ${root}/src/mcpe/sql/si/siresscutofftimes.si
  ${root}/src/mcpe/sql/si/siressholidays.si
  ${root}/src/mcpe/sql/si/siressparticipant.si
  ${root}/src/mcpe/sql/si/staff.si
  ${root}/src/mcpe/sql/si/staffgroup.si
  ${root}/src/mcpe/sql/si/streams.si
  ${root}/src/mcpe/sql/si/summary.si
  )
set (inputList ${root}/src/mcpe/inputs.list)
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
  "-o {root}/out/mcpe/sql/ddl/oracle ddl.OracleDDL"
  "-o {root}/out/mcpe/sql/ddl/lite3 ddl.Lite3DDL"
  "-o {root}/out/mcpe/sql/ddl/mssql ddl.MSSqlDDL"
  "-o {root}/out/mcpe/sql/yaml2 code.SwaggerCode"
  "-o {root}/out/mcpe/sql/yaml3 code.OpenApiCode"
  "-o {root}/out/mcpe/sql/py/dbapi/format -F %param=format code.PyDBApiCode"
  "-o {root}/out/mcpe/sql/py/dbapi/named -F %param=named code.PyDBApiCode"
  "-o {root}/out/mcpe/sql/py/dbapi/pyformat -F %param=pyformat code.PyDBApiCode"
  "-o {root}/out/mcpe/sql/py/dbapi/numeric -F %param=numeric code.PyDBApiCode"
  "-o {root}/out/mcpe/sql/py/dbapi/qmark -F %param=qmark code.PyDBApiCode"
  "-o {root}/out/mcpe/sql/clish code.CliCCode"
  "-o {root}/out/mcpe/sql/msssh code.MSSqlCCode"
  "-o {root}/out/mcpe/sql/myssh code.MySqlCCode"
  "-o {root}/out/mcpe/sql/ocish code.OciCCode"
  "-o {root}/out/mcpe/sql/pgsh code.PostgreCCode"
  "-o {root}/out/mcpe/sql/odbc/db2 -F %odbc=db2 code.OdbcCCode"
  "-o {root}/out/mcpe/sql/odbc/mssql -F %odbc=mssql code.OdbcCCode"
  "-o {root}/out/mcpe/sql/odbc/mysql -F %odbc=mysql code.OdbcCCode"
  "-o {root}/out/mcpe/sql/odbc/oracle -F %odbc=oracle code.OdbcCCode"
  "-o {root}/out/mcpe/sql/odbc/postgre -F %odbc=postgre code.OdbcCCode"
  "-o {root}/out/mcpe/sql/ii code.IdlPyCode"
)
separate_arguments(switches)
log_info("java -jar ${jportal_jar} ${switches}")

add_custom_command(
  OUTPUT  ${logFile}
  COMMAND java -jar ${jportal_jar} ${switches}
  DEPENDS ${inFiles}
  VERBATIM
)

add_custom_target (mcpe_sql_build ALL
  DEPENDS ${logFile}
    SOURCES ${siFiles} ${logFile} ${inputList}
)

set_property(TARGET mcpe_sql_build  PROPERTY FOLDER "mcpe/sql_build")
