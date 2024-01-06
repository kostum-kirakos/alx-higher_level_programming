#!/bin/bash
# a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

curl -s GET "$1"
