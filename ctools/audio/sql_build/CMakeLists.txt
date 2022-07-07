project (audio_sql_build)

set (root ${JTOOLS_DIR})
set (logFile ${root}/out/audio/sql/build.log)
set (siFiles
  ${root}/src/audio/sql/si/book.si
  )
set (inputList ${root}/src/audio/inputs.list)
source_group ("SI Files" FILES ${siFiles} ${logFile} ${inputList})
file (WRITE ${inputList})
foreach (file ${siFiles})
  file (APPEND ${inputList} ${file} "\n")
endforeach ()

# 
# The -F %param and -F %odbc are set as this to make them single usage flags
# The PyDBApiCode generators have specific code to handle this.
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
  "-o {root}/out/audio/sql/ddl/oracle ddl.OracleDDL"
  "-o {root}/out/audio/sql/ddl/lite3 ddl.Lite3DDL"
  "-o {root}/out/audio/sql/ddl/mssql ddl.MSSqlDDL"
  "-o {root}/out/audio/sql/yaml2 code.SwaggerCode"
  "-o {root}/out/audio/sql/yaml3 code.OpenApiCode"
  "-o {root}/out/audio/sql/clish code.CliCCode"
  "-o {root}/out/audio/sql/msssh code.MSSqlCCode"
  "-o {root}/out/audio/sql/myssh code.MySqlCCode"
  "-o {root}/out/audio/sql/ocish code.OciCCode"
  "-o {root}/out/audio/sql/pgsh code.PostgreCCode"
  "-o {root}/out/audio/sql/py/dbapi/format -F %param=format code.PyDBApiCode"
  "-o {root}/out/audio/sql/py/dbapi/named -F %param=named code.PyDBApiCode"
  "-o {root}/out/audio/sql/py/dbapi/pyformat -F %param=pyformat code.PyDBApiCode"
  "-o {root}/out/audio/sql/py/dbapi/numeric -F %param=numeric code.PyDBApiCode"
  "-o {root}/out/audio/sql/py/dbapi/qmark -F %param=qmark code.PyDBApiCode"
  "-o {root}/out/audio/sql/py/dbapi/pyodbc -F %param=pyodbc code.PyDBApiCode"
  "-o {root}/out/audio/sql/ii code.IdlPyCode"
)
separate_arguments(switches)
log_info("java -jar ${jportal_jar} ${switches}")

add_custom_command(
  OUTPUT  ${logFile}
  COMMAND java -jar ${jportal_jar} ${switches}
  DEPENDS ${siFiles}
  VERBATIM
)

add_custom_target (audio_sql_build ALL
  DEPENDS ${logFile}
  SOURCES ${siFiles} ${logFile} ${inputList}
)

set_property(TARGET audio_sql_build  PROPERTY FOLDER "audio/sql_build")
