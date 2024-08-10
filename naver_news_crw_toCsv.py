# import requests
# from bs4 import BeautifulSoup
# import csv
# import time

# # 카테고리별 URL과 이름
# categories = {
#     '정치': '100',
#     '경제': '101',
#     '사회': '102',
#     '생활/문화': '103',
#     'IT/과학': '105',
#     '세계': '104',
# }

# # 결과를 저장할 집합(중복 방지용) 및 리스트 초기화
# news_titles_set = set()
# news_titles_list = []

# # 각 카테고리별로 뉴스 크롤링
# for category_name, category_code in categories.items():
#     page = 1
#     count = 0
    
#     while count < 1011:
#         url = f'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1={category_code}&page={page}'
#         headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        
#         response = requests.get(url, headers=headers)
#         soup = BeautifulSoup(response.text, 'html.parser')
        
#         news_list = soup.select('ul.type06_headline li dl')
        
#         for news in news_list:
#             if count >= 1011:
#                 break
            
#             title = news.select_one('dt:not(.photo) a').get_text().strip()
            
#             # 중복되지 않은 제목만 추가
#             if title not in news_titles_set:
#                 news_titles_set.add(title)
#                 news_titles_list.append([title])
#                 count += 1
        
#         page += 1
#         time.sleep(0.5)  # 서버 부하를 줄이기 위해 약간의 지연을 추가
    
#     print(f"{category_name} 카테고리에서 {count}개의 뉴스 제목을 크롤링했습니다.")

# # CSV 파일로 저장
# with open('naver_news_titles_only.csv', 'w', newline='', encoding='utf-8-sig') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Title'])
#     writer.writerows(news_titles_list)

# print("크롤링 완료 및 CSV 파일 저장 완료.")
import requests
from bs4 import BeautifulSoup
import csv
import time
import tkinter as tk
from tkinter import ttk

# 카테고리별 URL과 이름
categories = {
    '정치': '100',
    '경제': '101',
    '사회': '102',
    '생활/문화': '103',
    'IT/과학': '105',
    '세계': '104',
}

# 결과를 저장할 집합(중복 방지용) 및 리스트 초기화
news_titles_set = set()
news_titles_list = []

# GUI 설정
root = tk.Tk()
root.title("크롤링 진행 상태")
root.geometry("400x250")

# Noto Sans CJK 폰트로 설정
custom_font = ("Noto Sans CJK KR", 12)

label = tk.Label(root, text="크롤링 진행 상태", font=("Noto Sans CJK KR", 14))
label.pack(pady=10)

progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress.pack(pady=10)

status_label = tk.Label(root, text="대기 중...", font=custom_font)
status_label.pack(pady=10)

def start_crawling():
    total_news = 1011 * len(categories)
    progress["maximum"] = total_news
    count_total = 0

    for category_name, category_code in categories.items():
        page = 1
        count = 0
        
        while count < 1011:
            url = f'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1={category_code}&page={page}'
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
            
            try:
                response = requests.get(url, headers=headers)
                response.raise_for_status()  # HTTPError를 발생시킵니다.
                soup = BeautifulSoup(response.text, 'html.parser')
                
                news_list = soup.select('ul.type06_headline li dl')
                
                if not news_list:  # 뉴스가 없으면 종료
                    break
                
                for news in news_list:
                    if count >= 1011:
                        break
                    
                    title_tag = news.select_one('dt:not(.photo) a')
                    if title_tag:
                        title = title_tag.get_text().strip()
                        
                        # 중복되지 않은 제목만 추가
                        if title and title not in news_titles_set:
                            news_titles_set.add(title)
                            news_titles_list.append([title])
                            count += 1
                            count_total += 1

                            # 진행 상태 업데이트
                            progress["value"] = count_total
                            status_label.config(text=f"{category_name}: {count_total}/{total_news}개 수집 완료")
                            root.update_idletasks()
            
                page += 1
                time.sleep(0.3)  # 서버 부하를 줄이기 위해 약간의 지연을 추가
            
            except requests.RequestException as e:
                print(f"요청 오류: {e}")
                break
        
        print(f"{category_name} 카테고리에서 {count}개의 뉴스 제목을 크롤링했습니다.")

    # CSV 파일로 저장
    with open('naver_news_titles_only.csv', 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow(['Title'])
        writer.writerows(news_titles_list)

    status_label.config(text="크롤링 완료 및 CSV 파일 저장 완료.")
    print("크롤링 완료 및 CSV 파일 저장 완료.")

# 시작 버튼 추가
start_button = tk.Button(root, text="크롤링 시작", command=start_crawling, font=custom_font)
start_button.pack(pady=20)

root.mainloop()
