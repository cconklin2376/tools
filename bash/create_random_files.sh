#!/bin/bash

# aray of file sizes for random selection
sizes=(1 10 100 1000 10000 100000)

END=10 # number of files to create
FNLEN=12  # length of file names

# Seed random generator
RANDOM=$$$(date +%s)



for x in $(seq 1 $END); do
   fname=`cat /dev/urandom | tr -cd 'a-f0-9' | head -c $FNLEN`
   fsize=${sizes[$RANDOM % ${#sizes[@]} ]}
   ( dd if=/dev/zero of=GEN${fname} bs=1024 count=0 seek=$((1024 * $fsize)) status=none ) > /dev/null
done


