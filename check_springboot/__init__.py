#!/usr/bin/env python
import requests
import sys
import argparse


def check_springboot_service(args):
    try:
        resp = requests.get('http://{0}:{1}/health'.format(args.host, args.port)).json()
    except:
        print ("FAIL!")
        sys.exit(2)

    if resp['status'] == 'UP':
        print ("OK")
        sys.exit(0)
    else:
        print ("FAIL!")
        sys.exit(2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port")
    parser.add_argument("--host")
    args = parser.parse_args()

    check_springboot_service(args)
