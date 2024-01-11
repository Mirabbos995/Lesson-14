import psycopg2
from accessory_parsing import accessory_Base, product_image, product_name, product_price

accessory_data_base = psycopg2.connect(
    host='john.db.elephantsql.com',
    user='ticbodpx',
    database='ticbodpx',
    password='bi4ui8sReUxmeBaHvViM2e85z9j3UXYh'
)
cursor = accessory_data_base.cursor()


for a in accessory_Base:
    name = a["Accessory_name"]
    price = a["Accessory_price"]
    img = a["Accessory_image"]
    cursor.execute(f"""INSERT INTO accessory(name, price, image) values ('{product_name}', '{product_price}', '{product_image}')""")

accessory_data_base.commit()
print(accessory_data_base)