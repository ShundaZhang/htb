#!/bin/bash

for i in {0..130}
do
	echo $i
	forge create src/Contract.sol:Contract --rpc-url http://157.245.43.189:31608/rpc --private-key 0x2de3d450f2b9f28d5640560572511a56b1133ff1f39236fc40e51c6fb55e945c
done
