#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : play.py

import os
import pygame


def play_mp3(file_path):
    file_path = os.path.abspath(file_path)
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    # 等待音频播放完毕
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


if __name__ == '__main__':
    play_mp3('../test/src/hello.mp3')
