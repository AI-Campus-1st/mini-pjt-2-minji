# 글로우픽 상품 데이터 크롤링

import time
import requests

from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from .config import FOUNDATION_URL, EYESHADOW_URL, LIP_URL


# 재시도 설정
def make_session(retries=3, backoff=0.5):
    session = requests.Session()

    retry = Retry(
        total=retries,
        backoff_factor=backoff,
        status_forcelist=[429, 500, 502, 503, 504]
    )

    session.mount(
        "https://",
        HTTPAdapter(max_retries=retry)
    )

    return session


session = make_session()


# 공통 요청 함수
def fetch_html(url, sleep=0.3):
    response = session.get(
        url,
        timeout=10
    )

    response.raise_for_status()

    time.sleep(sleep)

    return response.text


def crawl_base():
    html = fetch_html(FOUNDATION_URL)

    soup = BeautifulSoup(
        html,
        'html.parser'
    )

    result = soup.select(
        'li[class*="newProductListItem"]'
    )

    category_id = 1
    products = []

    for item in result:
        rank = item.select_one(
            '[class*="newProductItemRankNumber"]'
        ).get_text(strip=True)

        up_tag = item.select_one(
            'p[class*="newProductItemRankChangeUp"]'
        )

        down_tag = item.select_one(
            'p[class*="newProductItemRankChangeDown"]'
        )

        surgechange_tag = item.select_one(
            'p[class*="newProductItemSurgeChange"]'
        )

        if up_tag is not None:
            rank_change = "+" + up_tag.get_text(strip=True)

        elif down_tag is not None:
            rank_change = "-" + down_tag.get_text(strip=True)

        elif surgechange_tag is not None:
            rank_change = "+" + surgechange_tag.get_text(strip=True)

        else:
            rank_change = "-"

        brand = item.select_one(
            '[class*="newProductItemBrand"]'
        ).get_text(strip=True)

        title = item.select_one(
            '[class*="newProductItemTitle"]'
        ).get_text(strip=True)

        rating = item.select_one(
            '[class*="newProductItemRatingValue"]'
        ).get_text(strip=True)

        review_count = item.select_one(
            '[class*="newProductItemReviewCnt"]'
        ).get_text(strip=True)

        review_count = int(
            review_count
            .replace('·', '')
            .replace('\u2002', '')
            .replace('리뷰', '')
            .replace(',', '')
            .strip()
        )

        price = item.select_one(
            'p[class*="newProductItemPdtInfo"]'
        ).text.rsplit("/", 1)[-1].strip()

        date = soup.select_one(
            '[class*="updateDate"]'
        ).text.split()[0]

        product = {
            'category_id': category_id,
            'current_rank': rank,
            'rank_change': rank_change,
            'brand': brand,
            'product_name': title,
            'rating': rating,
            'review_count': review_count,
            'price': price,
            'update_date': date
        }

        products.append(product)

    return products


def crawl_eye():
    html = fetch_html(EYESHADOW_URL)

    soup = BeautifulSoup(
        html,
        'html.parser'
    )

    result = soup.select(
        'li[class*="newProductListItem"]'
    )

    category_id = 2
    products = []

    for item in result:
        rank = item.select_one(
            '[class*="newProductItemRankNumber"]'
        ).get_text(strip=True)

        up_tag = item.select_one(
            'p[class*="newProductItemRankChangeUp"]'
        )

        down_tag = item.select_one(
            'p[class*="newProductItemRankChangeDown"]'
        )

        surgechange_tag = item.select_one(
            'p[class*="newProductItemSurgeChange"]'
        )

        if up_tag is not None:
            rank_change = "+" + up_tag.get_text(strip=True)

        elif down_tag is not None:
            rank_change = "-" + down_tag.get_text(strip=True)

        elif surgechange_tag is not None:
            rank_change = "+" + surgechange_tag.get_text(strip=True)

        else:
            rank_change = "-"

        brand = item.select_one(
            '[class*="newProductItemBrand"]'
        ).get_text(strip=True)

        title = item.select_one(
            '[class*="newProductItemTitle"]'
        ).get_text(strip=True)

        rating = item.select_one(
            '[class*="newProductItemRatingValue"]'
        ).get_text(strip=True)

        review_count = item.select_one(
            '[class*="newProductItemReviewCnt"]'
        ).get_text(strip=True)

        review_count = int(
            review_count
            .replace('·', '')
            .replace('\u2002', '')
            .replace('리뷰', '')
            .replace(',', '')
            .strip()
        )

        price = item.select_one(
            'p[class*="newProductItemPdtInfo"]'
        ).text.rsplit("/", 1)[-1].strip()

        date = soup.select_one(
            '[class*="updateDate"]'
        ).text.split()[0]

        product = {
            'category_id': category_id,
            'current_rank': rank,
            'rank_change': rank_change,
            'brand': brand,
            'product_name': title,
            'rating': rating,
            'review_count': review_count,
            'price': price,
            'update_date': date
        }

        products.append(product)

    return products


def crawl_lip():
    html = fetch_html(LIP_URL)

    soup = BeautifulSoup(
        html,
        'html.parser'
    )

    result = soup.select(
        'li[class*="newProductListItem"]'
    )

    category_id = 3
    products = []

    for item in result:
        rank = item.select_one(
            '[class*="newProductItemRankNumber"]'
        ).get_text(strip=True)

        up_tag = item.select_one(
            'p[class*="newProductItemRankChangeUp"]'
        )

        down_tag = item.select_one(
            'p[class*="newProductItemRankChangeDown"]'
        )

        surgechange_tag = item.select_one(
            'p[class*="newProductItemSurgeChange"]'
        )

        if up_tag is not None:
            rank_change = "+" + up_tag.get_text(strip=True)

        elif down_tag is not None:
            rank_change = "-" + down_tag.get_text(strip=True)

        elif surgechange_tag is not None:
            rank_change = "+" + surgechange_tag.get_text(strip=True)

        else:
            rank_change = "-"

        brand = item.select_one(
            '[class*="newProductItemBrand"]'
        ).get_text(strip=True)

        title = item.select_one(
            '[class*="newProductItemTitle"]'
        ).get_text(strip=True)

        rating = item.select_one(
            '[class*="newProductItemRatingValue"]'
        ).get_text(strip=True)

        review_count = item.select_one(
            '[class*="newProductItemReviewCnt"]'
        ).get_text(strip=True)

        review_count = int(
            review_count
            .replace('·', '')
            .replace('\u2002', '')
            .replace('리뷰', '')
            .replace(',', '')
            .strip()
        )

        price = item.select_one(
            'p[class*="newProductItemPdtInfo"]'
        ).text.rsplit("/", 1)[-1].strip()

        date = soup.select_one(
            '[class*="updateDate"]'
        ).text.split()[0]

        product = {
            'category_id': category_id,
            'current_rank': rank,
            'rank_change': rank_change,
            'brand': brand,
            'product_name': title,
            'rating': rating,
            'review_count': review_count,
            'price': price,
            'update_date': date
        }

        products.append(product)

    return products