#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : down.py

import os
import requests


def get_audio(url, ROOT, name, loca='uk'):
    ROOT = os.path.join(ROOT, loca)
    os.makedirs(ROOT, exist_ok=True)

    if not name.endswith('.mp3'):
        name += ".mp3"

    if os.path.exists(os.path.join(ROOT, name)):
        file_name = os.path.abspath(os.path.join(ROOT, name))
        print(f"{name} is exist, download next one")
        return file_name, True
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15'
    }
    response = requests.get(url, stream=True, timeout=10, headers=headers)

    if response.status_code == 200:
        if not name.endswith('.mp3'):
            name += ".mp3"
        file_name = os.path.abspath(os.path.join(ROOT, name))

        print(f"Saving {name}")
        with open(file_name, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)

        print(f'file saved at {file_name}')
        return file_name, False

    else:
        print(f'error: {response.status_code}')
