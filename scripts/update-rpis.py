#!/usr/bin/env python
#

from __future__ import print_function

import requests
import argparse


def main(server):
    print("# Auto generated by %s" % __file__)
    print('[rpis]')
    r = requests.get("http://%s/providers?json" % server)
    for v in r.json():
        if v.get('present'):
            print(v['ip'])

    print("")
    print('\n'.join([
        '[rpis:vars]',
        'ansible_ssh_user=pi',
        'ansible_ssh_pass=raspberry']))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='generate hosts.ini',
             formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-s', dest='server', default='wifiphone.nie.netease.com', help='atx server url')
    args = parser.parse_args()
    main(args.server)