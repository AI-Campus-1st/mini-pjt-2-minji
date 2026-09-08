# 글로우픽 상품 데이터 크롤링

import requests
from bs4 import BeautifulSoup
from config import FOUNDATION_URL, EYESHADOW_URL, LIP_URL

def crawl_base():
    response = requests.get(FOUNDATION_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    result = soup.select('li[class*="newProductListItem"]')
    category_id = 1
    products = []

    for item in result:
        rank = item.select_one('[class*="newProductItemRankNumber"]').get_text(strip=True)
        #rank_change = item.select_one('[class*="newProductItemRankChange"]')
        up_tag = item.select_one('p[class*="newProductItemRankChangeUp"]')
        down_tag = item.select_one('p[class*="newProductItemRankChangeDown"]')
        surgechange_tag = item.select_one('p[class*="newProductItemSurgeChange"]')


        if up_tag is not None:
            rank_change = "+" + up_tag.get_text(strip=True)
        elif down_tag is not None:
            rank_change = "-" + down_tag.get_text(strip=True)
        elif surgechange_tag is not None:
            rank_change = "+" + surgechange_tag.get_text(strip=True)
        else:
            rank_change = "-"
        brand = item.select_one('[class*="newProductItemBrand"]').get_text(strip=True)
        title = item.select_one('[class*="newProductItemTitle"]').get_text(strip=True)
        rating = item.select_one('[class*="newProductItemRatingValue"]').get_text(strip=True)
        review_count = item.select_one('[class*="newProductItemReviewCnt"]').get_text(strip=True)
        review_count = int(
        review_count.replace('·', '')
                .replace('\u2002', '')
                .replace('리뷰', '')
                .replace(',', '')
                .strip()
        )
        price = item.select_one('p[class*="newProductItemPdtInfo"]').text.rsplit("/", 1)[-1].strip()
        date = soup.select_one('[class*="updateDate"]').text.split()[0]
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
    category_id = 2
    response = requests.get(EYESHADOW_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    result = soup.select('li[class*="newProductListItem"]')
    products = []

    for item in result:
        rank = item.select_one('[class*="newProductItemRankNumber"]').get_text(strip=True)
        #rank_change = item.select_one('[class*="newProductItemRankChange"]')
        up_tag = item.select_one('p[class*="newProductItemRankChangeUp"]')
        down_tag = item.select_one('p[class*="newProductItemRankChangeDown"]')
        surgechange_tag = item.select_one('p[class*="newProductItemSurgeChange"]')


        if up_tag is not None:
            rank_change = "+" + up_tag.get_text(strip=True)
        elif down_tag is not None:
            rank_change = "-" + down_tag.get_text(strip=True)
        elif surgechange_tag is not None:
            rank_change = "+" + surgechange_tag.get_text(strip=True)
        else:
            rank_change = "-"
        brand = item.select_one('[class*="newProductItemBrand"]').get_text(strip=True)
        title = item.select_one('[class*="newProductItemTitle"]').get_text(strip=True)
        rating = item.select_one('[class*="newProductItemRatingValue"]').get_text(strip=True)
        review_count = item.select_one('[class*="newProductItemReviewCnt"]').get_text(strip=True)
        review_count = int(
        review_count.replace('·', '')
                .replace('\u2002', '')
                .replace('리뷰', '')
                .replace(',', '')
                .strip()
        )
        price = item.select_one('p[class*="newProductItemPdtInfo"]').text.rsplit("/", 1)[-1].strip()
        date = soup.select_one('[class*="updateDate"]').text.split()[0]
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
    response = requests.get(LIP_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    result = soup.select('li[class*="newProductListItem"]')
    category_id = 3
    products = []

    for item in result:
        rank = item.select_one('[class*="newProductItemRankNumber"]').get_text(strip=True)
        #rank_change = item.select_one('[class*="newProductItemRankChange"]')
        up_tag = item.select_one('p[class*="newProductItemRankChangeUp"]')
        down_tag = item.select_one('p[class*="newProductItemRankChangeDown"]')
        surgechange_tag = item.select_one('p[class*="newProductItemSurgeChange"]')


        if up_tag is not None:
            rank_change = "+" + up_tag.get_text(strip=True)
        elif down_tag is not None:
            rank_change = "-" + down_tag.get_text(strip=True)
        elif surgechange_tag is not None:
            rank_change = "+" + surgechange_tag.get_text(strip=True)
        else:
            rank_change = "-"
        brand = item.select_one('[class*="newProductItemBrand"]').get_text(strip=True)
        title = item.select_one('[class*="newProductItemTitle"]').get_text(strip=True)
        rating = item.select_one('[class*="newProductItemRatingValue"]').get_text(strip=True)
        review_count = item.select_one('[class*="newProductItemReviewCnt"]').get_text(strip=True)
        review_count = int(
        review_count.replace('·', '')
                .replace('\u2002', '')
                .replace('리뷰', '')
                .replace(',', '')
                .strip()
        )
        price = item.select_one('p[class*="newProductItemPdtInfo"]').text.rsplit("/", 1)[-1].strip()
        date = soup.select_one('[class*="updateDate"]').text.split()[0]

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
