import pandas as pd
from deep_translator import GoogleTranslator
from korean_romanizer import Romanizer
from korean_romanizer.romanizer import Romanizer as ro


def translate(data):

    languages = {
        'English': 'en',
        'Bengali': 'bn',
        'Nepali': 'ne',
        'Filipino': 'tl',
        'Mongolian': 'mn',
        'Indonesian': 'id'
    }

    # 각 언어로 번역하여 새 칼럼에 추가
    count = 0
    data['Pronunciation'] = data['Korean'].apply(lambda x: Romanizer(x).romanize())
    for lang_name, lang_code in languages.items():
        print(count)
        count += 1
        translator = GoogleTranslator(source='ko', target=lang_code)
        data[f"{lang_name}"] = data['Korean'].apply(lambda x: translator.translate(x))

    data.rename(columns={'Bengali': 'Bangladesh', 'Nepali': 'Nepal', 'Filipino': 'Philippines', 'Mongolian': 'Mongolia', 'Indonesian': 'Indonesia'}, inplace=True)
    return data

def main():
    BoK = 'BoK_1사분기'
    # korean_csv = pd.read_csv(f'korean/korean_words_1124.csv', encoding='utf-8')
    korean_csv = pd.read_csv(f'korean/{BoK}.csv', encoding='utf-8')
    data = translate(korean_csv)

    # print(data['Pronunciation'])
    print(data.columns)

    data.to_csv(f'korean/{BoK}_translated.csv', index=False, encoding='utf-8-sig')


if __name__ == '__main__':
    main()