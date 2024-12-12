from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from pandas import read_csv


# 웹사이트 로그인 및 게시글 작성
def post_to_famigo(df, year, month, date):


    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  # Service 객체 사용
    driver.maximize_window()

    try:
        # www.famigo.net 접속
        driver.get('https://www.famigo.net/login?back_url=LzYx&used_login_btn=N')

        # 로그인 페이지로 이동 (로그인 폼이 메인 페이지에 없으면 적절한 URL로 이동)
        time.sleep(5)

        # 이메일 입력
        email_input = driver.find_element(By.NAME, 'uid')  # 이메일 입력 필드의 ID를 확인 후 수정
        driver.execute_script("arguments[0].value = 'test_fortune@gmail.com';", email_input)
        # email_input.send_keys('test_fortune@gmail.com')
        time.sleep(2)

        # 비밀번호 입력
        password_input = driver.find_element(By.NAME, 'passwd')  # 비밀번호 입력 필드의 ID를 확인 후 수정
        password_input.send_keys('Fortune2025!')
        time.sleep(1)

        # 로그인 버튼 클릭
        login_button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary.btn-block')
        login_button.click()

        # 로그인 완료 대기
        time.sleep(5)

        # 게시글 작성 페이지로 이동
        driver.get('https://famigo.net/32/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&board=b2024043047b9691430dd3&bmode=write&back_url=LzMy')  # 게시글 작성 페이지 URL로 이동

        # 게시글 제목 입력
        title_input = driver.find_element(By.ID, 'post_subject')  # 제목 입력 필드의 ID를 확인 후 수정
        title_input.send_keys(f'[{year} / {month} / {date}] Today’s Fortune Teller')
        time.sleep(2)

        # 게시글 내용 입력
        for i in range(0, 14):
            if i == 0:
                image_upload = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')  # 이미지 업로드 필드의 ID 확인 필요
                image_path = f"automation_fortune_picture/{i}.jpg"  # 업로드할 이미지 경로
                image_upload.send_keys(image_path)
                content_input = driver.find_element(By.CSS_SELECTOR,
                                                    '.fr-element[contenteditable="true"]')
                content_input.send_keys(Keys.RETURN)

                time.sleep(2)
            else:
                image_upload = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')  # 이미지 업로드 필드의 ID 확인 필요
                image_path = f"automation_fortune_picture/{i}.png"  # 업로드할 이미지 경로
                image_upload.send_keys(image_path)
                time.sleep(2)

                if i == 13:
                    break
                else:
                    content_input = driver.find_element(By.CSS_SELECTOR,
                                                    '.fr-element[contenteditable="true"]')  # 내용 입력 필드의 ID를 확인 후 수정
                    content_input.send_keys(Keys.RETURN)
                    content_input.send_keys(df['띠 전체운세'][i*5-1])
                    content_input.send_keys(Keys.RETURN)
                    content_input.send_keys(Keys.RETURN)
                    time.sleep(2)


        # 게시글 등록 버튼 클릭
        post_button = driver.find_element(By.CSS_SELECTOR, 'button._save_post.save_post.btn')
        post_button.click()

        # 완료 대기
        time.sleep(3)

        print("게시글 작성 완료!")

        current_url = driver.current_url
        print(f"새로 생성된 게시글 링크: {current_url}")


    except Exception as e:
        print(f"오류 발생: {e}")

    finally:
        # 브라우저 닫기
        driver.quit()

def main():
    today = 1213
    year = 2024
    month = int(today / 100)
    date = int(today%100)
    df = read_csv(f'korean/오늘의 운세/12월/{today}.csv', encoding='utf-8')
    post_to_famigo(df, year, month, date)


if __name__ == '__main__':
    main()
