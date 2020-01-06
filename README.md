Automated Monitoring using CMDB
===============================
Using a CMDB model, Customers can create Automatic Monitoring for their:
- Infrastructure(s)
- Platform(s)
- Application(s)
- Service(s)  
-------------------------------

Git repo : https://github.com/erlisb/auto_monitoring_cmdb

Testing Environment 
-------------------

![Image description](env.jpg)


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
  - pyyaml
  - urllib3


Usage
-----
1. Create Docker containers :
```sh
docker-compose up
```
2. List Docker containers :
```sh
docker-compose ps -a

                  Name                          Command         State                          Ports                       
---------------------------------------------------------------------------------------------------------------------------
auto_monitoring_cmdb_flask_rest_facade_1   python /opt/app.py   Up      0.0.0.0:6000->5000/tcp                             
auto_monitoring_cmdb_icinga2_1             /opt/run             Up      443/tcp, 0.0.0.0:5665->5665/tcp, 0.0.0.0:80->80/tcp
```
3. Stop/Remove Docker containers :
```sh
docker-compose down

Stopping auto_monitoring_cmdb_icinga2_1           ... done
Stopping auto_monitoring_cmdb_flask_rest_facade_1 ... done
Removing auto_monitoring_cmdb_icinga2_1           ... done
Removing auto_monitoring_cmdb_flask_rest_facade_1 ... done
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
In order to access Icinga2 API, we need the api user credentials :

2.1 - Enter inside icinga2 container we already created :

docker exec -it <icinga2_container> bash

2.2 - Update ubuntu repositories :

apt-get update

2.3 - Install vim editor :

apt-get install vim

2.4 - Modify config file : /etc/icinga2/conf.d/api-users.conf, as follows :

vi /etc/icinga2/conf.d/api-users.conf

2.5 - Set username & password :

Username : root
Password : icinga2
Permissions : *

2.6 - Test Icinga2 API using the above credentials :

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

References
-----
- Icinga API : https://icinga.com/docs/icinga2/latest/doc/12-icinga2-api/#icinga2-api-config-management
- Docker : https://docs.docker.com/install/linux/docker-ce/ubuntu/
- Docker Compose : https://docs.docker.com/compose/

Author
------
Erlis Balla <erlis.balla@lhind.dlh.de>
