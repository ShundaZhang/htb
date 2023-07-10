#!/bin/sh
while true; do php -dextension=/php_logger.so -S 0.0.0.0:1337; done
