from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
import hello_korean_translation as translation


def draw_pic(korean_csv, im, language, start_date, date, row_count):

    draw=ImageDraw.Draw(im)
    y = [195.15, 318.55, 441.95, 565.25]
    small_pt = 19.8
    big_pt = 44.7
    small_word = round(small_pt* 4/3, 1)
    big_word = round(big_pt* 4/3, 1)
    # print(small_word, big_word)

    if language == 'Bangladesh':
        font= "font/Mina-Regular.ttf"
    elif language == 'Nepal':
        font = "font/Yashomudra-Normal.ttf"
    elif language == 'Philippines':
        font = "font/SongMyung-Regular.ttf"
    elif language == 'Mongolia':
        font = "font/EBGaramond-Bold.ttf"
    elif language == 'USA':
        font = "font/SongMyung-Regular.ttf"
    elif language == 'Indonesia':
        font = 'font/NotoSans-VariableFont_wdth,wght.ttf'
    else:
        font = "font/SongMyung-Regular.ttf"

    for i in range(row_count, row_count+4):
        y_row = i%4
        draw.text((105.1, y[y_row] - big_word / 2), korean_csv['Korean'][i],
                  font=ImageFont.truetype("font/SongMyung-Regular.ttf", big_word), fill=(255, 255, 255))
        if language == 'USA':
            draw.text((345, y[y_row] - 10 - small_word), f"[{korean_csv['Pronunciation'][i]}]",
                      font=ImageFont.truetype("font/SongMyung-Regular.ttf", small_word), fill=(255, 255, 255))
            draw.text((345, y[y_row] + 10 ), korean_csv['English'][i],
                      font=ImageFont.truetype("font/SongMyung-Regular.ttf", small_word), fill=(255, 255, 255))
        else:
            draw.text((345, y[y_row] - small_word / 2 * 3 - 11), f"[{korean_csv['Pronunciation'][i]}]",
                      font=ImageFont.truetype("font/SongMyung-Regular.ttf", small_word), fill=(255, 255, 255))
            draw.text((345, y[y_row] - small_word / 2), korean_csv['English'][i],
                      font=ImageFont.truetype("font/SongMyung-Regular.ttf", small_word), fill=(255, 255, 255))
            draw.text((345, y[y_row] + small_word / 2 + 11), korean_csv[language][i],
                      font=ImageFont.truetype(font, (small_word* 7/ 8)), fill=(255, 255, 255))

    im.save(f"finish_picture_words/{language}_{start_date}/{language}_{date}.png")
    # im.show()

def main():
    korean_csv = pd.read_csv('korean/korean_words_1124.csv', encoding='utf-8')


    row_length = len(korean_csv)
    # start_date = int(input('시작하는 날짜는?(예: 1101 = 11월 1일)'))
    # country = input('페이스북에 게시할 국가는?(Bangladesh, Nepal, Philippines, USA)')
    # interval = int(input("페이스북 게시 간격은?(숫자만)"))
    korean_csv = translation.translate(korean_csv)

    print('translation done')

    start_date = 1124

    countries = ['USA', 'Bangladesh', 'Nepal', 'Philippines', 'Mongolia', 'Indonesia']
    # country = 'USA'
    interval = 2

    for country in countries:
        basic_path = os.getcwd()
        try:
            os.mkdir(basic_path + '/finish_picture_words/' + f'{country}_{start_date}')
        except:
            pass

        for pic_count in range(0, int(row_length / 4)):
            category = korean_csv['Category'][pic_count * 4]
            date = start_date + interval * pic_count

            im = Image.open(f"base_picture_words/{category}.png")
            # width, height = im.size
            # print(f"Image width: {width}, Image height: {height}")
            draw_pic(korean_csv, im, country, start_date, date, pic_count * 4)

        print(f'{country} done')


def test():
    korean_csv = pd.read_csv('korean/korean_words_1124_all.csv', encoding='utf-8')

    row_length = 4
    # start_date = int(input('시작하는 날짜는?(예: 1101 = 11월 1일)'))
    # country = input('페이스북에 게시할 국가는?(Bangladesh, Nepal, Philippines, USA)')
    # interval = int(input("페이스북 게시 간격은?(숫자만)"))
    start_date = 1124

    country = 'Indonesia'

    category = korean_csv['Category'][0]
    date = start_date

    im = Image.open(f"base_picture_words/{category}.png")
    # width, height = im.size
    # print(f"Image width: {width}, Image height: {height}")
    draw_pic(korean_csv, im, country, start_date, date, 0)


if __name__ == '__main__':
    main()
    # test()
