SELECT user_transact.user_id, SUM(user_transact.gbp_amount) AS total_spent_gbp
FROM (
  SELECT t.user_id, t.amount*er.rate AS gbp_amount
  FROM transactions AS t, (
    WITH with_pos AS (
      SELECT *, ex_rate.ts as ets, trans.ts as tts, ROW_NUMBER() OVER(PARTITION BY from_currency ORDER BY ex_rate.ts <= trans.ts DESC) AS n
      FROM exchange_rates ex_rate, transactions trans WHERE to_currency = 'GBP'
    )
    SELECT from_currency, rate
    FROM with_pos
    WHERE n = 1
  ) AS er
  WHERE t.currency = er.from_currency

  UNION ALL

  SELECT user_id, amount AS gbp_amount
  FROM transactions
  WHERE currency = 'GBP') AS user_transact
GROUP BY user_transact.user_id ORDER BY user_transact.user_id;
