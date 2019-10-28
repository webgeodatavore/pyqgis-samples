# coding: utf-8
import urllib
from PyQt4.QtNetwork import QSslCertificate
from qgis.gui import QgsAuthCertInfo

# Certificate for test from http://fm4dd.com/openssl/certexamples.htm
# The one retrieved is http://fm4dd.com/openssl/source/PEM/certs/1024b-rsa-example-cert.pem

remote_url = 'http://fm4dd.com/openssl/source/PEM/certs/1024b-rsa-example-cert.pem'
pem_path = remote_url.split('/')[-1]
# Fetch certificate from remote url and write to file
with open(pem_path, 'wb') as f:
    certificate_string = urllib.urlopen(remote_url).read()
    f.write(certificate_string)

# Instanciate a QgsAuthCertInfo using QSslCertificate.fromPath
auth_cert_info = QgsAuthCertInfo(
    QSslCertificate.fromPath(pem_path)[0],
    True
)

auth_cert_info.show()
