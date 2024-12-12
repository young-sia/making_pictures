import pandas as pd
from deep_translator import GoogleTranslator

df = pd.read_csv('korean/amigo article_11_27.csv', encoding = 'utf-8')

languages = {
    'Bengali': 'bn',
    'Nepali': 'ne',
    'Filipino': 'tl',
    'Mongolian': 'mn',
    'Indonesian': 'id'
}

# 각 언어로 번역하여 새 칼럼에 추가
count = 0
for lang_name, lang_code in languages.items():
    print(count)
    count += 1
    translator = GoogleTranslator(source='en', target=lang_code)
    df[f"{lang_name}"] = df['English'].apply(lambda x: translator.translate(x))


df.to_csv("korean/amigo article_11_27.csv", index=False, encoding='utf-8-sig')