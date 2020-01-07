#!/usr/bin/env bash
# Bash script that lists all the subdomains asociated one domain IP
func1 () {
    if [ "$1" ] && [ "$2" ]
    then
	dig $2.$1 | grep -A1 'ANSWER SECTION:' |grep -v 'ANSWER SECTION:' | awk -v var="$2" '{print "The subdomain " var " is a " $4 " record and points to " $5 }'
    elif [ "$1" ]
    then
	for sub in www lb-01 web-01 web-02;do
	    dig $sub."$1" | grep -A1 'ANSWER SECTION:' |grep -v 'ANSWER SECTION:' | awk -v var="$sub" '{print "The subdomain " var " is a " $4 " record and points to " $5 }'
	done
    fi
}

func1 $1 $2
