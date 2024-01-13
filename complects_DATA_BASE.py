import psycopg2
from complects_parsing import complects_Base


complects_data_base = psycopg2.connect(
    host='john.db.elephantsql.com',
    user='ticbodpx',
    database='ticbodpx',
    password='bi4ui8sReUxmeBaHvViM2e85z9j3UXYh'
)
cursor = complects_data_base.cursor()


for complect in complects_Base:
    product_name = complect["Complects_name"]
    product_price = complect["Complects_price"]
    product_image = complect["Complects_image"]
    cursor.execute(f"""INSERT INTO complects(name, price, image) values ('{product_name}', '{product_price}', '{product_image}')""")

complects_data_base.commit()
