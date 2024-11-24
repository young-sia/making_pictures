from turtledemo.penrose import start

from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os


def draw_pic_sentence(korean_csv, im, country, start_date, date, row_count):

    draw=ImageDraw.Draw(im)
    y = [378.4, 524.7]
    small_word = 22
    big_word = 43.6
    middle_word = 22.7

    if country == 'Bangladesh':
        font1= "font/Mina-Regular.ttf"
        font2 = "font/AnekDevanagari-VariableFont_wdth,wght.ttf"
        lang1 = 'Bengali'
        lang2 = 'Hindi'
    elif country == 'Nepal':
        font1 = "font/Yashomudra-Normal.ttf"
        font2 = "font/Mina-Regular.ttf"
        lang1 = 'Nepalese'
        lang2 = 'Bengali'
    elif country == 'Philippines':
        font1 = "font/SongMyung-Regular.ttf"
        font2 = "font/SongMyung-Regular.ttf"
        lang1 = 'Filipino'
        lang2 = 'Cebuano'
    elif country == 'Mongolia':
        font1 = "font/EBGaramond-Bold.ttf"
        font2 = "font/EBGaramond-Bold.ttf"
        lang1 = 'Mongolian'
        lang2 = 'Buryat'
    elif country == 'USA':
        font2 = "font/NotoSans-VariableFont_wdth,wght.ttf"
        font1 = "font/NotoSans-VariableFont_wdth,wght.ttf"
        lang2 = 'Spanish'
        lang1 = 'French'
    elif country == 'Indonesia':
        font2 = 'font/OpenSans-VariableFont_wdth,wght.ttf'
        font1 = 'font/OpenSans-VariableFont_wdth,wght.ttf'
        lang1 = 'Indonesian'
        lang2 = 'Javanese'
    else:
        font1 = "font/SongMyung-Regular.ttf"
        font2 = "font/SongMyung-Regular.ttf"
        lang1 = 'English'
        lang2 = 'English'


    # 한글
    draw.text((237.2, 276.2), korean_csv['Korean'][row_count],
            font=ImageFont.truetype('font/NanumGothic-Bold.ttf', big_word), fill=(255, 255, 255))
    draw.text((191.9, 327.6), f'[{korean_csv['Pronunciation'][row_count]}]',
                font=ImageFont.truetype('font/DMSans-VariableFont_opsz,wght.ttf', middle_word), fill=(255, 255, 255))

    # 1번째 언어
    if country == 'USA':
        draw.text((191.9, ((y[0] + y[1]) / 2 + y[0]) / 2 - small_word / 2 - 10), 'English',
                  font=ImageFont.truetype('font/LibreFranklin-Bold.ttf', small_word), fill=(255, 255, 255))
        draw.text((320.4, ((y[0] + y[1]) / 2 + y[0]) / 2 - small_word / 2 - 10), korean_csv['English'][row_count],
                  font=ImageFont.truetype(font1, small_word), fill=(255, 255, 255))
    else:
        draw.text((191.9, ((y[0] + y[1]) / 2 + y[0])/2 - small_word / 2 - 10), lang1,
                  font=ImageFont.truetype('font/LibreFranklin-Bold.ttf', small_word), fill=(255, 255, 255))
        draw.text((320.4, ((y[0] + y[1]) / 2 + y[0])/2 - small_word / 2 -10), korean_csv[lang1][row_count],
                  font=ImageFont.truetype(font1, small_word), fill=(255, 255, 255))

    # 2번째 언어
    draw.text((191.9, (y[0] + y[1])/2 - small_word/2 ), lang2,
              font=ImageFont.truetype('font/LibreFranklin-Bold.ttf', small_word), fill=(255, 255, 255))
    draw.text((320.4, (y[0] + y[1]) / 2 - small_word / 2), korean_csv[lang2][row_count],
              font=ImageFont.truetype(font2, small_word), fill=(255, 255, 255))

    # 영어
    if country == 'USA':
        draw.text((191.9, ((y[0] + y[1]) / 2 + y[1]) / 2 - small_word / 2 + 10), lang1,
                  font=ImageFont.truetype('font/LibreFranklin-Bold.ttf', small_word), fill=(255, 255, 255))
        draw.text((320.4, ((y[0] + y[1]) / 2 + y[1]) / 2 - small_word / 2 + 10), korean_csv[lang1][row_count],
                  font=ImageFont.truetype('font/Roboto-Medium.ttf', small_word), fill=(255, 255, 255))
    else:
        draw.text((191.9, ((y[0] + y[1]) / 2 + y[1])/2 - small_word / 2 + 10), 'English',
                  font=ImageFont.truetype('font/LibreFranklin-Bold.ttf', small_word), fill=(255, 255, 255))
        draw.text((320.4, ((y[0] + y[1]) / 2 + y[1])/2 - small_word / 2+ 10), korean_csv['English'][row_count],
                  font=ImageFont.truetype('font/Roboto-Medium.ttf', small_word), fill=(255, 255, 255))

    im.save(f"finish_picture_sentence/{country}_{start_date}/{country}_{date}.png")
    print(f'done with {country}_{date}.png')
    # im.show()

def main():
    korean_csv = pd.read_csv('korean/Nov_Korean_of_the_day_alls .csv', encoding='utf-8')

    row_length = len(korean_csv)
    # start_date = int(input('시작하는 날짜는?(예: 1101 = 11월 1일)'))
    # country = input('페이스북에 게시할 국가는?(Bangladesh, Nepal, Philippines, Mongolia)')
    # interval = int(input("페이스북 게시 간격은?(숫자만)"))
    start_date = 1102
    country = 'Indonesia'
    working_days = 29

    basic_path = os.getcwd()

    try:
        os.mkdir(basic_path + '/finish_picture_sentence/'+f'{country}_{start_date}')
    except:
        pass

    for date in range(start_date, start_date+working_days):

        row_num = date - start_date
        im = Image.open(f"base_picture_sentence/2024_11/{date}.png")
        # width, height = im.size
        # print(f"Image width: {width}, Image height: {height}")
        draw_pic_sentence(korean_csv, im, country, start_date, date, row_num)

if __name__ == '__main__':
    main()
