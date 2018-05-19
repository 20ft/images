FROM alpine
RUN apk update ; apk upgrade
RUN apk add git php7 php7-openssl php7-json php7-phar php7-iconv php7-zlib php7-mbstring php7-intl php7-xml php7-simplexml php7-dom php7-tokenizer php7-ctype php7-session php7-curl php7-fileinfo php7-fpm  php7-pgsql php7-gd gd nginx

COPY silverstripe.sh /etc/profile.d/
COPY nginx.conf /etc/nginx/conf.d/

COPY compose_install.sh /
RUN /bin/sh compose_install.sh
RUN php /composer.phar create-project silverstripe/installer /site
RUN cd /site ; php /composer.phar require silverstripe/postgresql
