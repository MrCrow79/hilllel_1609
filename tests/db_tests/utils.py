import allure



@allure.step('insert data into')
def insert_data(query, cursor, connection):

    cursor.execute(query)
    connection.commit()  # опублікувати зміни