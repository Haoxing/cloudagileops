#!/bin/bash

if [ "$1" ==  "" ] ; then 

echo "usage build.sh <tag>"
exit 1

fi


echo "tag: $1"


docker build . -t $1

