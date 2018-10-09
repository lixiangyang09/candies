# coding:utf-8

from setuptools import setup
# or
# from distutils.core import setup

setup(
        name='candies',     # 包名字
        version='1.0',   # 包版本
        description='This package is some common used functions, class',   # 简单描述
        author='Xiangyang.Li',  # 作者
        author_email='xiangyang_li@qq.com',  # 作者邮箱
        url='',      # 包的主页
        packages=['candies'],                 # 包
        install_requires=[
            'lxml>=4.2.5',
        ]
)

