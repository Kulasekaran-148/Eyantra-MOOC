#!/bin/bash

#take the input file name which is passed as an argument

#find the valid IP addresses present in the input file

#print the valid IP addresses found

grep -o ' [0-9]\{1,\}\.[0-9]\{1,\}\.[0-9]\{1,\}\.[0-9]\{1,\} ' $1  | sed 's_^ __g' | awk ' 
BEGIN {
FS="."
}

{
if(NF==4)
	{
	if( $1>=0 && $1<256 && $2>=0 && $2<256 && $3>=0 && $3<256 && $4>=0 && $4<256 )
		{ 
		if( $1>=0 && $1<=127 )
		print$1"."$2"."$3"."$4"A"
		if( $1>=128 && $1<=191 )
		print$1"."$2"."$3"."$4"B"
		if( $1>=192 && $1<=223 )
		print$1"."$2"."$3"."$4"C"
		if( $1>=224 && $1<=239 )
		print$1"."$2"."$3"."$4"D"
		if( $1>=240 && $1<=247 )
		print$1"."$2"."$3"."$4"E"
		if( $1>=248 && $1<=255 )
		print$1"."$2"."$3"."$4"Not Defined"
		}
	}
}
END{
}
' 



