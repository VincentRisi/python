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


pathed(msqlcDir  ${CMAKE_CURRENT_BINARY_DIR}/msqlc) 
pathed(msqlDir   ${CMAKE_CURRENT_BINARY_DIR}/mddl) 

pathed(msqlcDirOld   ${CMAKE_CURRENT_BINARY_DIR}/msqlc-old) 
pathed(msqlDirOld   ${CMAKE_CURRENT_BINARY_DIR}/mddl-old) 
pathed(msqlPyDirOld   ${CMAKE_CURRENT_BINARY_DIR}/msqlpy-old) 


set (switches
  "${msqlcDir}|code.MSSqlCCode|Msql C Files"
  "${msqlDir}|ddl.MSSqlDDL|Msql SQL Files"
 )

set (sifiles
/vlab/python/jtools/src/azure/sql/si/comments.si
/vlab/python/jtools/src/azure/sql/si/country.si
/vlab/python/jtools/src/azure/sql/si/currency.si
/vlab/python/jtools/src/azure/sql/si/dates.si
/vlab/python/jtools/src/azure/sql/si/domain.si
/vlab/python/jtools/src/azure/sql/si/drivers.si
/vlab/python/jtools/src/azure/sql/si/fields.si
/vlab/python/jtools/src/azure/sql/si/fieldsearch.si
/vlab/python/jtools/src/azure/sql/si/fieldsearchdef.si
/vlab/python/jtools/src/azure/sql/si/group.si
/vlab/python/jtools/src/azure/sql/si/lookup.si
/vlab/python/jtools/src/azure/sql/si/message.si
/vlab/python/jtools/src/azure/sql/si/metadata.si
/vlab/python/jtools/src/azure/sql/si/persistent.si
/vlab/python/jtools/src/azure/sql/si/queue.si
/vlab/python/jtools/src/azure/sql/si/queuetype.si
/vlab/python/jtools/src/azure/sql/si/reply.si
/vlab/python/jtools/src/azure/sql/si/response.si
/vlab/python/jtools/src/azure/sql/si/routing.si
/vlab/python/jtools/src/azure/sql/si/sourcesystem.si
/vlab/python/jtools/src/azure/sql/si/staff.si
/vlab/python/jtools/src/azure/sql/si/staffconfigname.si
/vlab/python/jtools/src/azure/sql/si/staffgroup.si
/vlab/python/jtools/src/azure/sql/si/staffprofile.si
/vlab/python/jtools/src/azure/sql/si/staffqueueconfig.si
/vlab/python/jtools/src/azure/sql/si/staffqueueperm.si
/vlab/python/jtools/src/azure/sql/si/streams.si
/vlab/python/jtools/src/azure/sql/si/streamtype.si
/vlab/python/jtools/src/azure/sql/si/summary.si
)
#set (inputList /vlab/python/jtools/src/azure/inputs.list)
#file (WRITE ${inputList})
#foreach (file ${sifiles})
#  file (APPEND ${inputList} ${file} "\n")
#endforeach ()

jportal (${name} "${sifiles}" ${switches})
