#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : emit.py

import os
import shutil


def remove_directory(directory_path):
    try:
        # 检查路径是否存在
        if not os.path.exists(directory_path):
            print(f"错误: 路径 '{directory_path}' 不存在。")
            return False

        # 检查路径是否为目录
        if not os.path.isdir(directory_path):
            print(f"错误: '{directory_path}' 不是一个目录。")
            return False

        # 使用shutil.rmtree()递归删除目录及其所有内容
        shutil.rmtree(directory_path)
        print(f"成功删除目录: '{directory_path}'")
        return True

    except PermissionError:
        print(f"错误: 没有权限删除 '{directory_path}'。")
    except OSError as e:
        print(f"错误: 删除 '{directory_path}' 时发生错误: {e}")

    return False
