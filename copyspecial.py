#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import shutil
import subprocess
import argparse

__author__ = "Bryan"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='from directory')
    args = parser.parse_args()

    file_directory = os.listdir(args.from_dir)
    
    if args.todir:     
        dst_path = os.getcwd() + args.todir
        src_path = os.getcwd()
        try:
            shutil.copytree(src_path, dst_path)
        except:
            print("Format: --todir /yourdirectory\nDirectory and/or file(s) May exist already")

        return

    elif args.tozip:
        subprocess.call(['zip', '-r', args.tozip, args.from_dir])
        print("Command I'm going to do: zip -r {} {}".format(args.tozip, args.from_dir))
        return


    for file in file_directory:

        file_path = os.path.abspath(file)
        print(file_path)


if __name__ == "__main__":
    main()
