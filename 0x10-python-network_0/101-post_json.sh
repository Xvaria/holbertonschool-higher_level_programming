#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument, and displays the body of the response
curl -s "$1" -H "content-Type: application/json" -d "@$2"
