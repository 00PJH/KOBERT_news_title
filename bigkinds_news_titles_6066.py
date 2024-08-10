import pandas as pd

# 원본 CSV 파일 이름
input_csv_file = 'bigkinds_news_only_title.csv'  # 원본 CSV 파일의 경로를 지정하세요.

# 새로 저장할 CSV 파일 이름
output_csv_file = 'bigkinds_news_titles_6066_label0.csv'

# CSV 파일을 데이터프레임으로 읽어들임
df = pd.read_csv(input_csv_file)

# 무작위로 6066개의 샘플을 추출
sample_df = df.sample(n=6066, random_state=1)  # random_state를 지정하면 재현 가능한 결과를 얻을 수 있습니다.

sample_df.rename(columns={'제목': 'title'}, inplace=True)
# label 0으로 지정
sample_df['label'] = 0
# 새 CSV 파일로 저장
sample_df.to_csv(output_csv_file, index=False, encoding='utf-8-sig')  # 인덱스 없이 저장하고, UTF-8 인코딩으로 저장합니다.

print(f"무작위로 6066개의 행을 추출하여 '{output_csv_file}'로 저장했습니다.")
