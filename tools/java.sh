#!/usr/bin/env bash
OPENJDKDEB="openjdk-7-jre"
OPENJDKFEDORA="java-1.7.0-openjdk"

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <Java Type> <Architecture>"
    exit 1
fi
if [[ $1 == 0 ]]; then #OpenJDK
    yum install $OPENJDKFEDORA 2>/dev/null 1>/dev/null
    status=$?
    if [ $status -ne 0 ]; then
	apt-get -y install $OPENJDKDEB 2>/dev/null 1>/dev/null
    fi
else
    if [[ $2 == 0 ]]; then #32 bit
	wget -O java.tar.gz http://javadl.sun.com/webapps/download/AutoDL?BundleId=83374 2>/dev/null 1>/dev/null
    else #64 bit
	wget -O java.tar.gz http://javadl.sun.com/webapps/download/AutoDL?BundleId=83376 2>/dev/null 1>/dev/null
    fi
    tar -xzf java.tar.gz -C /usr/bin/java
    for file in /usr/bin/java/jre*/bin/*
    do
	ln -s /usr/bin/java/jre*/bin/$file /usr/bin/$file
    done
    rm java.tar.gz
fi
exit 0