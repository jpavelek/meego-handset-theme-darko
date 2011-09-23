#!/bin/sh

for f in *.svg
do
    echo `echo $f | sed -e 's/.svg//g' `
    STEM=`echo $f | sed -e 's/.svg//g' `
    convert $f $STEM.png 
done
