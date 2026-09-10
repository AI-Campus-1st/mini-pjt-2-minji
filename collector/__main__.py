from .crawler import crawl_base, crawl_eye, crawl_lip
from .loader import load_data


import pandas as pd

base_data = crawl_base()
eye_data = crawl_eye()
lip_data = crawl_lip()

all_data = base_data + eye_data + lip_data

df = pd.DataFrame(all_data)
df.to_csv('data/raw/glowpick_20260906.csv', index=False, encoding='utf-8-sig')

load_data()
