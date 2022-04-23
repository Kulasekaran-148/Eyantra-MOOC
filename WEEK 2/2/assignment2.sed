#!/bin/sed -f

# write the sed command to remove single-line and multi-line comments
# but not delete those lines

s_//.*__ 
s_/\*.*\*/__ 
s_.*/\*.*__ 
s_.*\*/__ 
