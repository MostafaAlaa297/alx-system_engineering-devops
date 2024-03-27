#!/bin/bash
# Take URL as input
curl -sI $1 | grep "Content-Length" | cut -d " " -f2
