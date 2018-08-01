#!/bin/sh

# fetch all results
cat results/*/*/stdout | \

# eliminate non IP traffic
grep -E "^[^ ]+ IP" | \

# rip out pairs of IPs
sed -r 's/^.*IP ([^ ]+) > ([^ ]+):.*$/\1 \2/' | \

# dedupe
sort | uniq 
