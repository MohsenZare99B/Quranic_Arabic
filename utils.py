def smart_print(text, length=70):
    words = text.split()
    line = ''
    for word in words:
        if len(line) + len(word) + 1 <= length:
            line += word + ' '
        else:
            print(line)
            line = word + ' '
    print(line.strip())

import json
import random

def random_verse(Surah=-1, Ayah_range=None):
    # Reading JSON data from a file
    with open('quran_en.json', 'r') as file:
        data = json.load(file)
    if Surah == -1:
        Surah = random.randint(0, 113)
    else:
        Surah -= 1
    if Ayah_range:
        a, b = Ayah_range
        if Ayah_range[0] < 0:
            a += len(data[Surah]["verses"]) + 1
        if Ayah_range[1] < 0:
            b += len(data[Surah]["verses"]) + 1
        if b > len(data[Surah]["verses"]):
            b = len(data[Surah]["verses"])
        Ayah = random.randint(a - 1, b - 1)
    else:
        Ayah = random.randint(0, len(data[Surah]["verses"])-1)
    return  data[Surah]["name"], Ayah+1, data[Surah]["verses"][Ayah]["text"], data[Surah]["verses"][Ayah]["translation"]

def get_verse(Surah, Ayah_range=(1, -1)):
    # Reading JSON data from a file
    with open('quran_en.json', 'r') as file:
        data = json.load(file)
    Surah -= 1
    a, b = Ayah_range
    if Ayah_range[0] < 0:
        a += len(data[Surah]["verses"]) + 1
    if Ayah_range[1] < 0:
        b += len(data[Surah]["verses"]) + 1
    if b > len(data[Surah]["verses"]):
        b = len(data[Surah]["verses"])
    verses = []
    for i in range(a-1, b):
        verses.append({
            "text": data[Surah]["verses"][i]["text"],
            "translation": data[Surah]["verses"][i]["translation"],
            "number": f'({i+1})'})

    return verses