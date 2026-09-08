# 가격, 리뷰, 순위 등 전처리
import pandas as pd

df = pd.read_csv('../data/raw/glowpick_20260906.csv')

df['price'] = df['price'].str.replace(',', '').str.replace('원', '').astype(int)

def change_rank(rank_change):
    if rank_change == '-':
        return 0
    else:
        return int(rank_change)

df['rank_change_value'] = df['rank_change'].apply(change_rank)
df['previous_rank'] = df['current_rank'] + df['rank_change_value']

df.to_csv(
    '../data/raw/glowpick_20260906_clean.csv',
    index=False,
    encoding='utf-8-sig'
)
