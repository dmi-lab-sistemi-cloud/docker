#!/bin/bash

# build images
for image in client server
do
    echo "[+] Building py${image} image ..."
    docker build -f "${image}/Dockerfile" -t py${image}:latest "${image}"
done