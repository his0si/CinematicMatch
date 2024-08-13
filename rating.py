import pandas as pd
import matplotlib
matplotlib.use('TkAgg')  # 또는 'Qt5Agg'
#Matplotlib 백엔드를 명시적으로 설정
import matplotlib.pyplot as plt

# ratings 데이터 로드
ratings_df = pd.read_csv('D:\\_Code\\CinematicMatch\\TheMoviesDataset\\ratings_small.csv')

# 평점 분포 히스토그램 생성
plt.figure(figsize=(10, 6))
plt.hist(ratings_df['rating'], bins=10, edgecolor='black', color='skyblue')
plt.title('Distribution of Movie Ratings')
plt.xlabel('Rating')
plt.ylabel('Number of Ratings')
plt.grid(True)

# 그래프 표시
plt.show()