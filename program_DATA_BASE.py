import psycopg2
from program_parsing import program_Base

program_data_base = psycopg2.connect(
    host='john.db.elephantsql.com',
    user='ticbodpx',
    database='ticbodpx',
    password='bi4ui8sReUxmeBaHvViM2e85z9j3UXYh'
)
cursor = program_data_base.cursor()


for program in program_Base:
    product_name = program["Program_name"]
    product_price = program["Program_price"]
    product_image = program["Program_image"]
    cursor.execute(f"""INSERT INTO program(name, price, image) values ('{product_name}', '{product_price}', '{product_image}')""")

program_data_base.commit()
# print(program_data_base)
