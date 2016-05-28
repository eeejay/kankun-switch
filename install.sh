#!/bin/sh

if [ -z "$1" ]
  then
    echo "No host supplied"
    exit 1
fi

scp -r index.html cgi-bin root@$1:/www
