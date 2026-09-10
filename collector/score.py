# 점수 계산
import pandas as pd


# clean CSV 불러오기
df = pd.read_csv('data/raw/glowpick_20260906_clean.csv')


# 순위 상승폭 점수 계산
def calc_rank_change_score(rank_change_value, max_rank_change):
    if rank_change_value <= 0:
        score = 0
    else:
        score = round(
            rank_change_value / max_rank_change * 40,
            2
        )

    return score


# 현재 순위 점수 계산
def calc_current_rank_score(current_rank):
    rank = round(
        (20 - current_rank) / 19 * 30,
        2
    )

    return rank


# 평점 점수 계산
def calc_rating_score(rating, min_rating, max_rating):
    rat = round(
        (rating - min_rating)
        / (max_rating - min_rating)
        * 30,
        2
    )

    return rat


# 카테고리별 점수 계산
def calculate_score(df):

    result_list = []

    # 카테고리별로 데이터 분리
    for category_id, category_df in df.groupby('category_id'):

        category_df = category_df.copy()

        # 해당 카테고리 기준값
        max_rank_change = max(category_df['rank_change_value'])
        max_rating = max(category_df['rating'])
        min_rating = min(category_df['rating'])


        # 순위 상승폭 점수
        rank_change_scores = []

        for i in range(len(category_df)):
            row = category_df.iloc[i]

            rank_change_value = row['rank_change_value']

            score = calc_rank_change_score(
                rank_change_value,
                max_rank_change
            )

            rank_change_scores.append(score)

        category_df['rank_change_score'] = rank_change_scores


        # 현재 순위 점수
        current_rank_scores = []

        for i in range(len(category_df)):
            row = category_df.iloc[i]

            current_rank = row['current_rank']

            rank = calc_current_rank_score(
                current_rank
            )

            current_rank_scores.append(rank)

        category_df['current_rank_score'] = current_rank_scores


        # 평점 점수
        rating_scores = []

        for i in range(len(category_df)):
            row = category_df.iloc[i]

            rating = row['rating']

            rat = calc_rating_score(
                rating,
                min_rating,
                max_rating
            )

            rating_scores.append(rat)

        category_df['rating_score'] = rating_scores


        # 최종 점수
        category_df['score'] = (
            category_df['rank_change_score']
            + category_df['current_rank_score']
            + category_df['rating_score']
        ).round(2)


        result_list.append(category_df)


    # 카테고리별 계산 결과 다시 합치기
    result_df = pd.concat(result_list)

    # 기존 행 순서 복원
    result_df = result_df.sort_index()

    return result_df


df = calculate_score(df)


df.to_csv(
    'data/raw/glowpick_20260906_clean.csv',
    index=False,
    encoding='utf-8-sig'
)