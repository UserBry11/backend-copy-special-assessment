#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import shutil
import subprocess
import argparse

__author__ = "Bryan"


def get_special_paths(from_dir):
    file_directory = os.listdir(from_dir)
    special_files_list = []

    for file in file_directory:

        if re.search(r'\w+__\w+__.\w+', file):
            special_path = os.path.abspath(file)
            special_files_list.append(special_path)

    return special_files_list


def copy_to(src_path_list, todir):

    if todir.startswith("/"):
        todir = todir[1:]

    dst_path = os.path.abspath(todir)

    try:
        os.makedirs(dst_path)
    except OSError:
        print("Format: --todir /yourdirectory\nDirectory May exist already")

    for src in src_path_list:
        shutil.copy(src, dst_path)

    return


def zip_function(special_file_list, to_zip):
    print("Command I'm going to do: zip -j {} {}".format(to_zip,
                                                         special_file_list))

    for each in special_file_list:
        subprocess.call(['zip', '-j', to_zip, each])

    return


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='from directory')
    args = parser.parse_args()

    special_file_list = get_special_paths(args.from_dir)

    if args.todir:
        copy_to(special_file_list, args.todir)

    elif args.tozip:
        zip_function(special_file_list, args.tozip)

    else:
        for special in special_file_list:
            print(special)
        print("\n")


if __name__ == "__main__":
    main()
