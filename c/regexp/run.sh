#!/bin/bash

mkdir -p build
cd build
cmake ..
make 

./my_prog ^[A-D]{3}_[1-9]+_[1-9] ACD_12345_123
./my_prog ^[A-D]{3}_[1-9]+_[1-9] ABCD_12345_123
./my_prog ^[A-D]{3}_[1-9]+_[1-9] ACDZ_12345_123

./my_prog ^[A-D]{3}_[1-9]+_[1-9] ACDZ_12345_123
./my_prog [A-D]{3}_[1-9]+_[1-9]  kloiACDZ_12345_123
./my_prog ^[A-D]{3}_[1-9]+_[1-9]+AZ$ ACD_12345_1239AB
./my_prog ^[A-D]{3}_[1-9]+_[1-9]+AZ$ ACD_12345_1239AZ

