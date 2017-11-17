#!/bin/bash

JSONLIST=$1
VOCPATH=$2

python gen_urllist.py --in $JSONLIST --vocpath $VOCPATH
URLLIST=$(realpath $JSONLIST.urllist)

cd $VOCPATH/JPEGImages
wget -i $URLLIST