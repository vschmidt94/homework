# Homework problems

Instructions: clone this repo locally, preferably on a Linux machine with Python3.

## Shell Scripts (Problem 1)

### Script 1: Discussion

 - Suggest we define what "networking is up" actually means.
 - I considered the following scenarios:
   1. Network link is up
	    - i.e., testing Physical / layer 1
        - Q: ? What about multiple links ?
        - Is there requirement for specific link?
        - Ultimately, what good is this - if physical link is up, so what? Generally networking implies communication.
   2. Can we make first hop to gateway?
	    - Again, potential for multiple gateways based on routing.
   3. Can we communicate with *something*?
        - Q: Are we firewalled? What are we expected to communciate with that would validate the network is 'up'?
        - Q: What protocols might be disallowed?
	        - ping is a common utility, but also common for ICMP protocol to be blocked. Going to avoid use of ping for this reason.

Assuming the problem is to check for 'useful connectivity', and not just that the loopback route is functional on an otherwise airgapped device, I am submitting 2 possible implmentations as described below. The choice of which to use is determined by the degree of connectivity that is desired.

#### Script 1 / Implementation #1: netup1.sh

For this one, I am going to assume 'networking is up' intends to require that we can communicate bi-directionally on the network. i.e., we can do useful work. For demo purposes, the validation is based on successful wget from google.com, but could just as well be an internal address, etc.

- Mechanism:
    - use `netcat` (`nc`) command to attempt communication with authoritative IP address + port. In this example, using Google's DNS server 8.8.8.8, port 443 (HTTPS)

#### Script 1 / Implementation #2: netup2.sh

Alternate script that might be more appropriate for devices on internal network or otherwise firewalled.

- Machanism:
    - Use `route` command to locate the gateway IP that is up.  i.e., find a IP address in route table with flags `UG`.


### Installation instructions for boot-time exectution

1. For SystemMD distibutions (Fedora, Centos, RHEL, +more):
   - Edit netup.service file with the appropriate shell script desired.
   - Copy that file to `/usr/lib/systemd/system/` directrory
   - Enable the service using `systemctl enable netup.service`

2. Alternatively, use Cron daemon.
   - Details of this approach will be an exercise left to the reader.

#### Afterthoughts on Script 1 assignment:

1. I realized after the fact that only Script 2 actually specified shell scripts. I would probably look to convert these to Python scripts.
2. Neither script actually *does* anything as a result of the testing. They should be expanded to perform an action, perhaps periodically attempt to restart the networking services. Without networking, a more common action like an email alert won't be any useful. In the old days, we could trigger the CD drive to open and close as a flag wave...

### Script 2: Remotely restart FooBar service

#### Script 2 / Implementation: restartFooBar.sh

- Mechanism: `ssh` into each box and restart the desired service.

This one is fairly straightforward. Would be good to set this up for command-line parameters, but I get the impression you are kicking an internal server farm.  Still the hard-coded user name and password is less than desirable. In the future, I would move this to its own configuration / init file.

Another good candidate for being a Python script, but it was specified to use bash script.

I did provide some very basic output as that could be useful to user. Also note timeout set to 5 seconds (hardcoded), that could be adjusted based on real life experience. I'm noting this because the script is going to kick each server in the list in serial fashion, and could be slow if the server list is large. For large server counts, this needs to be redone to fork and go parallel.

## Back-end RESTful API (Problem 2)

Implemented using Python / Flask (specifically Flask-RESTplus)

Flask application is in `backend` directory of git repo.  There Pipfile/Pipfile.lock that can be used to recreate a pipenv (and a requirements.txt).

Dev config launch should be basically:
- `python manage.py run` to launch the flask app.
- `python manage.py test` to launch the unit tests

Right now set to listen on localhost port 5000

### On Flask

I knew from Sarah that Flask is preferred over Django, so I used this as opportunity to touch Flask. To be honest, I'm still wrapping my head around it, progress was frustratingly slow - and I realized the tutorial I initially latched onto (Greg Obinna's at: https://medium.com/free-code-camp/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563) doesn't use the most Pythonic structure.  Seems like this article proposes a cleaner organization: http://michal.karzynski.pl/blog/2016/06/19/building-beautiful-restful-apis-using-flask-swagger-ui-flask-restplus/

I opted for `Flask-RESTplus` to leverage the built-in Swagger interface.

Also, I need a better understanding of the database join syntax. I have a simple join working between users and roles - but that's largly just some Flask magic.

### On unit tests

There are currently ~ 14 unit tests.  On retrospect, I think `Pytest` module would have been a better choice after more reading. The fixtures concept there seems useful.  Due to time constraints, I did not attempt swapping this out.

### On functionality

I was able to get a basic authentication / authorization scheme in place. I'm not entirely sure every endpoint is decorated appropriately, but seems to be largely working when exercised through Swagger.

### On deployment

I am not entirely sure how far I should take this. I did plan for different databases to be used for testing, dev, and production. That can be set / controlled with an environment variable. The unit tests actually do make use of the testing database, while normal dev DB is untouched.

For physical deployment, suggest setting up a NGINX server and deploying via WSGI.  I've done similar in the past with Jupyter servers, but would have to work through all the details again to provided detailed instructions.

### Front-End Web Interface (Problem 3)

Yet to be done due to time constraints - but there is the Swagger interface mentioned above.

I was hoping to use this as an opportunity to make an Angular 8 application, as that's something I've never touched and hope to spend more time with.