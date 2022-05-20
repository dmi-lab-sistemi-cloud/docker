#!/bin/bash -x

# create user bridge network
NETWORK="pysocket"

# create network (if it does not exist)
docker network create $NETWORK

# run server in background
docker run --rm --name pyserver -d --network $NETWORK pyserver:latest

# run client in foreground (passing the server name as an env variable)
#docker run --rm --name pyclient --env HOST=pyserver -it --network $NETWORK pyclient:latest
docker run --rm --name pyclient -it --network $NETWORK pyclient:latest

# stop the server (due to the --rm flag, it will also be removed)
#docker container stop pyserver

# list containers looking for pysever OR pyclient
docker ps --all | grep "pyserver\|pyclient"
