#/usr/bin/env python
import argparse
import os

from deepascii.main import main


if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='Deep ASCII')
    argparser.add_argument('source_glob')
    argparser.add_argument('--font', default='DroidSansMono.ttf')
    argparser.add_argument('--font-size', type=int, default=13)
    argparser.add_argument('--layer', default='block2_conv1')
    argparser.add_argument('--pool', type=int, default=1)
    argparser.add_argument('--pool-type', default='avg', help='"max" or "avg"')
    argparser.add_argument('--invert-color', action='store_true', help="Switch to black on white text")
    argparser.add_argument('--charset', default=None, help='Text characters to use')
    argparser.add_argument('--columns', type=int, default=80)
    config = argparser.parse_args()
    main(config)
