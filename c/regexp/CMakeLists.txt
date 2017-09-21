#
# Run the tutorial by hand
#

cmake_minimum_required(VERSION 2.6)
project(Template)

include_directories("${PROJECT_SOURCE_DIR}")
include_directories("${PROJECT_SOURCE_DIR}/lib")
#set(EXTRA_LIBS json-c)



set (EXTRA_LIBS ${EXTRA_LIBS} ssl)

add_executable(my_prog my_prog.c)
target_link_libraries(my_prog ${EXTRA_LIBS})


