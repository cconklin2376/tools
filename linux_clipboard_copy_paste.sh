#!/bin/bash

# http://web.archive.org/web/20120626184619/http://whereswalden.com/2009/10/23/pbcopy-and-pbpaste-for-linux

sudo apt-get install -y xsel

alias pbcopy='xsel --clipboard --input'
alias pbpaste='xsel --clipboard --output'
