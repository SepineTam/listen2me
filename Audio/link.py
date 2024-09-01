#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : link.py

import time
import os

import requests
from bs4 import BeautifulSoup
from requests import RequestException
from requests.exceptions import ProxyError

from Audio.audio import Basic


def scrape_website(url, max_retries=3, delay=5):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/91.0.4472.124 Safari/537.36'
    }

    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()  # 如果状态码不是200，将引发HTTPError异常

            soup = BeautifulSoup(response.text, 'html.parser')

            print(f"成功爬取 {url}")
            return soup

        except ProxyError as e:
            print(f"代理错误: {e}")
            if attempt < max_retries - 1:
                print(f"等待 {delay} 秒后重试...")
                time.sleep(delay)
            else:
                print("达到最大重试次数,放弃爬取")
                return None

        except RequestException as e:
            print(f"请求错误: {e}")
            if attempt < max_retries - 1:
                print(f"等待 {delay} 秒后重试...")
                time.sleep(delay)
            else:
                print("达到最大重试次数,放弃爬取")
                return None


def BASE_URL(word):
    return f"https://dictionary.cambridge.org/zhs/词典/英语-汉语-简体/{word}?q=+{word}"


def basic(block) -> Basic:
    block = BeautifulSoup(str(block), 'html.parser')
    title = block.find_all('div', class_='di-title')[0].text
    basic_info: Basic = Basic(title)

    part_of_speech_div = block.find_all('span', class_='pos dpos')
    for part_of_speech in part_of_speech_div:
        basic_info.part_of_speech.append(part_of_speech.text)

    uk_div = block.find_all('span', class_='uk dpron-i')[0]
    us_div = block.find_all('span', class_='us dpron-i')[0]

    uk_audio_element = uk_div.find('source', type='audio/mpeg')
    uk_mp3_src = uk_audio_element['src']

    us_audio_element = us_div.find('source', type='audio/mpeg')
    us_mp3_src = us_audio_element['src']

    uk_pron = uk_div.find_all('span', class_='pron')[0].text
    us_pron = us_div.find_all('span', class_='pron')[0].text

    basic_info.pronunciation.uk["pron"] = uk_pron
    basic_info.pronunciation.uk["src"] = uk_mp3_src
    basic_info.pronunciation.us["pron"] = us_pron
    basic_info.pronunciation.us["src"] = us_mp3_src

    return basic_info


def link(word, loca: str = "uk") -> str:
    BASE = "https://dictionary.cambridge.org/"
    soup = scrape_website(BASE_URL(word))
    basic_info = basic(soup)
    j_path = basic_info.pronunciation.src(loca=loca)
    return os.path.join(BASE, j_path.lstrip('/'))


if __name__ == '__main__':
    taw = "flask"
    a = link(taw, loca="uk")
    print(a)
