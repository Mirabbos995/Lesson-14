import psycopg2
from parsing_laptops import data_laptop


laptop_data_base = psycopg2.connect(
    host='john.db.elephantsql.com',
    user='ticbodpx',
    database='ticbodpx',
    password='bi4ui8sReUxmeBaHvViM2e85z9j3UXYh'
)
cursor = laptop_data_base.cursor()

for laptop in data_laptop:
    product_name = laptop["Product_name"]
    product_price = laptop["Product_price"]
    product_image = laptop["Product_image"]
    cursor.execute(f"""INSERT INTO laptops(name, price, image) values ('{product_name}', '{product_price}', '{product_image}')""")

laptop_data_base.commit()
# print(laptop_data_base)


