#!/bin/bash

#take the input of csv file name which is passed as an argument


#print the details of only 1st and 3rd column, if the first column data starts with letter "S"
#and sort it alphabetically based on first column data

grep -h ^S $1 | sort -s -t "," -k1,1  | cut -d',' -f1,3 
