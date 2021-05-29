#!/bin/bash
#THis enables Old and nee ABI compatibelity
conan profile new default --detect
conan profile update settings.compiler.libcxx=libstdc++11 default