-- 분석용 데이터 생성 SQL
SELECT *
FROM tb_ranking
ORDER BY SCORE DESC;

-- 테이블 조인 
SELECT p.product_id,
    p.category_id,
    p.brand,
    p.name,
    r.current_rank,
    r.previous_rank,
    r.rank_change,
    r.rating,
    r.review_count,
    r.price,
    r.score
FROM tb_product p
JOIN tb_ranking r ON p.product_id = r.product_id
ORDER BY p.category_id, r.score DESC;

-- 현재 순위 확인
SELECT p.product_id,
    p.category_id,
    p.brand,
    p.name,
    r.current_rank,
    r.previous_rank,
    r.rank_change,
    r.rating,
    r.review_count,
    r.price,
    r.score
FROM tb_product p
JOIN tb_ranking r ON p.product_id = r.product_id
ORDER BY p.category_id, r.current_rank;

-- 상승 상품, 상승 폭 확인
SELECT 
    p.category_id,
    p.brand,
    p.name,
    r.current_rank,
    r.previous_rank,
    r.rank_change
FROM tb_product p
JOIN tb_ranking r ON p.product_id = r.product_id
WHERE r.rank_change > 0
ORDER BY r.rank_change DESC;

-- 평점을 기준으로 
SELECT 
    p.category_id,
    p.brand,
    p.name,
    r.rating
FROM tb_product p
JOIN tb_ranking r ON p.product_id = r.product_id
WHERE r.rank_change > 0
ORDER BY r.rating DESC;

-- score을 기준으로 (전체)
SELECT
    p.category_id,
    p.brand,
    p.name,
    r.score
FROM tb_product p
JOIN tb_ranking r ON p.product_id = r.product_id
WHERE r.rank_change > 0
ORDER BY r.score DESC;

-- score을 기준으로 (카테고리 별로)
SELECT
    p.category_id,
    p.brand,
    p.name,
    r.current_rank,
    r.previous_rank,
    r.rank_change,
    r.score
FROM tb_product p
JOIN tb_ranking r ON p.product_id = r.product_id
WHERE r.rank_change > 0
ORDER BY p.category_id, r.score DESC;

-- top 5 선정
SELECT
    p.category_id,
    p.brand,
    p.name,
    r.current_rank,
    r.previous_rank,
    r.rank_change,
    r.score
FROM tb_product p
JOIN tb_ranking r ON p.product_id = r.product_id
WHERE r.rank_change > 0
ORDER BY r.score DESC limit 5;