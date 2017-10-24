# -*- coding: utf-8 -*-

import sys
import os


if __name__ == '__main__':
    jsonname = sys.argv[1]
    labelbyline_list = []
    with open(jsonname) as content:
        line = content.readline()
        while line:
            label = eval(line.rstrip('\n'))
            bbox = label['label']['detect']['general_d']['bbox']
            if bbox:
                for item in bbox:
                    labelbyline = []
                    labelbyline.append(os.path.basename(label['url']))
                    print 'imgname:', os.path.basename(label['url'])
                    labelbyline.append(item['class'].replace(' ', ''))
                    labelbyline.append(str(item['pts'][0][0]))
                    labelbyline.append(str(item['pts'][0][1]))
                    labelbyline.append(str(item['pts'][2][0]))
                    labelbyline.append(str(item['pts'][2][1]))
                    labelbyline_list.append(' '.join(labelbyline))
            line = content.readline()

    r = '\n'.join([line for line in labelbyline_list])
    with open(jsonname+'.labelbyline', 'w+') as f: f.write(r)