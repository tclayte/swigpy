# adapted from http://www.swig.org/Doc3.0/Introduction.html#Introduction_build_system
cmake_minimum_required(VERSION 3.16)

# set the project name
project(HelloWorld)

FIND_PACKAGE(SWIG REQUIRED)
INCLUDE(${SWIG_USE_FILE})

FIND_PACKAGE(PythonLibs)
INCLUDE_DIRECTORIES(${PYTHON_INCLUDE_PATH})
message(${PYTHON_INCLUDE_PATH})

INCLUDE_DIRECTORIES(${CMAKE_CURRENT_SOURCE_DIR})
INCLUDE_DIRECTORIES(${CMAKE_CURRENT_SOURCE_DIR}/src)

SET(CMAKE_SWIG_FLAGS "")

ADD_SUBDIRECTORY("src")

SET(CMAKE_INSTALL_PREFIX "../install")
FILE(TOUCH build/src/__init__.py)
INSTALL(FILES "build/src/greet.py" DESTINATION lib)
INSTALL(FILES "build/src/_greet.so" DESTINATION lib)
INSTALL(FILES "build/src/__init__.py" DESTINATION lib)

