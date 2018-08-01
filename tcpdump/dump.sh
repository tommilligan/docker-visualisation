#!/bin/sh

echo 'Dumping network metadata'
docker network inspect $@ > inspect.json

echo 'Beginning TCP dump - use ^C to exit'

# Get all docker network ids from network names
docker network inspect -f '{{.Id}}' $@ | \

# Convert to a linux interface id in the form 'br-<12 char of network id>'
sed -r 's/^(.{12}).*$/br-\1/' | \

# Run tcpdump on these bridge interfaces in parallel
sudo parallel --results results tcpdump -n -i

