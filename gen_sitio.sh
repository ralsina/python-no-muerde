#!/bin/sh

rm -rf sources
hg clone https://python-no-muerde.googlecode.com/hg/ sources
find sources -type d -name hg -exec rm {} \;
r2w.py rst2web.ini