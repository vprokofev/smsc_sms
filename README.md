# smsc_sms.py
Simple script to send SMS via SMSC.RU service.  
Don't forget to change credentials!
## usage
```
$ python3 smsc_sms.py -h
usage: smsc_sms.py [-h] [-d] PHONES MESSAGE

positional arguments:
  PHONES       phone numbers list in E.123 format, comma separated
  MESSAGE      message

optional arguments:
  -h, --help   show this help message and exit
  -d, --debug  enable debug logging
```
