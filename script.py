import sys
import os
import qrcode

dir_name = sys.argv[2] if len(sys.argv) == 3 else 'qr_codes'

try:
    os.makedirs(dir_name)
except OSError as e:
    if not os.path.isdir(dir_name):
        raise

db = open(sys.argv[1], 'r')

def build_url(list):
    string = 'otpauth://totp/'
    string += list[1] + '?'
    string += 'secret=' + list[2]
    string += '&'
    string += 'issuer=' + list[6]

    return string

with db:
    for line in db:
        data_list = line.split('|')
        url = build_url(data_list)
        qr = qrcode.make(url)

        file_name = data_list[1] + '.png'
        file_name = file_name.replace('/', '.')
        file_name = file_name.replace(':', ' ')
        file_name =  dir_name + '/' + file_name

        qr.save(file_name)
