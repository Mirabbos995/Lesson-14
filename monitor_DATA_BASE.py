import psycopg2
from monitor_parsing import monitor_Base, product_image, product_name, product_price


monitor_data_base = psycopg2.connect(
    host='john.db.elephantsql.com',
    user='ticbodpx',
    database='ticbodpx',
    password='bi4ui8sReUxmeBaHvViM2e85z9j3UXYh'
)
cursor = monitor_data_base.cursor()


for m in monitor_Base:
    name = m["Monitor_name"]
    price = m["Monitor_price"]
    img = m["Monitor_image"]
    cursor.execute(f"""INSERT INTO monitor(name, price, image) values ('{product_name}', '{product_price}', '{product_image}')""")

monitor_data_base.commit()
print(monitor_data_base)