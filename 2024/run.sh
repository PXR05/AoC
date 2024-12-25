#!/bin/bash

run_day() (
    local day=$1
    local dir="d${day}"
    
    if [ ! -d "$dir" ]; then
        echo "Directory $dir does not exist"
        return 1
    fi
    
    cd "$dir" || return 1
    echo ""
    echo "Running day $day solution..."
    
    start_time=$(date +%s.%N)
    python3 "d${day}.py" 2>&1
    exit_code=$?
    end_time=$(date +%s.%N)
    
    duration=$(echo "$end_time - $start_time" | bc)
    
    if [ $exit_code -eq 0 ]; then
        echo "Completed in ${duration}s"
    else
        echo "Failed with exit code $exit_code"
    fi
    
    cd - > /dev/null
    return $exit_code
)

if [ "$1" == "-a" ]; then
    for d in ./d*/; do
        day=${d//[!0-9]/}
        run_day "$day"
    done
else
    if [ -z "$1" ]; then
        echo "Usage: $0 <day_number> or $0 -a for all days"
        exit 1
    fi
    run_day "$1"
fi

