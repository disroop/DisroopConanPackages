#!/bin/bash
#This enables Old and nee ABI compatibility
conan profile new default --detect
conan profile update settings.compiler.libcxx=libstdc++11 default