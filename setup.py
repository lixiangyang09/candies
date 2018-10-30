# coding:utf-8

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements

install_reqs = parse_requirements('requirements.txt', session='hack')
requirements = [str(ir.req) for ir in install_reqs]

setup(
        name='candies',     # 包名字
        version='0.1.0',   # 包版本
        description='This package is some common used functions, class',   # 简单描述
        author='Xiangyang.Li',  # 作者
        include_package_data=True,
        author_email='xiangyang_li@qq.com',  # 作者邮箱
        url='',      # 包的主页
        packages=['candies'],                 # 包
        install_requires=requirements,
        zip_safe=False,
        package_data={'candies': ['data/test_data']},
)

