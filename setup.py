#! -*- coding: utf-8 -*-
from setuptools import setup

setup(name='zigpe',
      version='0.0.1',
      author='Jihyun Choi',
      author_email='jihychoi00@gmail.com',
      install_requires=[
          'flask==0.12', 'sqlalchemy==1.2',
          'Flask-OAuthlib==0.9.3', 'alembic==0.9.2'
      ])
