project (audio_sql_build)

set (root ${JTOOLS_DIR})
set (logFile ${CMAKE_CURRENT_BINARY_DIR}/build.log)

file (READ ${root}/audio/inputs.list lines)
separate_arguments(lines)
set (inFiles)
foreach (line ${lines})
  string (REPLACE {root} ${root} newline ${line})
  list (APPEND inFiles ${newline})
endforeach ()
log_info(${inFiles})

# 
# The -F %param and -F %odbc are set as this to make them single usage flags
# The PyDBApiCode generators have specific code to handle this.
# The -R switch is for the {root} substitutions. These switches are very
# much the same as in the IDEA intellij run configs.
# 
set (switches
  "-l ${logFile}"
  "-R ${JTOOLS_DIR}"
  "-f {root}/audio/inputs.list"
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

add_custom_target (audio_sql_build ALL
  DEPENDS ${logFile}
  #SOURCES ${inFiles}
)

set_property(TARGET audio_sql_build  PROPERTY FOLDER "audio/sql_build")
