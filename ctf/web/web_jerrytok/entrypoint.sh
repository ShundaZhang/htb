#!/bin/ash

# Secure entrypoint
chmod 600 /entrypoint.sh

# Secure PHP Installation
mkdir -p /etc/php82/conf.d
mkdir -p /run/apache2

echo "disable_functions = exec, system, popen, proc_open, shell_exec, passthru, ini_set, putenv, pfsockopen, fsockopen, socket_create, mail" >> /etc/php82/conf.d/disablefns.ini
echo "open_basedir = /www" >> /etc/php82/conf.d/openbdir.ini

# Run supervisord
/usr/bin/supervisord -c /etc/supervisord.conf