from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

from pandas import read_csv


def draw_fortune_picture(text1, text2, im, language, pic_number):

    draw = ImageDraw.Draw(im)
    word_pt = 29
    word_size = round(word_pt* 4/3, 1)
    y = [249, 307.5, 359, 534.4, 588.6, 640,4]
    texts = [text1, text2]

    for j in range(2):
        text = texts[j]
        word_len = len(text1.split(' '))
        words = text.split(' ')
        line_len = 30
        count = 0

        for row in range(int(len(y)/2)):
            one_line = ''
            if row == 2:
                for i in range(word_len):
                    one_line += words[i + count]
                    if (len(one_line) + len(words[i + 1]) + 1) > (line_len - 3):
                        one_line += '...'
                        break
                    elif (len(one_line) + len(words[i + 1]) + 1) == (line_len - 3):
                        one_line += ' '
                        one_line += words[i + 1]
                        one_line += '...'
                        break
                    else:
                        one_line += ' '
                draw.text((329, y[row+ 3*j]), one_line,
                          font=ImageFont.truetype("font/NanumSquare_acR.ttf", word_size), fill=(0, 0, 0))
            else:
                for i in range(word_len):
                    one_line += words[i + count]
                    if (len(one_line) + len(words[i + 1]) + 1) > line_len:
                        count += i + 1
                        break
                    else:
                        one_line += ' '
                draw.text((329, y[row+ 3*j]), one_line,
                          font=ImageFont.truetype("font/NanumSquare_acR.ttf", word_size), fill=(0, 0, 0))

    im.save(f"finish_fortune_picture/{language}_{pic_number}.png")


def main():
    df = read_csv('fortune.csv', encoding='utf-8')

    language = 'English'
    # print(df.columns)

    for zodiac in range(0, 12, 2):
        pic_number = round(zodiac/2 + 1)
        text1 = df[f'띠 전체운세_{language}'][zodiac*5+1]
        text2 = df[f'띠 전체운세_{language}'][(zodiac+1)*5+1]

        im = Image.open(f"base_fortune_picture/{pic_number}.png")

        draw_fortune_picture(text1, text2, im, language, pic_number)


if __name__ == '__main__':
    main()


