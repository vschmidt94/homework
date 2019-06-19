#!/bin/bash

function GetGateway() 
{
  local address=$(route -n | grep 'UG[ \t]' | awk '{print $2}')

  # If we could not get a route to the default gateway, won't be
  # able to access network.
  if [ -z "$address" ]; then
    return 1
  fi

  return 0
}

GetGateway
