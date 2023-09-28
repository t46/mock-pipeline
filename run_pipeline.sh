#!/bin/bash

for i in {1..50}
do
   echo "Running iteration $i"
   python pipeline.py
done
