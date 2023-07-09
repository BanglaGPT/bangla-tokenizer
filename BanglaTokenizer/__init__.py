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
from tokenizers import ByteLevelBPETokenizer

class Tokenizer(ByteLevelBPETokenizer):
    def __init__(self, vocab='./out/tokenizer/banglagpt-vocab.json', merges='./out/tokenizer/banglagpt-merges.txt'):
        super().__init__(vocab, merges)


if __name__ == '__main__':
    text = "কফি হাউসের সেই আড্ডাটা আজ আর নেই’ বলে  বাঙালির যে চিরন্তন হা-হুতাশ, সে সম্পর্কে আমরা কমবেশি সবাই ওয়াকিফহাল।"
    tokenizer = Tokenizer()
    
    tokz_text = tokenizer.encode(text)
    decoded = tokenizer.decode(tokz_text.ids)
    print(decoded)
    