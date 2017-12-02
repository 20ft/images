# docker build -t tfnz/mail .
FROM alpine

# install exim and dovecot
RUN apk update ; apk add exim dovecot

# create directory structures
RUN mkdir -p /var/mail                          ; \
    chown 100:103 /var/mail                     ; \
    mkdir -p /var/log/exim/                     ; \
    touch /var/log/exim/mainlog                 ; \
    chown 100:103 /var/log/exim /var/log/exim/* ; \
    mkdir -p /usr/lib/exim/                     ; \
    chown 100:103 /usr/lib/exim/                ; \
    touch /var/log/dovecot.log                  ; \
    chown dovecot:dovecot /var/log/dovecot.log

# copy in dovecot's config
COPY dovecot.conf /etc/dovecot/
COPY 1*.conf 2*.conf /etc/dovecot/conf.d/
COPY auth-passwdfile.conf.ext /etc/dovecot/conf.d/

# copy in exim template
COPY exim_template /home/admin/
