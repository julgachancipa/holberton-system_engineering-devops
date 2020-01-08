#!/bin/bash
#Only status code
curl -sL -w "%{http_code}" -I "$1" -o /dev/null
