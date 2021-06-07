#!/bin/sh 

TIMEOUT="5s"

while : ; do
    python3 main.py
    echo "Restarting occurs in $TIMEOUT"
    sleep $TIMEOUT 
done

