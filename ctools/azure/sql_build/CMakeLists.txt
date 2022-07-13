set (name azure_sql_build)
project (${name})

function (pathed result ext_dir)
  foreach (arg ${ARGN})
    if (${ARGN} STREQUAL REMOVE)
      file (GLOB remFiles ${ext_dir}/*.*)
      list (LENGTH remFiles count)
      if (0 LESS count)
        #message (STATUS "--info-- Removing all files in ${ext_dir}")
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
  ##message (STATUS "--info-- GLOB ${globs}")
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
  #set (logFiles ${logFiles} PARENT_SCOPE)
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

### set (switchesOld
###  "${msqlPyDirOld}|code.PyDBApiCode|Msql PY Files"
###  "${msqlcDirOld}|code.MSSqlCCode|Msql C Files"
###  "${msqlDirOld}|ddl.MSSqlDDL|Msql SQL Files"
### )

set (sifiles
   #${CMAKE_CURRENT_SOURCE_DIR}/accuitycontact.si
   #${CMAKE_CURRENT_SOURCE_DIR}/accuitycorrespondent.si
   #${CMAKE_CURRENT_SOURCE_DIR}/accuitycorrespondentsub.si
   #${CMAKE_CURRENT_SOURCE_DIR}/accuitylocation.si
   #${CMAKE_CURRENT_SOURCE_DIR}/accuityofficer.si
   #${CMAKE_CURRENT_SOURCE_DIR}/accuityroutingatt.si
   #${CMAKE_CURRENT_SOURCE_DIR}/accuityroutingcode.si
   #
   #${CMAKE_CURRENT_SOURCE_DIR}/accuityoverride.si
   #${CMAKE_CURRENT_SOURCE_DIR}/audits.si

  ${CMAKE_CURRENT_SOURCE_DIR}/comments.si
  ${CMAKE_CURRENT_SOURCE_DIR}/country.si
  ${CMAKE_CURRENT_SOURCE_DIR}/currency.si
  ${CMAKE_CURRENT_SOURCE_DIR}/dates.si
  ${CMAKE_CURRENT_SOURCE_DIR}/domain.si
  ${CMAKE_CURRENT_SOURCE_DIR}/drivers.si
  ${CMAKE_CURRENT_SOURCE_DIR}/fields.si
  ${CMAKE_CURRENT_SOURCE_DIR}/fieldsearch.si
  ${CMAKE_CURRENT_SOURCE_DIR}/fieldsearchdef.si
  ${CMAKE_CURRENT_SOURCE_DIR}/group.si
  ${CMAKE_CURRENT_SOURCE_DIR}/lookup.si
  ${CMAKE_CURRENT_SOURCE_DIR}/message.si
  ${CMAKE_CURRENT_SOURCE_DIR}/metadata.si
  ${CMAKE_CURRENT_SOURCE_DIR}/persistent.si
  ${CMAKE_CURRENT_SOURCE_DIR}/queue.si
  ${CMAKE_CURRENT_SOURCE_DIR}/queuetype.si
  ${CMAKE_CURRENT_SOURCE_DIR}/reply.si
  ${CMAKE_CURRENT_SOURCE_DIR}/response.si
  ${CMAKE_CURRENT_SOURCE_DIR}/routing.si
  ${CMAKE_CURRENT_SOURCE_DIR}/sourcesystem.si
  ${CMAKE_CURRENT_SOURCE_DIR}/staff.si
  ${CMAKE_CURRENT_SOURCE_DIR}/staffconfigname.si
  ${CMAKE_CURRENT_SOURCE_DIR}/staffgroup.si
  ${CMAKE_CURRENT_SOURCE_DIR}/staffprofile.si
  ${CMAKE_CURRENT_SOURCE_DIR}/staffqueueconfig.si
  ${CMAKE_CURRENT_SOURCE_DIR}/staffqueueperm.si
  ${CMAKE_CURRENT_SOURCE_DIR}/streams.si
  ${CMAKE_CURRENT_SOURCE_DIR}/streamtype.si
  ${CMAKE_CURRENT_SOURCE_DIR}/summary.si
)


jportal (${name} "${sifiles}" ${switches})

#set_property(TARGET jportalmsql.gen  PROPERTY FOLDER "mcpe/sql/jportalmsql_gen")
#folder(${name})


#set (name jportalmsql-old.gen)
#project (${name})
#jportal (${name} "${sifiles}" ${switchesOld})

#set_property(TARGET jportalmsql.gen  PROPERTY FOLDER "mcpe/sql/jportalmsql_gen")
#folder(${name})