#!/usr/bin/env python3
import argparse
from gendiff.core import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str, default='json')
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)
