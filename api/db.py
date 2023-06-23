import pymysql

# MySQL connection details
DB_HOST = "db4free.net"
DB_USER = "aradhya"
DB_PORT = 3306
DB_PASSWORD = "aradhya123"
DB_NAME = "putatoedb"


def get_word():
    conn = pymysql.connect(
        host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME
    )
    cursor = conn.cursor()
    query = "SELECT word FROM words LIMIT 1"
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result[0] if result else None


def update_word(new_word):
    conn = pymysql.connect(
        host=DB_HOST,  user=DB_USER, password=DB_PASSWORD, database=DB_NAME
    )
    cursor = conn.cursor()
    query = "UPDATE words SET word = %s"
    cursor.execute(query, (new_word,))
    conn.commit()
    cursor.close()
    conn.close()
