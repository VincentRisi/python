set (name azure_sql_build)
project (${name})

function (pathed result ext_dir)
  foreach (arg ${ARGN})
    if (${ARGN} STREQUAL REMOVE)
      file (GLOB remFiles ${ext_dir}/*.*)
      list (LENGTH remFiles count)
      if (0 LESS count)
 
         file (REMOVE ${remFiles})
      endif ()
    endif ()
  endforeach ()
  file(MAKE_DIRECTORY ${ext_dir})
  set ("${result}" ${ext_dir} PARENT_SCOPE)
endfunction ()

function (file_glob dir)
  file (GLOB globs 
    ${dir}/*.bas 
    ${dir}/*.cls 
    ${dir}/*.cpp 
    ${dir}/*.cs 
    ${dir}/*.def 
    ${dir}/*.h 
    ${dir}/*.idl 
    ${dir}/*.idl2 
    ${dir}/*.py 
    ${dir}/*.pty 
    ${dir}/*.sh 
    ${dir}/*.txt 
    ${dir}/*.sql
    ${dir}/*.yaml
    ${dir}/*.json
    )

  set (files ${globs} PARENT_SCOPE)
endfunction()

function (idl_split target_args)
  list (LENGTH target_args count)
  if (2 LESS count)
    list (GET target_args 2 arg)
    set (title ${arg})
  endif ()
  if (1 LESS count)
    list (GET target_args 0 arg)
    set (targetdir ${arg})
    list (GET target_args 1 arg)
    set (targetgen ${arg})
  endif ()
  set (groups PARENT_SCOPE)
  if (1 EQUAL count)
    set (switch ${target_args} PARENT_SCOPE)
  elseif (2 EQUAL count)
    set (switch "-o;${targetdir};${targetgen}" PARENT_SCOPE)
  elseif (3 EQUAL count)
    set (switch "-o;${targetdir};${targetgen}" PARENT_SCOPE)
    set (groups "${title};${targetdir}" PARENT_SCOPE)
  endif ()
endfunction ()

function (jportal projectName siFiles)
  source_group ("SI Files"  REGULAR_EXPRESSION ".*[.]si$")
  set (logFiles)
  set (switches)
  set (allFiles)
  foreach (arg ${ARGN})
    string(REPLACE "|" ";" arg2 ${arg})
    idl_split("${arg2}")
    if (1 EQUAL noOf)
      list(APPEND switches "${switch}")
    else ()    
      list(APPEND switches "${switch}")
    endif ()
    list (LENGTH groups noOf)
    if (1 LESS noOf)
      list (GET groups 0 title)
      list (GET groups 1 dir)
      set (files)
      file_glob (${dir})
      source_group (${title} FILES ${files})
      list (APPEND allFiles ${files})
    endif ()  
  endforeach ()
  set (jportalJar ${TOOLS_DIR}/anydb/jportal.jar)
  foreach (siFile ${siFiles})
    get_filename_component (temp ${siFile} NAME)
    string (TOLOWER ${temp} temp1)
    get_filename_component (filename ${temp1} NAME_WE)
    set (logFile ${CMAKE_CURRENT_BINARY_DIR}/${filename}.log)
    list (APPEND logFiles ${logFile})
    add_custom_command (
      OUTPUT  ${logFile}
      COMMAND java -jar ${jportal_jar} ${siFile} -l ${logFile} ${switches}
      DEPENDS ${siFile}
      VERBATIM
    )
  endforeach ()
  source_group (LogFiles FILES ${logFiles})
   
  add_custom_target (${projectName} ALL
    DEPENDS ${logFiles}
    SOURCES ${siFiles} ${allFiles} ${logFiles}
  )
endfunction()

pathed(SQL_MSSSH  ${JTOOLS_DIR}/out/azure/sql/msssh) 
pathed(DDL_MSSQL  ${JTOOLS_DIR}/out/azure/ddl/mssql)
pathed(SQL_DBAPI  ${JTOOLS_DIR}/out/azure/sql/py/dbapi) 
pathed(SQL_PYMSSQL  ${JTOOLS_DIR}/out/azure/sql/py/dbapi/mssql)
pathed(SQL_PYODBC   ${JTOOLS_DIR}/out/azure/sql/py/dbapi/odbc)

set (switches
  "${SQL_MSSSH}|code.MSSqlCCode|Msql C Files"
  "${DDL_MSSQL}|ddl.MSSqlDDL|Msql SQL Files"
  "${SQL_DBAPI}|code.PyDBOldCode|DBOld PY Files"
  "${SQL_PYMSSQL}|code.MSSqlPyCode|MSSql PY Files"
  "${SQL_PYODBC}|code.OdbcPyCode|Odbc PY Files"
 )

set (sifiles
${JTOOLS_DIR}/src/azure/sql/si/comments.si
${JTOOLS_DIR}/src/azure/sql/si/country.si
${JTOOLS_DIR}/src/azure/sql/si/currency.si
${JTOOLS_DIR}/src/azure/sql/si/dates.si
${JTOOLS_DIR}/src/azure/sql/si/domain.si
${JTOOLS_DIR}/src/azure/sql/si/drivers.si
${JTOOLS_DIR}/src/azure/sql/si/fields.si
${JTOOLS_DIR}/src/azure/sql/si/fieldsearch.si
${JTOOLS_DIR}/src/azure/sql/si/fieldsearchdef.si
${JTOOLS_DIR}/src/azure/sql/si/group.si
${JTOOLS_DIR}/src/azure/sql/si/lookup.si
${JTOOLS_DIR}/src/azure/sql/si/message.si
${JTOOLS_DIR}/src/azure/sql/si/metadata.si
${JTOOLS_DIR}/src/azure/sql/si/persistent.si
${JTOOLS_DIR}/src/azure/sql/si/queue.si
${JTOOLS_DIR}/src/azure/sql/si/queuetype.si
${JTOOLS_DIR}/src/azure/sql/si/reply.si
${JTOOLS_DIR}/src/azure/sql/si/response.si
${JTOOLS_DIR}/src/azure/sql/si/routing.si
${JTOOLS_DIR}/src/azure/sql/si/sourcesystem.si
${JTOOLS_DIR}/src/azure/sql/si/staff.si
${JTOOLS_DIR}/src/azure/sql/si/staffconfigname.si
${JTOOLS_DIR}/src/azure/sql/si/staffgroup.si
${JTOOLS_DIR}/src/azure/sql/si/staffprofile.si
${JTOOLS_DIR}/src/azure/sql/si/staffqueueconfig.si
${JTOOLS_DIR}/src/azure/sql/si/staffqueueperm.si
${JTOOLS_DIR}/src/azure/sql/si/streams.si
${JTOOLS_DIR}/src/azure/sql/si/streamtype.si
${JTOOLS_DIR}/src/azure/sql/si/summary.si
)

jportal (${name} "${sifiles}" ${switches})

file (GLOB CPP_MSSSH ${SQL_MSSSH}/*.*)

message (status "${SQL_MSSSH}")
message (status "${CPP_MSSSH}")

add_subdirectory (check_sh)
