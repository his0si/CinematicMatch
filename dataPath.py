import pandas as pd
import ast

# 파일 경로 설정
movies_metadata_path = 'D:\\_Code\\CinematicMatch\\TheMoviesDataset\\movies_metadata.csv'
ratings_path = 'D:\\_Code\\CinematicMatch\\TheMoviesDataset\\ratings_small.csv'

# 영화 메타데이터 로드
movies_df = pd.read_csv(movies_metadata_path, low_memory=False)

# 사용자들의 영화 평점 데이터를 로드
ratings_df = pd.read_csv(ratings_path)

# 영화 메타데이터에서 분석에 필요한 열만 선택
movies_df = movies_df[['id', 'title', 'genres', 'vote_average', 'vote_count', 'popularity']]

# id 컬럼을 숫자로 변환 (오류 발생 시 NaN으로 처리)
movies_df['id'] = pd.to_numeric(movies_df['id'], errors='coerce')

# id 값이 NaN인 행을 제거
movies_df = movies_df.dropna(subset=['id'])

# genres 컬럼을 리스트 형식으로 변환 (JSON 문자열을 파이썬 리스트로 변환)
movies_df['genres'] = movies_df['genres'].apply(lambda x: [genre['name'] for genre in ast.literal_eval(x)] if pd.notnull(x) else [])

# ratings 데이터의 movieId와 movies 데이터의 id를 기준으로 병합
movies_ratings_df = pd.merge(ratings_df, movies_df, left_on='movieId', right_on='id')

# 병합된 데이터프레임 확인
print(movies_ratings_df.head())