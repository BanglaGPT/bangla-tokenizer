#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
COPYRIGHT NOTICE

    Copyright (c) 2023, Shamim Ahamed

This file is part of BangaGPT Project.

BangaGPT is free software: you can redistribute it and/or modify it under the 
terms of the  Attribution-NonCommercial-ShareAlike 4.0  International License

You should have received a copy of the License along with 'bangla-tokenizer' 
project, if not Please visit https://github.com/BanglaGPT/bangla-tokenizer.
  
"""
from setuptools import setup

setup(
    name='BanglaTokenizer',
    version='0.1.0',    
    description='A example Python package',
    url='https://github.com/BanglaGPT/bangla-tokenizer',
    author='Shamim Ahamed',
    author_email='mail.sahamed@gmail.com',
    license='Attribution-NonCommercial-ShareAlike 4.0 International',
    packages=['BanglaTokenizer'],
    install_requires=['tokenizers',
                      'tqdm',
                      'datasets',
                      'glob2',
                      'pandas'
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: Attribution-NonCommercial-ShareAlike 4.0 International',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)