# coding: utf-8
import urllib
from PyQt4.QtCore import QByteArray
from PyQt4.QtNetwork import QSslCertificate
from qgis.gui import QgsAuthCertInfoDialog

# Certificate for test from http://fm4dd.com/openssl/certexamples.htm
# The one retrieved is http://fm4dd.com/openssl/source/PEM/certs/1024b-rsa-example-cert.pem

remote_url = 'http://fm4dd.com/openssl/source/PEM/certs/1024b-rsa-example-cert.pem'
pem_path = remote_url.split('/')[-1]
# Fetch certificate from remote url and write to file
with open(pem_path, 'wb') as f:
    certificate_string = urllib.urlopen(remote_url).read()
    f.write(certificate_string)

# Instanciate a first QgsAuthCertInfoDialog using QSslCertificate.fromPath
auth_cert_info_dialog_1 = QgsAuthCertInfoDialog(
    QSslCertificate.fromPath(pem_path)[0],
    True
)

auth_cert_info_dialog_1.show()


# Instanciate a second QgsAuthCertInfoDialog using QSslCertificate.fromData
auth_cert_info_dialog_2 = QgsAuthCertInfoDialog(
    QSslCertificate.fromData(
        QByteArray(certificate_string)
    )[0],
    False
)

auth_cert_info_dialog_2.show()

print(auth_cert_info_dialog_1.certInfoWidget())  # QgsAuthCertInfo
print(auth_cert_info_dialog_1.trustCacheRebuilt())  # Boolean
