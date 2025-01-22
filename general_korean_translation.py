from idlelib.pyparse import trans

import pandas as pd
from deep_translator import GoogleTranslator
from korean_romanizer import Romanizer

def translate(data):

    languages = {
        'English': 'en',
        'Bengali': 'bn',
        'Hindi': 'hi',
        'Nepali': 'ne',
        'Filipino': 'tl',
        'Cebuano': 'ceb',
        'Mongolian': 'mn',
        'Spanish': 'es',
        'French': 'fr',
        'Indonesian': 'id',
        'Javanese': 'jw',
        'Uyghur': 'ug',
        'Russian': 'ru'

    }

    # 각 언어로 번역하여 새 칼럼에 추가
    count = 0
    data['Pronunciation'] = data['Korean'].apply(lambda x: Romanizer(x).romanize())
    for lang_name, lang_code in languages.items():
        print(count)
        count += 1
        translator = GoogleTranslator(source='ko', target=lang_code)
        data[f"{lang_name}"] = data['Korean'].apply(lambda x: translator.translate(x))

    return data

def main():
    month_abbr = 'Jan'
    korean_csv = pd.read_csv(f'korean/{month_abbr}_korean_of_the_day.csv', encoding='utf-8')
    data = translate(korean_csv)

    # print(data['Pronunciation'])
    print(len(data.columns))
    # print(data.head())

    data.to_csv(f'korean/{month_abbr}_korean_of_the_day_all.csv', index = False, encoding='utf-8-sig')


if __name__ == '__main__':
    main()