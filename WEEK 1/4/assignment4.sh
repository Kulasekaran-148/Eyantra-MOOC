#!/bin/bash
#get the Cartesian x and y coodinates of a point that are passed as arguments
#convert the Cartesian coordinates to the corresponding polar coordinates
#compute radius and theta (in degrees) upto 5 decimal places
#note: theta should range from 0 to 360 degrees

let a=($1*$1 + $2*$2)
radius=$(bc -l <<< "sqrt($a)")
printf "%.5f" $radius
printf ", "
if [[ $1 -eq 0 && $2 -ne 0 ]] #checking for infinity condition
then
 if [ $2 -gt 0 ] #if argument 2 is greater than 0
  then
  theta=90
  printf "%.5f\n" $theta
 else #if argument 2 is less that 0
  theta=270
  printf "%.5f\n" $theta
 fi
else #when not infinity condition
 if [[ $1 -eq 0 && $2 -eq 0 ]]
 then
  printf "%.5f\n" 0
 elif [[ $1 -ne 0 ]]
 then
  c=$(bc -l <<< "$2/$1")
  d=$(bc -l <<< "a ($c)")
  e=$(bc -l <<< "180*$d")
  theta=$(bc -l <<< "$e/3.14159265358979323846")
   if [[ $1 -gt 0 && $2 -gt 0 ]] #1st quadrant
   then
    printf "%.5f\n" $theta
   elif [[ $1 -lt 0 && $2 -gt 0 ]] #2nd quadrant
   then
    theta=$(bc -l <<< "180+$theta")
    printf "%.5f\n" $theta
   elif [[ $2 -eq 0 ]]
   then 
    if [ $1 -gt 0 ]
    then 
     printf "%.5f\n" 0
    else
     printf "%.5f\n" 180
    fi
   elif [[ $1 -lt 0 && $2 -lt 0 ]] #3rd quadrand
   then
    theta=$(bc -l <<< "180+$theta")
    printf "%.5f\n" $theta
   elif [[ $1 -gt 0 && $2 -lt 0 ]] #4th quadrant
    then
    theta=$(bc -l <<< "360+$theta")
    printf "%.5f\n" $theta
   fi
  fi
fi
