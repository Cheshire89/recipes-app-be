#!/bin/sh

set -e

envsubst < /etc/nginx/default.conf.tpl > /tc/nginx/conf.d/default.conf
nginx -g 'daemon off;'