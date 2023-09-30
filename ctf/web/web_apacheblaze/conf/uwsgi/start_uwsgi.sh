#!/bin/sh
set -e
uwsgi --ini /app/uwsgi/conf1.ini --thunder-lock --enable-threads &
uwsgi --ini /app/uwsgi/conf2.ini --thunder-lock --enable-threads &

# Apache gets grumpy about PID files pre-existing
rm -f /usr/local/apache2/logs/httpd.pid

exec httpd -DFOREGROUND "$@"