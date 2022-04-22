#!/bin/bash
# (-o)utput f to null -w(rite) display transfed info in var content to stdout
curl -o /dev/null -s -w "%{http_code}" $1
