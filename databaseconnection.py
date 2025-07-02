# db_tools.py

import pandas as pd
import pymysql

def get_connection(
    username='root',
    password='Sahil@2003',
    host='localhost',
    port=3306,
    database='inventory'
):
    """
    Establishes a direct pymysql connection to the MySQL database.
    """
    try:
        connection = pymysql.connect(
            host=host,
            user=username,
            password=password,
            database=database,
            port=port
        )
        print("✅ Connected to MySQL successfully using pymysql.")
        return connection
    except Exception as e:
        print("❌ Connection failed:", e)
        return None

def fetch_data(
    query="SELECT * FROM vendor_sales_summary LIMIT 5;",
    username='',
    password='',
    host='localhost',
    port=3306,
    database='inventory'
):
    """
    Executes the given SQL query and returns the result as a DataFrame.
    """
    connection = get_connection(username, password, host, port, database)

    if connection:
        try:
            df = pd.read_sql(query, con=connection)
            print(f"➡️ Retrieved {df.shape[0]} rows × {df.shape[1]} columns")
            return df
        except Exception as e:
            print("❌ Query failed:", e)
            return None
        finally:
            connection.close()
    return None
