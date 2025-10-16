# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL

import os

import dotenv
import pymysql
import pymysql.cursors

TABLE_NAME = 'customers'

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    # cursorclass=pymysql.cursors.DictCursor,
    cursorclass=pymysql.cursors.SSDictCursor,
)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id) '
            ') '
        )
        #CUIDADO: TRUNCATE apaga todos os dados da tabela
        cursor.execute(F'TRUNCATE TABLE {TABLE_NAME}')
    connection.commit()

    # Insert de dados
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) VALUES (%(nome)s, %(idade)s) '
        )
        data = (
            {"nome": "João", "idade": 22},
            {"nome": "Ana", "idade": 32},
            {"nome": "Maria", "idade": 27},
            {"nome": "Pedro", "idade": 18},
            {"nome": "Júlia", "idade": 25},
        )
        result = cursor.executemany(sql, data)
        # print(sql)
        # print(data)
        # print(result)
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            'WHERE id = %s '
        )
        cursor.execute(sql, (5))
        data2 = cursor.fetchall()

        # for row in data2:
        #     print(row) 

    with connection.cursor() as cursor:
        sql = (
            f'DELETE FROM {TABLE_NAME} '
            'WHERE id = %s '
        )
        cursor.execute(sql, (4))
        connection.commit()

        cursor.execute(f'SELECT * FROM {TABLE_NAME}')

        # for row in cursor.fetchall():
        #     print(row)


    with connection.cursor() as cursor:
        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET idade = %s '
            'WHERE id = %s '
        )
        cursor.execute(sql,(30, 1))
        connection.commit()

        resultFromSelect = cursor.execute(f'SELECT * FROM {TABLE_NAME}')
        print('--- Após UPDATE ---')

        # for row in cursor.fetchall():
        #     _id, nome, idade = row
        #     print(_id, nome, idade)

        print('For 1: ')
        for row in cursor.fetchall_unbuffered():
            print(row)
            # print(row['id'])

            if row['id'] >= 3:
                break

        print('--- Usando cursor.scroll() ---')

        print('For 2: ')
        # cursor.scroll(1)
        # cursor.scroll(0, mode='absolute')
        data3 = cursor.fetchall()
        for row in data3:
            print(row)

        cursor.execute(
            f'SELECT id FROM {TABLE_NAME} ORDER BY id DESC LIMIT 1 '
        )
        lastIdFromSelect = cursor.fetchone()

        print('resultadoFromSelect: ', resultFromSelect)
        print('len(data3): ', len(data3))
        print('row count: ', cursor.rowcount)
        print('lastrowid: ', cursor.lastrowid)
        print('lastrowid na mão: ', lastIdFromSelect)
        print('rownumber: ', cursor.rownumber)

    connection.commit()