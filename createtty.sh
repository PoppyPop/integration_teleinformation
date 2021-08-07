#!/bin/bash
#

socat -d -d -v pty,raw,echo=0,link=./reader pty,raw,echo=0,link=./writer
