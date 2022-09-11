set (projects 
  "audio_db2|3847297c-3414-404e-9444-c5e879ec6c9c"
  "audio_lite3|bece4684-1c05-4a18-9bc5-04a409d7239d"
  "audio_mssql|8edc08ba-9ee2-4c29-8740-4858d1d30545"
  "audio_mysql|e2c32c35-5b27-49f9-b5b5-215ac6b477f6"
  "audio_odbc|f727770c-efe6-4aba-828b-572ef7431a34"
  "audio_oracle|fb641629-6f4b-447e-96fe-c1fceb8ea38a"
  "audio_postgre|469ad583-bfb3-43ba-a52b-683052f3a0f9"
  "azure_odbc|2f9ded4b-0f0a-402f-aa11-d9868835cf94"
  "azure_mssql|2f9ded4b-0f0a-402f-aa00-d9868835cf94"
  )

set (PYPROJ_DIR ${CMAKE_SOURCE_DIR}/ctools/audio/pyproj)
foreach (proj ${projects})
  string (REPLACE "|" ";" proj ${proj})
  list (LENGTH proj count)
  if (2 EQUAL count)
    list (GET proj 0 name)
    list (GET proj 1 uuid)
    include_external_msproject (${name} ${PYPROJ_DIR}/${name}.pyproj
      TYPE "${uuid}"
      PLATFORM "Any CPU"
      )
    set_property(TARGET ${name}  PROPERTY FOLDER "audio/pyproj/${name}")
  endif ()
endforeach ()