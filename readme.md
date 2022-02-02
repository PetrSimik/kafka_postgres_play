Toto je uplny simple example stahovani dat z Kafky a push do postgreSQL databaze
## Pro Kafku 
pip install confluent-kafka

## pro Postgre
pip install psycopg[binary]

## kod
kafka_to_postgres.py

## pozn
Pro simple ulohy one-time job je to pouzitelne 
pro produkci je nutne zajistit
- bulk/batch zpracovani
- osetreni vyjimek
- strukturovat kod do trid/funkci 
- jestli to pobezi jako servisa v kontejneru
- asynchronni pristup
- tuning pro high perf. (dle dokumentace pro confluent a postgresql)

