#!/bin/bash
docker build -t expenses-app .
docker run -it --rm -v $(pwd)/data:/data expenses-app
