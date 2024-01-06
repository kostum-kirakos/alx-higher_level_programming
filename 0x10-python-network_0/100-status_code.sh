#!/bin/bash
# Send a GET request to the provided URL and display only the status code
curl -s -w %"{http_code}" -o /dev/null "$1"
