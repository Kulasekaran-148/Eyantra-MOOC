#!/bin/bash
#take the input file name which is passed as an argument
#find the number of lines with one or more digits present in the input file
#print the number of line with one or more digits found
#find the digits present in the input file
#print the digits found
echo "Number of lines having one or more digits are: $(grep -c "\<[0-9]*\>" $1)"
echo "Digits found:"
grep -wo "[0-9]*" $1

