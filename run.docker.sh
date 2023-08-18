#!/bin/sh

docker build -t img-py-azdo-tmp-$1 .

docker run --name py-azdo-tmp-$1 -p 8000:8080 -it --detach img-py-azdo-tmp-$1

docker exec -it py-azdo-tmp-$1 sh
