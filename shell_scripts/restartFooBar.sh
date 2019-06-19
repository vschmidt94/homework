#!/bin/bash

# Note: Assume `user` has sufficient rights to execute systemctl 
# without being prompted for a password.

# Assumes the IP's in text file are generally good and machines
# are responsive. Using the `timeout` option to prevent extraordinary
# waits if this is not the case.

FILENAME="machines_list.txt"
SSH_USER="user"
SSH_PW="password"
SERVICE="fooBar.service"

while IFS= read -r line
do
  IP="$line"
  COMMAND="ssh $SSH_USER@$IP 'systemctl restart $SERVICE'"
 
  # Debugging - uncomment this line to see command in terminal. 
  # Echo the command to standard err for inspection.
  # echo "$COMMAND" >&2

  timeout --preserve-status 5 $COMMAND

  # Output results to stderr
  if [ $? -eq 0 ]; then
    RESULT="SUCCESS"
  else
    RESULT="FAILURE"
  fi

  echo "$RESULT - restarting $SERVICE on $IP" >&2


done < "$FILENAME"

echo "Finished" >&2
