#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : safe.py

import time
import random


def safe_time():
    return 1 + 0.9 * random.randint(1, 10)

def spy_time():
    return random.random()

def sleep(t=2, mode="sleep"):
    if mode == "safe":
        time.sleep(safe_time())
    elif mode == "sleep":
        time.sleep(t)
    elif mode == "spy":
        time.sleep(spy_time())
    elif mode == "inner":
        time.sleep(t)

def is_sleep(flag, t=2, mode="sleep"):
    if flag:
        sleep(t=t, mode=mode)


if __name__ == '__main__':
    print(safe_time())
