# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/lucas/catkin_ws/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/lucas/catkin_ws/build

# Utility rule file for run_tests_mavros_gtest_libmavros-sensor-orientation-test.

# Include the progress variables for this target.
include mavros/mavros/CMakeFiles/run_tests_mavros_gtest_libmavros-sensor-orientation-test.dir/progress.make

mavros/mavros/CMakeFiles/run_tests_mavros_gtest_libmavros-sensor-orientation-test:
	cd /home/lucas/catkin_ws/build/mavros/mavros && ../../catkin_generated/env_cached.sh /usr/bin/python /opt/ros/lunar/share/catkin/cmake/test/run_tests.py /home/lucas/catkin_ws/build/test_results/mavros/gtest-libmavros-sensor-orientation-test.xml "/home/lucas/catkin_ws/devel/lib/mavros/libmavros-sensor-orientation-test --gtest_output=xml:/home/lucas/catkin_ws/build/test_results/mavros/gtest-libmavros-sensor-orientation-test.xml"

run_tests_mavros_gtest_libmavros-sensor-orientation-test: mavros/mavros/CMakeFiles/run_tests_mavros_gtest_libmavros-sensor-orientation-test
run_tests_mavros_gtest_libmavros-sensor-orientation-test: mavros/mavros/CMakeFiles/run_tests_mavros_gtest_libmavros-sensor-orientation-test.dir/build.make

.PHONY : run_tests_mavros_gtest_libmavros-sensor-orientation-test

# Rule to build all files generated by this target.
mavros/mavros/CMakeFiles/run_tests_mavros_gtest_libmavros-sensor-orientation-test.dir/build: run_tests_mavros_gtest_libmavros-sensor-orientation-test

.PHONY : mavros/mavros/CMakeFiles/run_tests_mavros_gtest_libmavros-sensor-orientation-test.dir/build

mavros/mavros/CMakeFiles/run_tests_mavros_gtest_libmavros-sensor-orientation-test.dir/clean:
	cd /home/lucas/catkin_ws/build/mavros/mavros && $(CMAKE_COMMAND) -P CMakeFiles/run_tests_mavros_gtest_libmavros-sensor-orientation-test.dir/cmake_clean.cmake
.PHONY : mavros/mavros/CMakeFiles/run_tests_mavros_gtest_libmavros-sensor-orientation-test.dir/clean

mavros/mavros/CMakeFiles/run_tests_mavros_gtest_libmavros-sensor-orientation-test.dir/depend:
	cd /home/lucas/catkin_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/lucas/catkin_ws/src /home/lucas/catkin_ws/src/mavros/mavros /home/lucas/catkin_ws/build /home/lucas/catkin_ws/build/mavros/mavros /home/lucas/catkin_ws/build/mavros/mavros/CMakeFiles/run_tests_mavros_gtest_libmavros-sensor-orientation-test.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : mavros/mavros/CMakeFiles/run_tests_mavros_gtest_libmavros-sensor-orientation-test.dir/depend

