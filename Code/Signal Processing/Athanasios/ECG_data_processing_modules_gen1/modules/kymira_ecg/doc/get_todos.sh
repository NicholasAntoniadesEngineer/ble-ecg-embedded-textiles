#!/bin/bash

# Retrieves the TODO items from all python files in a directory (usually a module)
#
# :author: Athanasios Anastasiou
# :date: Jan 2022

echo "TODO List as of "`date`
egrep "TODO:" -Hn $1/*.py|sed -e 's/:[ \t]*#//g'