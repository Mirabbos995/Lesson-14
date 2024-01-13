import psycopg2
from accessory_parsing import accessory_Base

accessory_data_base = psycopg2.connect(
    host='john.db.elephantsql.com',
    user='ticbodpx',
    database='ticbodpx',
    password='bi4ui8sReUxmeBaHvViM2e85z9j3UXYh'
)
cursor = accessory_data_base.cursor()



for access in accessory_Base:
    product_name = access["Accessory_name"]
    product_price = access["Accessory_price"]
    product_image = access["Accessory_image"]
    cursor.execute(f"""INSERT INTO accessory(name, price, image) values ('{product_name}', '{product_price}', '{product_image}')""")

accessory_data_base.commit()
# print(monitor_data_base)