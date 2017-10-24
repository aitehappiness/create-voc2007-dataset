# -*- coding: utf-8 -*-

import argparse
import urllib
from os.path import basename, join, exists


def fetchimg(labelxjson, savedir):
    with open(labelxjson) as json_f:
        line = json_f.readline()
        count = 0
        while line:
            url = eval(line.rstrip('\n'))['url']
            count += 1
            if exists(join(savedir, basename(url))):
                print 'exists : %d %s >> %s' % (count, url, join(savedir, basename(url)))
            else:
                urllib.urlretrieve(url, join(savedir, basename(url)))
                print 'fetch ok: %d %s >> %s' % (count, url, join(savedir, basename(url)))

            line = json_f.readline()


def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='fetch img by labelx json list')
    parser.add_argument('--jsonlist',
                        dest='jsonlist',
                        help='labelx json list',
                        type=str)

    parser.add_argument('--savedir',
                        dest='savedir',
                        help='save dir for img',
                        type=str)

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    fetchimg(args.jsonlist, args.savedir)

    print 'Done'