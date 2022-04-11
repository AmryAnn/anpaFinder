#! /bin/bash
while getopts "w:" flag; do
   case "${flag}" in
	w) 
	  WEBPAGE=${OPTARG};;
   esac
done
echo $WEBPAGE #parameter argument: webpage url

python anpatools.py --url $WEBPAGE	#calls python script