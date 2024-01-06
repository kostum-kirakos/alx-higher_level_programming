#!/bin/bash
# Send a GET request to the provided URL with the required header and display the response body
curl -H "X-School-User-Id: 98" -s "$1"
