CREATE SCHEMA IF NOT EXISTS converter;

SET TIME ZONE 'America/Sao_Paulo';

CREATE TABLE IF NOT EXISTS converter.currency (id integer, alphabetic_code text, numeric_code numeric, name text, symbol text);

INSERT INTO converter.currency(id, alphabetic_code, numeric_code, name, symbol)
VALUES (1, 'BRL', 986, 'Brazilian Real', 'R$'),
       (2, 'EUR', 978, 'Euro', '€'),
       (3, 'INR', 356, 'Indian Rupee', '₹'),
       (4, 'USD', 840, 'US Dollar', '$');


CREATE TABLE IF NOT EXISTS converter.exchange_rate(id integer, currency_from_id integer, currency_to_id integer, date_rate timestamp, rate numeric);

INSERT INTO converter.exchange_rate(id, currency_from_id, currency_to_id, date_rate, rate)
VALUES (5687, 1, 4, CURRENT_TIMESTAMP, 5.395398554413112),
       (5688, 1, 2, CURRENT_TIMESTAMP, 6.365481623828969),
       (5689, 1, 3, CURRENT_TIMESTAMP, 0.0724135905111813);
       