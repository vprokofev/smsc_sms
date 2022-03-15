#!/usr/bin/env python3

import sys
import logging
import argparse
import requests

URL = "https://smsc.ru/sys/send.php"
# change these
LOGIN = "LOGIN"
PASSWORD = "PASSWORD"

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("phones", metavar="PHONES",
                        help="phone numbers list in E.123 format, comma separated")
    parser.add_argument("message", metavar="MESSAGE",
                        help="message")
    parser.add_argument("-d", "--debug", action="store_true",
                        help="enable debug logging")
    args = parser.parse_args()
    return args


def create_logger(args):
    level=logging.INFO
    if args.debug:
        level=logging.DEBUG
    logger = logging.getLogger(__name__)
    logger.setLevel(level)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(level)
    formatter = logging.Formatter(u"[%(asctime)s] - %(filename)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def send_sms(login, password, phones, message):
    r = requests.get(f"{URL}?login={login}&psw={password}&phones={phones}&mes={message}")
    return r.content


def main():
    args = parse_args()
    log = create_logger(args)
    try:
        log.info(send_sms(LOGIN, PASSWORD, args.phones, args.message))
    except Exception as e:
        log.error(e)

if __name__ == "__main__":
    main()
