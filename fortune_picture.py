from PIL import Image, ImageDraw, ImageFont
import os

from pandas import read_csv



def draw_fortune_picture(text1, text2, im, pic_number, date, language):

    draw = ImageDraw.Draw(im)
    word_pt = 29
    word_size = round(word_pt* 4/3, 1)
    y = [249, 307.5, 359, 534.4, 588.6, 640,4]
    texts = [text1, text2]

    if language == 'Bengali':
        font= "font/Mina-Regular.ttf"
        line_len = 27
    elif language == 'Nepali':
        font = "font/Yashomudra-Normal.ttf"
        line_len = 27
    elif language == 'Filipino':
        font = "font/SongMyung-Regular.ttf"
        line_len = 27
    elif language == 'Mongolian':
        font = "font/EBGaramond-Bold.ttf"
        line_len = 30
    elif language == 'English':
        font = "font/NanumSquare_acR.ttf"
        line_len = 30
    elif language == 'Indonesian':
        font = 'font/NotoSans-VariableFont_wdth,wght.ttf'
        line_len = 26
    elif language == 'Russian':
        font = "font/NotoSans-VariableFont_wdth,wght.ttf"
        line_len = 30
    else:
        font = "font/NanumSquare_acR.ttf"
        line_len = 30

    for j in range(2):
        text = texts[j]
        word_len = len(text1.split(' '))
        words = text.split(' ')
        count = 0

        for row in range(int(len(y)/2)):
            one_line = ''
            if row == 2:
                for i in range(word_len):
                    one_line += words[i + count]
                    if (len(one_line) + len(words[i +count + 1]) + 1) > (line_len - 3):
                        one_line += '...'
                        break
                    elif (len(one_line) + len(words[i + count + 1]) + 1) == (line_len - 3):
                        one_line += ' '
                        one_line += words[i +count+ 1]
                        one_line += '...'
                        break
                    else:
                        one_line += ' '
                draw.text((329, y[row+ 3*j]), one_line,
                          font=ImageFont.truetype(font, word_size), fill=(0, 0, 0))
            else:
                for i in range(word_len):
                    one_line += words[i + count]
                    if (len(one_line) + len(words[i +count + 1])) == line_len:
                        count += i + 1
                        break
                    elif (len(one_line) + len(words[i +count+ 1]) + 1) <= line_len:
                        one_line += ' '
                    else:
                        count += i + 1
                        break

                draw.text((329, y[row+ 3*j]), one_line,
                          font=ImageFont.truetype(font, word_size), fill=(0, 0, 0))

    im.save(f"finish_fortune_picture/{language}/{date}_{pic_number}.jpg")


def main():
    start_date = 122
    end_date = 131

    languages = ['English', 'Bengali', 'Nepali', 'Filipino', 'Mongolian', 'Indonesian', 'Russian']

    basic_path = os.getcwd()
    for language in languages:
        try:
            os.mkdir(basic_path + '/finish_fortune_picture/' + f'{language}')
        except:
            pass

    for date in range(start_date, end_date + 1):
        df = read_csv(f'korean/오늘의 운세/1월/{date}.csv', encoding='utf-8')

        for language in languages:

            for zodiac in range(0, 12, 2):
                pic_number = round(zodiac / 2 + 1)
                text1 = df[f'띠 전체운세_{language}'][zodiac * 5 + 1]
                text2 = df[f'띠 전체운세_{language}'][(zodiac + 1) * 5 + 1]

                im = Image.open(f"base_fortune_picture/{pic_number}.jpg")

                draw_fortune_picture(text1, text2, im, pic_number, date, language)

        print(f'done with {date}')


    # print(df.columns)




if __name__ == '__main__':
    main()


