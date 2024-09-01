#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : sword.py

import os.path


def clean_word(path):
    file_name = os.path.basename(path)
    name, ext = os.path.splitext(file_name)
    return [name, ext]


if __name__ == '__main__':
    print(clean_word("./asda/asdga/agsdf//asg//asgd.csv"))