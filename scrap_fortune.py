from bs4 import BeautifulSoup
import pandas as pd
from deep_translator import GoogleTranslator
import os

# HTML 구조를 파싱하고 BeautifulSoup 객체 생성
def scrap_fortune(year_month, date):
    with open(f'fortune_teller_txt/{year_month}/{date}.txt', 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, "html.parser")

    # 추출된 데이터를 담을 리스트 초기화
    data_list = []

    # 각 띠별 운세 섹션을 반복하여 데이터 추출
    for ul in soup.find_all("ul", class_="zodi_result"):
        # 띠 이름과 전체 운세 문장 추출
        zodiac = ul.find("b").get_text(strip=True)
        general_fortune = ul.find("p").get_text(strip=True)

        # 연도별 운세 추출
        for li in ul.find_all("li")[1:]:  # 첫 번째 li는 띠에 대한 전체 운세 정보이므로 제외
            year = li.find("span", class_="tit").get_text(strip=True)
            fortune = li.find("p", class_="txt").get_text(strip=True)

            # 추출된 데이터를 딕셔너리로 저장
            data_list.append({"띠": zodiac, "연도": year, "띠 전체운세": general_fortune, "연도별 운세": fortune})

    df = pd.DataFrame(data_list)
    return df



def translate_fortune(df):
    languages = {
        'English': 'en',
        'Bengali': 'bn',
        'Nepali': 'ne',
        'Filipino': 'tl',
        'Mongolian': 'mn',
        'Indonesian': 'id',
        'Russian': 'ru'
    }

    # 각 언어로 번역하여 새 칼럼에 추가
    count = 0
    for lang_name, lang_code in languages.items():
        print(f'translate fortune for {lang_name}')
        count += 1
        translator = GoogleTranslator(source='ko', target=lang_code)
        df[f"띠 전체운세_{lang_name}"] = df['띠 전체운세'].apply(lambda x: translator.translate(x))

    return df

def make_excel(fortune, df, date, count):

    # df.loc[count, 'Date'] = str(date)
    df['Date'] = df['Date'].astype('string')
    df.at[count, 'Date'] = str(date)
    # print(df)
    for i in range(1, 13):
        # df.loc[count, str(i)] = fortune.loc[5*i-1, '띠 전체운세']
        df[str(i)] = df[str(i)].astype('string')
        df.at[count, str(i)] = fortune.at[5 * i - 1, '띠 전체운세']
    return df



def main():

    # url = https://unse.daily.co.kr/?p=zodiac&day=20241231#unseback
    year_month = 2025.01
    month = 1
    start_date = 116
    end_date = 131

    df_all = pd.DataFrame({'Date':[], '1':[], '2':[], '3':[], '4':[], '5':[], '6':[], '7':[], '8':[], '9':[],
                           '10':[], '11':[], '12':[]})
    # print(df_all)

    basic_path = os.getcwd()
    # print(basic_path)
    try:
        os.mkdir(basic_path + '/korean/오늘의 운세/' + f'{month}월')
    except:
        pass

    for date in range(start_date, end_date + 1):
        day_fortune = scrap_fortune(year_month, date)
        fortune_csv = translate_fortune(day_fortune)

        df_all = make_excel(day_fortune, df_all, date, (date - start_date))

        fortune_csv.to_csv(f"korean/오늘의 운세/{month}월/{date}.csv", index=False, encoding='utf-8-sig')
        print(f'finished {date}')

    df_all.to_csv(f"korean/오늘의 운세/{month}월.csv", index=False, encoding='utf-8-sig')

if __name__ == '__main__':
    # start_date = 101
    # end_date = 131
    # df_all = pd.DataFrame({'Date':[], '1':[], '2':[], '3':[], '4':[], '5':[], '6':[], '7':[], '8':[], '9':[],
    #                        '10':[], '11':[], '12':[]})
    #
    # for date in range(start_date, end_date + 1):
    #     fortune_csv = pd.read_csv(f'korean/오늘의 운세/1월/{date}.csv', encoding='utf-8')
    #     df_all = make_excel(fortune_csv, df_all, date, date - start_date)
    #
    # df_all.to_csv(f"automation_fortune_picture/data/1월.csv", index=False, encoding='utf-8-sig')

    main()