#!/bin/bash

# Count the number of times the next element in an integer sequence causes the
# sum of the last [window] elements to increase

input="input.txt"
count=0
window=$1
readarray -t depths < "$input"
for i in ${!depths[@]}; do
    if [ $i -lt $window ]
    then
        continue
    fi

    if [ ${depths[$i]} -gt ${depths[$((i-window))]} ]
    then
        ((count++))
    fi
done

echo "$count"
