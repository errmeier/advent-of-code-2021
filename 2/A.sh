#!/bin/bash

# For a series of commands,
#   forward X increases the horizontal position by X
#   down X increases the depth by X
#   up X decereases the depth by X
# return the product of the horizontal position and depth

input="input.txt"
depth=0
distance=0
readarray -t depths < "$input"
for index in ${!depths[@]}; do
    line=(${depths[index]})
    if [ ${line[0]} == "forward" ]; then
        ((distance += ${line[1]}))
    elif [ ${line[0]} == "down" ]; then
        ((depth += ${line[1]}))
    else 
        ((depth -= ${line[1]}))
    fi
done

echo "$((depth * distance))"
