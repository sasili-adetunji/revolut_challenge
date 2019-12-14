SELECT ft.user_id, SUM(ft.gbp_amount) as total_spent_gbp
FROM (
  SELECT t.user_id, t.amount*er.rate AS gbp_amount
  FROM transactions AS t, (
    WITH with_pos AS (
      SELECT *, ROW_NUMBER() OVER(PARTITION BY from_currency ORDER BY ts DESC) AS n
      FROM exchange_rates WHERE to_currency = 'GBP'
    )
    SELECT from_currency, rate, ts
    FROM with_pos
    WHERE n = 1
  ) AS er
  WHERE t.currency = er.from_currency

  UNION ALL

  SELECT user_id, amount AS gbp_amount
  FROM transactions
  WHERE currency = 'GBP') as ft
GROUP BY ft.user_id ORDER BY ft.user_id;





