import collections
import argparse


def argument_parser(args):
    defaults = {
        'hostname': 'localhost',
        'port': '8000'
    }
    parser = argparse.ArgumentParser(description="A standard argument parser",
                                  usage="Run this program with or without arguments",
                                  epilog="And that is coded by KM.")
    parser.add_argument('-H', '--hostname', default=argparse.SUPPRESS)
    parser.add_argument('-p', '--port', default=argparse.SUPPRESS)
    input_args = vars(parser.parse_args(args))
    enabled_args = {k: v for k, v in input_args.items() if v}
    return collections.ChainMap(enabled_args, defaults)

