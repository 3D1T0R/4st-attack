#!/bin/bash
# A shell script which uses imagemagick to
# resize 1024x768 images from themes to
# 800x600 and 640x480, it even makes the dirs
#
# Written for use with 4st Attack by Jeroen Vloothuis

themename=$1

cd data/graphics/$themename/1024x768

mkdir ../800x600
mkdir ../640x480

for i in $( ls *.png); 
do
	source=$i
	echo $i

	convert $i -scale 78.125% ../800x600/$i
	convert $i -scale 62.5% ../640x480/$i
	
done
										         

										    
