# Google Authenticator Backup Tool

A (very)simple python script to convert the data retrived from Google Authenticator to QR codes.

## How-to use:

First, you need to get the sqlite database that contains your 2FA keys.

For this you need to have root acess on your android device.
With an adb connection established, get the database:

```bash
adb pull /data/data/com.google.android.apps.authenticator2/databases/databases
```
Alternatively, you can use a file explorer on the device with root privilege.

Second, you'll need to get the table that contains your accounts data (including the keys), and save the content on a text file.

```bash
sqlite3 databases "select * from accounts;" > databases.txt
```
Third, download the python script from this repository and install the necessary libraries via pip.

```bash
wget https://raw.githubusercontent.com/danielbibit/Google-Authenticator-Backup-Tool/master/script.py
pip install qrcode
pip install pillow
```
Fourth, run the script passing the file as an argument:

```bash
python script.py databases.txt
```

## Warning:
Only do this if you know what you're doing! And only do this if you're on a safe computer! And know how to
store these codes in a safe manner.

Doing this is very useful if you wanna transfer the data from the authenticator of and old device to a new device, or use the same codes one multiple devices. But, not being careful with the code, reduce the security bonus that 2FA provides.

And, be aware that if you lose access to a device that contains these codes, it is advisable
that you disable them and generate new ones.
