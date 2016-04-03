#!/bin/bash
rm -f output.txt
cd ..
for f in *.png
do
    echo "https://www.princeton.edu/deptafe_internal/cimg%210/$f" 1>> efaces/output.txt
    br -algorithm FaceRecognition -compare efaces/e1.png $f 1>> efaces/output.txt 2>> /dev/null
    br -algorithm FaceRecognition -compare efaces/e2.png $f 1>> efaces/output.txt 2>> /dev/null
    br -algorithm FaceRecognition -compare efaces/e3.png $f 1>> efaces/output.txt 2>> /dev/null
    br -algorithm FaceRecognition -compare efaces/e4.png $f 1>> efaces/output.txt 2>> /dev/null
    br -algorithm FaceRecognition -compare efaces/e5.png $f 1>> efaces/output.txt 2>> /dev/null
done
