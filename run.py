#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : run.py

from Audio import *
from Audio.play import play_mp3

from utils.load import load_words, remove_blank
from utils.safe import sleep
from utils.sword import clean_word
from utils.emit import remove_directory

import _config


def pre_load():
    ws = remove_blank(load_words(_config.WORDS_BASE))
    path_list = []
    for w in ws:
        a_p, flag = audio(w, _config.SRC_BASE,
                          loca=_config.pron_loca, is_play=_config.is_play)
        path_list.append(a_p)
        print(a_p)
        if not flag:
            sleep(mode="safe")
    return path_list


def play(word_path_list, stop_time: int = 2, times: int = 2):
    count = 0
    for word_path in word_path_list:
        count += 1
        if _config.is_check:
            if _config.check_position == "before":
                print(clean_word(word_path)[0])

        for i in range(times):
            play_mp3(word_path)
            print(f"Word{count}, \ttime{i+1}")
            if i+1 != times:
                sleep(t=2, mode="inner")
            else:
                sleep(t=stop_time, mode="sleep")

        if _config.is_check:
            if _config.check_position == "after":
                print(clean_word(word_path)[0])


if __name__ == '__main__':
    wp_list = pre_load()
    input("键入回车以开始：")
    play(wp_list, stop_time=2)

    if _config.self_destruct:
        remove_directory(_config.SRC_BASE)
