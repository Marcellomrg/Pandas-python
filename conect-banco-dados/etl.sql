SELECT seller_id,
        sum(price) as totalRevenue,
        count(DISTINCT t1.order_id) as qtSalles

FROM tb_order_items as t1

GROUP BY seller_id
