# BangaTokenizer

The purpose of this project is to tokenize Bangla text for BanglaGPT model. This is a tokenizer was trained on large corpus (>16GB) of bangla text data.

### Usage
Install the tokenizer using
```
pip install git+https://github.com/BanglaGPT/bangla-tokenizer.git
```

Python code for tokenization
``` python
from BanglaTokenizer import Tokenizer

text = "কফি হাউসের সেই আড্ডাটা আজ আর নেই’ বলে  বাঙালির যে চিরন্তন হা-হুতাশ, সে সম্পর্কে আমরা কমবেশি সবাই ওয়াকিফহাল।"
tokenizer = Tokenizer()
tokz_text = tokenizer.encode(text)
print(tokz_text.ids)

# Decoding
text_d = tokenizer.decode(tokz_text.ids)
print(text_d)
```

See `BanglaTokenizer/out/tokens.csv` for trained tokens and ids. 

# Training
The tokenizer comes with a pretrained version. For general use you don't need to train it. But if you really want to train it on your own data use the following commands.
``` python
from BanglaTokenizer import Tokenizer
tokenizer = Tokenizer()

tokenizer.train(
  files=<path_to_text_files>,
  vocab_size=<your_vocabulary_size>,
  min_frequency=<minimum_no_of_frequency>, 
  special_tokens=<list_of_special_tokens>
)

tokenizer.save_model("<path>", "<tokenizer_name>")
```

# License
Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)


