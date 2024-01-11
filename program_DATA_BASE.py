import psycopg2
from program_parsing import program_Base, product_image, product_name, product_price

program_data_base = psycopg2.connect(
    host='john.db.elephantsql.com',
    user='ticbodpx',
    database='ticbodpx',
    password='bi4ui8sReUxmeBaHvViM2e85z9j3UXYh'
)
cursor = program_data_base.cursor()


for c in program_Base:
    name = c["Program_name"]
    price = c["Program_price"]
    img = c["Program_image"]
    cursor.execute(f"""INSERT INTO program(name, price, image) values ('{product_name}', '{product_price}', '{product_image}')""")

program_data_base.commit()
print(program_data_base)
