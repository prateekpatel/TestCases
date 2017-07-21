#!/bin/bash
echo "please list out the hostnames"

echo $@

for var in "$@"
do
 echo "enter the user name"
 read user
 ssh "$user@$var" ls && pwd
 echo $?
done

