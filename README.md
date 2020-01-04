Automated Monitoring using CMDB
===============================
Using a CMDB model, Customers can create Automatic Monitoring for their:
- Infrastructure(s)
- Platform(s)
- Applications(s)
- Service(s)  
-------------------------------

Git repo : https://github.com/erlisb/auto_monitoring_cmdb

Requirements
------------
In order to set up this testing environment, you need to install the following tools/packages :

- docker
  - docker images : python:3.7.6, jordan/icinga2:latest
- docker-compose
- virtualenv
- pip
- python packages :
  - Flask
  - flask_restful
  - requests
  - sqlite


Usage
-----
```sh
docker-compose up
```

Test
-----
1. Test the Flask REST API
```
curl -v http://localhost:6000/health

Response :

* Connected to localhost (127.0.0.1) port 6000 (#0)
> GET /health HTTP/1.1
> Host: localhost:6000
> User-Agent: curl/7.58.0
> Accept: */*
> 
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
```

2. Test the Icinga API
```
curl -v -k -s -u root:<root_password> 'https://localhost:5665/v1/objects/hosts?pretty=1'

Response :

> GET /v1/objects/hosts?pretty=1 HTTP/1.1
> Host: localhost:5665
> Authorization: Basic cm9vdDpjZjdkNmI4NTM3ZGJlZDRm
> User-Agent: curl/7.58.0
> Accept: */*
> 
< HTTP/1.1 200 OK
< Server: Icinga/r2.11.2-1
< Content-Type: application/json
```

Author
------
Erlis Balla <erlis.balla@lhind.dlh.de>
