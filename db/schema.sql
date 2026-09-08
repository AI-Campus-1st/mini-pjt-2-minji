CREATE DATABASE beauty_db;

USE beauty_db;

CREATE TABLE tb_category (
    category_id INT  PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE tb_product (
    product_id INT  PRIMARY KEY,
    category_id INT NOT NULL, 
    brand VARCHAR(100) NOT NULL,
    name VARCHAR(100) NOT NULL,
    UNIQUE uq_product (category_id, brand, name)
);

CREATE TABLE tb_ranking (
    product_id INT NOT NULL,
    update_date DATE NOT NULL,
    current_rank INT NOT NULL,
    previous_rank INT NOT NULL,
    rank_change INT NOT NULL,
    rating DECIMAL(3,2) NOT NULL,
    review_count INT NOT NULL,
    price INT NOT NULL,
    score DECIMAL(5,2) NOT NULL,
    UNIQUE uq_ranking (product_id, update_date)
);

INSERT INTO tb_category(category_id, name)
VALUES
(1, '파운데이션'),
(2, '아이섀도우'),
(3, '립틴트/라커');