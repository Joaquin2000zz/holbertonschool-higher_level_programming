#!/bin/bash
# -L to redirect n times -H header saying origin and -d value to autenticate
curl -s -L -X "PUT" -H "Origin: HolbertonSchool" -d "user_id=98" "0.0.0.0:5000/catch_me"
