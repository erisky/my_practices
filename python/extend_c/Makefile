

.phony: build_module


all: build_module install test

build_module:
	gcc -fpic --shared $(shell python3-config --includes) samplemodule.c -o sample.abi3.so

install:
	sudo python3 setup.py install

test:
	python3 testsample.py

