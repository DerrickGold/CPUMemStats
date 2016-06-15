#!/bin/bash

CURDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

protocol="$1"
port="$2"

python3 "$CURDIR/cpumemstats.py" "$protocol" "$port"
