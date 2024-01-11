import psycopg2
from parsing_office_technique import data_Base, product_image, product_name, product_price


office_technique_data_base = psycopg2.connect(
    host='john.db.elephantsql.com',
    user='ticbodpx',
    database='ticbodpx',
    password='bi4ui8sReUxmeBaHvViM2e85z9j3UXYh'
)
cursor = office_technique_data_base.cursor()


for c in data_Base:
    name = c["Technique_name"]
    price = c["Technique_price"]
    img = c["Technique_image"]
    cursor.execute(f"""INSERT INTO office_technique(name, price, image) values ('{product_name}', '{product_price}', '{product_image}')""")

office_technique_data_base.commit()
print(office_technique_data_base)