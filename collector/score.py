# 점수 계산
import pandas as pd


# clean CSV 불러오기
df = pd.read_csv('../data/raw/glowpick_20260906_clean.csv')


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


# 전체 점수 계산
def calculate_score(df):

    max_rank_change = max(df['rank_change_value'])
    max_rating = max(df['rating'])
    min_rating = min(df['rating'])


    rank_change_scores = []

    for i in range(len(df)):
        row = df.iloc[i]

        rank_change_value = row['rank_change_value']

        score = calc_rank_change_score(
            rank_change_value,
            max_rank_change
        )

        rank_change_scores.append(score)

    df['rank_change_score'] = rank_change_scores

    current_rank_scores = []

    for i in range(len(df)):
        row = df.iloc[i]

        current_rank = row['current_rank']

        rank = calc_current_rank_score(
            current_rank
        )

        current_rank_scores.append(rank)

    df['current_rank_score'] = current_rank_scores


    rating_scores = []

    for i in range(len(df)):
        row = df.iloc[i]

        rating = row['rating']

        rat = calc_rating_score(
            rating,
            min_rating,
            max_rating
        )

        rating_scores.append(rat)

    df['rating_score'] = rating_scores


    # 최종 점수
    df['score'] = (
        df['rank_change_score']
        + df['current_rank_score']
        + df['rating_score']
    ).round(2)

    return df

df = calculate_score(df)

df.to_csv(
    '../data/raw/glowpick_20260906_clean.csv',
    index=False,
    encoding='utf-8-sig'
)