#!/bin/bash

TESTIP=8.8.8.8   # Google's DNS server, highly available
TESTPORT=443     # HTTPS port

function TestNet()
{
# Using netcat in port scan mode for quick check.
# with options:
# -z = zero I/O mode
# -d = Don't attempt to read from stdin. Probably not needed for this.
# -w1 = Wait 1 second before timeout. Could lower into milliseconds.
  if nc -dzw1 $TESTIP $TESTPORT; then
    return 0
  fi
  return 1 
}

TestNet
