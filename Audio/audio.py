#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : audio.py

class Audio:
    def __init__(self, word):
        self.word = word
        self.uk = {"pron": "N/A", "src": "N/A"}
        self.us = {"pron": "N/A", "src": "N/A"}

    def __repr__(self):
        repr_str = self.word + '\n'
        repr_str += f"uk: {str(self.uk)}\n"
        repr_str += f"us: {str(self.us)}\n"
        return repr_str

    def uk_src(self) -> str:
        return self.uk['src']

    def us_src(self) -> str:
        return self.us['src']

    def src(self, loca: str = "uk") -> str:
        if loca == "uk":
            return self.uk_src()
        elif loca == "us":
            return self.us_src()

class Basic:
    def __init__(self, name):
        self.name = name
        self.part_of_speech = []
        self.pronunciation = Audio(name)

    def __repr__(self):
        repr_str = f"{self.name}\n"
        repr_str += f"part_of_speech: {self.part_of_speech}\n"
        repr_str += f"pronunciation: \n"
        repr_str += f"uk_pron: {self.pronunciation.uk['pron']}\n"
        repr_str += f"us_pron: {self.pronunciation.us['pron']}\n"
        return repr_str

