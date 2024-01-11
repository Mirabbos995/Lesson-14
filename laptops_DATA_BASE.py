import psycopg2
from parsing_laptops import data_laptop, product_name, product_price, product_image


laptop_data_base = psycopg2.connect(
    host='john.db.elephantsql.com',
    user='ticbodpx',
    database='ticbodpx',
    password='bi4ui8sReUxmeBaHvViM2e85z9j3UXYh'
)
cursor = laptop_data_base.cursor()

for l in data_laptop:
    name = l["Product_name"]
    price = l["Product_price"]
    img = l["Product_image"]
    cursor.execute(f"""INSERT INTO laptops(name, price, image) values ('{product_name}', '{product_price}', '{product_image}')""")

laptop_data_base.commit()
print(laptop_data_base)


