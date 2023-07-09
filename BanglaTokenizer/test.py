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
from BanglaTokenizer import Tokenizer
import pandas as pd
from utils import clean_text


text = "কফি হাউসের সেই আড্ডাটা আজ আর নেই’ বলে  বাঙালির যে চিরন্তন হা-হুতাশ, সে সম্পর্কে আমরা কমবেশি সবাই ওয়াকিফহাল।"
print("Cleaned: ", clean_text(text))

tokenizer = Tokenizer()
tokz_text = tokenizer.encode(text)
for i in tokz_text.ids:
    print(tokenizer.decode([i]))
print(tokz_text.ids)

# Save all token to csv
d = []
for i in range(52000):
    token = tokenizer.decode([i])
    d.append({"Token ID": i, "Token": token})
pd.DataFrame(d).to_csv('./out/tokens.csv', index=False)

