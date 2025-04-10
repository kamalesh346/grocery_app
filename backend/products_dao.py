from sql_connection import get_sql_connection
def get_all_products(connection):
    
    cursor = connection.cursor()
    query=("SELECT products.prod_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name " \
    "FROM products inner join uom on products.uom_id=uom.uom_id")
    cursor.execute(query)
    response=[]
    for (prod_id, name, uom_id, price_per_unit,uom_name) in cursor:
        response.append(
            {
                'prod_id':prod_id, 
                'name':name, 
                'uom_id':uom_id, 
                'price_per_unit':price_per_unit, 
                'uom_name':uom_name
            }
       )

    return response
def insert_new_product(connection,product):
    cursor=connection.cursor()
    query=("INSERT INTO products(name,uom_id,price_per_unit) VALUES (%s,%s,%s)")
    data=(product['name'],product['uom_id'],product['price_per_unit'])
    cursor.execute(query,data)
    connection.commit()

    return cursor.lastrowid
def delete_product(connection,prod_id):

    cursor=connection.cursor()
    query=("DELETE FROM products where prod_id=%s")#+str(prod_id)
    cursor.execute(query,[prod_id,])
    connection.commit()
if __name__=='__main__':
    connection=get_sql_connection()
    print(delete_product(connection,3))
