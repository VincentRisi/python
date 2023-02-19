project (cpp_aax_utilities)

add_executable(main_props main_props.cpp)
set_property(TARGET main_props PROPERTY FOLDER "audio/cpp_aax/main_props")

add_executable(main_tags main_tags.cpp)
set_property(TARGET main_tags PROPERTY FOLDER "audio/cpp_aax/main_tags")

add_executable(main_times main_times.cpp)
set_property(TARGET main_times PROPERTY FOLDER "audio/cpp_aax/main_times")