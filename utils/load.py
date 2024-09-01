#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : load.py

import json
import os.path


def remove_blank(words_list):
    return_list = []
    for word in words_list:
        if word != '' and word not in return_list:
            return_list.append(word)
    return return_list

def load_words(path):
    _format = os.path.splitext(path)[-1]
    if _format == '.txt':
        with open(path, 'r') as f:
            words = f.read().splitlines()
            return words
    elif _format == '.json':
        with open(path, 'r') as f:
            words = json.load(f)
            return words
    elif _format == '.csv':
        with open(path, 'r') as f:
            words = f.read().splitlines()
            return words
    else:
        raise ValueError('Format is not supported')


if __name__ == '__main__':
    words = load_words('../test/src/word.txt')
    print(words)
    print(remove_blank(words))
