#!/usr/bin/env bash
OPENJDKDEB="openjdk-7-jre"
OPENJDKFEDORA="java-1.7.0-openjdk"

yum install $OPENJDKFEDORA 2>/dev/null 1>/dev/null
status=$?
if [ $status -ne 0 ]; then
    apt-get -y install $OPENJDKDEB 2>/dev/null 1>/dev/null
fi

exit 0