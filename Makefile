#!/usr/bin/make -f

.PHONY: all
all: requirements.txt

requirements.txt: requirements.in
	pip-compile --upgrade -o $@ $^
