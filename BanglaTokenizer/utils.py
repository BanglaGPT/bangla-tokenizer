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

bangla_range = ('\u0980', '\u09FF')
english_range = ('\u0000', '\u007F')

def clean_text(text):
    min_b, max_b = ord(bangla_range[0]), ord(bangla_range[1])
    min_e, max_e = ord(english_range[0]), ord(english_range[1])
    return ''.join(c for c in text if ((min_b <= ord(c) <= max_b) or (min_e <= ord(c) <= max_e)))


def clean_text_bn(text):
    min_b, max_b = ord(bangla_range[0]), ord(bangla_range[1])
    return ''.join(c for c in text if (min_b <= ord(c) <= max_b))
