project (accuity_idl2_build)

set (root ${JTOOLS_DIR})
set (idlFile ${root}/out/idl2/accuity.idl2)
set (imFile  ${root}/src/idl2/accuity.im)

file (READ ${root}/src/ibfiles.list inlines)
set (ibFiles)
foreach (inline ${inlines})
  string (REPLACE {root} ${root} outline ${inline})
  list (APPEND ibFiles ${outline})
endforeach ()

file (READ ${root}/src/iifiles.list inlines)
set (iiFiles)
foreach (inline ${inlines})
  string (REPLACE {root} ${root} outline ${inline})
  list (APPEND iiFiles ${outline})
endforeach ()

# The -R switch is for the {root} substitutions. These switches are very
# much the same as in the IDEA intellij run configs.

set (switches
  "-R ${JTOOLS_DIR}"
  "-B {root}/src/ibfiles.list"
  "-I {root}/src/iifiles.list"
  "-f {root}/out/idl2/accuity.idl2 {root}/src/idl2/accuity.im"
  "-o {root}/out/idl2/http http.PopHTTPImpl http.PopHTTPServer http.PopHTTPOpenApi http.PopHTTPSwagger"
  "-o {root}/out/idl2/http/py http.PopHTTPPython"
  )

separate_arguments(switches)
log_info("java -jar ${crackle_jar} ${switches}")

add_custom_command(
  OUTPUT  ${idlFile}
  COMMAND java -jar ${crackle_jar} ${switches}
  DEPENDS ${imFile} ${ibFiles} ${iiFiles}
  VERBATIM
)

add_custom_target (accuity_idl2_build ALL
  DEPENDS ${idlFile}
  SOURCES ${imFile} ${ibFiles} ${iiFiles} ${idlFile}
)

add_dependencies (accuity_idl2_build accuity_sql_build)
set_property(TARGET accuity_idl2_build PROPERTY FOLDER "accuity/idl2_build")
