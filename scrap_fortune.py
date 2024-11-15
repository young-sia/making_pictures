from bs4 import BeautifulSoup
import pandas as pd
from deep_translator import GoogleTranslator

# HTML 구조를 파싱하고 BeautifulSoup 객체 생성
with open('fortune_teller_txt/2024.11/1102.txt', 'r', encoding='utf-8') as file:
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

# 결과 확인

df = pd.DataFrame(data_list)

languages = {
    'English': 'en',
    'Bengali': 'bn',
    'Nepali': 'ne',
    'Filipino': 'tl',
    'Mongolian': 'mn'
}

# 각 언어로 번역하여 새 칼럼에 추가
count = 0
for lang_name, lang_code in languages.items():
    print(count)
    count += 1
    translator = GoogleTranslator(source='ko', target=lang_code)
    df[f"띠 전체운세_{lang_name}"] = df['띠 전체운세'].apply(lambda x: translator.translate(x))


df.to_csv("fortune.csv", index=False, encoding='utf-8-sig')