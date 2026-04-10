cmake_minimum_required(VERSION 3.22)
project(VocalForgePersonaPlexLab VERSION 0.1.0)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Point JUCE_DIR at your JUCE checkout or use FetchContent.
if(NOT DEFINED JUCE_DIR)
  message(STATUS "Set JUCE_DIR to your local JUCE checkout before building.")
endif()

add_library(VocalForgeCore STATIC
  Source/services/BackendClient.cpp
  Source/models/VoiceModel.cpp
)

target_include_directories(VocalForgeCore PUBLIC Source)

# This file is intentionally a starter shell; wire juce_add_plugin when your local JUCE path is configured.
