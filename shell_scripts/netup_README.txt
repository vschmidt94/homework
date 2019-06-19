Problem 1.a

Write a script checking that networking is up. 
The script should execute at system startup.
Instruction: How would you set it up?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Discussion:

 - Suggest we define what "networking is up"
   actually means.
 - Could encompass:
   1. Network link is up
	- Physical / layer 1
        Q: ? What about multiple links ?
	   Is there requirement for specific link?
   2. Can we make first hop to gateway?
	- Again, potential for multiple gateways based 
	  on routing.
   3. Can we communicate with *something*?
	Q: Are we firewalled? What are we expected to 
           communciate with that would validate
	   the network is 'up'?
	Q: What protocols might be disallowed?
	   ping is a common utility, but also common for ICMP
	   protocol to be blocked. Going to avoid use of ping
	   for this reason.

Assuming the problem is to check for 'useful connectivity', and not just
that the loopback route is functional on an otherwise airgapped device,
I am submitting 2 possible implmentations as described below. The choice
of which to use is determined by the degree of connectivity that is
desired.

Implementation #1: netup1.sh
============================

For this one, I am going to assume 'networking is up' intends to 
require that we can communicate bi-directionally on the network.
i.e., we can do useful work. For demo purposes, the validation is
based on successful wget from google.com, but could just as well
be an internal address, etc.

Mechanism: use netcat (nc) command to attempt communication with
           authoritative IP address + port. In this example, using
           Google's DNS server 8.8.8.8, port 443 (HTTPS)

Implementation #2: netup2.sh
============================

Alternate script that might be more appropriate for devices on
internal network or otherwise firewalled.

Machanism: use route command to locate the gateway IP that is
	   up.  i.e., find a IP address in route table with flags
	   'UG'.


Installation instructions for boot-time exectution
--------------------------------------------------

1. For SystemMD distibutions (Fedora, Centos, RHEL, +more):
   
   - Edit netup.service file with the appropriate shell script desired.
   - Copy that file to /usr/lib/systemd/system/ directrory
   - Enable the service using `systemctl enable netup.service`

2. Alternatively, use Cron daemon.

   - Details of this approach will be an exercise left to the reader.

Final Note
----------

Note: Neither of these scripts perform any action based on the 
      results of the network test. They should be expanded to 
      perform an action - perhaps shutdown the unit or ???.
