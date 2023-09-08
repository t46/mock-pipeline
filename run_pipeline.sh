#!/bin/bash

for i in {1..21}
do
   echo "Running iteration $i"
   python pipeline.py
done
