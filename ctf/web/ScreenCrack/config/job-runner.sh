#!/bin/sh

cd /www/
while true;
do
    php artisan queue:work --queue=default -v --sleep=600
done

