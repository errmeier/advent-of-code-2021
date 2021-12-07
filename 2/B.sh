#!/bin/bash

# For a series of commands:
#   down X increases the aim by X
#   up X decreases the aim by X
#   forward X increases horizontal position by X and depth by aim*X
# Return product of horizontal position and depth

input="input.txt"
depth=0
distance=0
aim=0
readarray -t lines < "$input"
for index in ${!lines[@]}; do
    line=(${lines[index]})
    if [ ${line[0]} == "forward" ]; then
        ((distance += ${line[1]}))
        ((depth += ${line[1]}*aim))
    elif [ ${line[0]} == "down" ]; then
        ((aim += ${line[1]}))
    else 
        ((aim -= ${line[1]}))
    fi
done

echo "$((depth * distance))"
