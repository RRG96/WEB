#echo "magumbos.local" > /etc/hostname
#reboot
apt install mailutils postfix -y

echo "# See /usr/share/postfix/main.cf.dist for a commented, more complete version
# Debian specific:  Specifying a file name will cause the first
# line of that file to be used as the name.  The Debian default
# is /etc/mailname.
#myorigin = /etc/mailname

smtpd_banner = $myhostname ESMTP $mail_name (Debian/GNU)
biff = no

# appending .domain is the MUA's job.
append_dot_mydomain = no

# Uncomment the next line to generate "delayed mail" warnings
#delay_warning_time = 4h

readme_directory = no

# TLS parameters
smtpd_tls_cert_file=/etc/ssl/certs/ssl-cert-snakeoil.pem
smtpd_tls_key_file=/etc/ssl/private/ssl-cert-snakeoil.key
smtpd_use_tls=yes
smtpd_tls_session_cache_database = btree:${data_directory}/smtpd_scache
smtp_tls_session_cache_database = btree:${data_directory}/smtp_scache

# See /usr/share/doc/postfix/TLS_README.gz in the postfix-doc package for
# information on enabling SSL in the smtp client.

smtpd_relay_restrictions = permit_mynetworks permit_sasl_authenticated defer_unauth_destination
myhostname = magumbos.local
alias_maps = hash:/etc/aliases
alias_database = hash:/etc/aliases
myorigin = /etc/mailname
mydestination = magumbos.local, localhost, localhost.localdomain, localhost
relayhost = [smtp.gmail.com]:587
mynetworks = 127.0.0.0/8 [::ffff:127.0.0.0]/104 [::1]/128
mailbox_command = procmail -a "$EXTENSION"
mailbox_size_limit = 0
recipient_delimiter = +
inet_interfaces = all

# Enables SASL authentication for postfix
smtp_sasl_auth_enable = yes
# Disallow methods that allow anonymous authentication
smtp_sasl_security_options = noanonymous
# Location of sasl_passwd we saved
smtp_sasl_password_maps = hash:/etc/postfix/sasl/sasl_passwd
# Enable STARTTLS encryption for SMTP
smtp_tls_security_level = encrypt
# Location of CA certificates for TLS
smtp_tls_CAfile = /etc/ssl/certs/ca-certificates.crt" > /etc/postfix/main.cf

echo "[smtp.gmail.com]:587 magumbocitos@gmail.com:hola123.," > /etc/postfix/sasl/sasl_passwd
postmap /etc/postfix/sasl/sasl_passwd
chown root:root /etc/postfix/sasl/sasl_passwd
chmod 600 /etc/postfix/sasl/sasl_passwd
systemctl restart postfix

apt-get install libnss-ldap -y
echo "# /etc/nsswitch.conf
#
# Example configuration of GNU Name Service Switch functionality.
# If you have the glibc-doc-reference' and info' packages installed, try
# info libc Name Service Switch for information about this file.

passwd:         files systemd ldap
group:          files systemd ldap
shadow:         files ldap
gshadow:        files ldap

hosts:          files mdns4_minimal [NOTFOUND=return] dns
networks:       files

protocols:      db files
services:       db files
ethers:         db files
rpc:            db files

netgroup:       nis" > /etc/nsswitch.conf
