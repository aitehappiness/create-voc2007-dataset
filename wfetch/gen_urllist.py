# -*- coding: utf-8 -*-

import argparse
import os
from os.path import basename, join, exists


def gen_urllist(labelxjson, vocpath):
    savedir = join(vocpath, 'JPEGImages')
    if not exists(savedir):
        os.mkdir(savedir)
    urllist = []
    with open(labelxjson) as json_f:
        line = json_f.readline()
        while line:
            url = eval(line.rstrip('\n'))['url']
            urllist.append(url)
            line = json_f.readline()

    r = '\n'.join(urllist)
    with open(labelxjson+'.urllist', 'w+') as f: f.write(r)


def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='fetch img by labelx json list')
    parser.add_argument('--in',
                        dest='jsonlist',
                        help='labelx json list',
                        type=str)

    parser.add_argument('--vocpath',
                        dest='vocpath',
                        help='path to your voc datasets',
                        type=str)

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    gen_urllist(args.jsonlist, args.vocpath)

    print 'Done'