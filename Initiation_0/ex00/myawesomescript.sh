#!/bin/bash
if [ -z "$1" ]; then
    echo "Arg is empty";
    exit 1;
fi

url=$(curl -sIL "$1" | grep -i "location:" | cut -d' ' -f2 | cut -d$'\n' -f1)

echo $url 