#!/bin/bash
# (-X) HTTP method -H header content type -d values of post
curl -s -X "POST" $1 -H "Content-type: application/json" -d @$2
