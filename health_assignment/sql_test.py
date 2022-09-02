
import pandas as pd
import sqlite3
import openpyxl


def reading_sql(query, connection, query_name):
    if query_name == "no":
        if type(query) != str:
            df = pd.read_sql_query(query.read(), connection)
            # if you wish to export your query to excel:
            print(df)
            return df
        else:
            df = pd.read_sql_query(query, connection)
            # if you wish to export your query to excel:
            print(df)
            return df
    else:
        if type(query) != str:
            df = pd.read_sql_query(query.read(), connection)
            # if you wish to export your query to excel:
            df.to_excel(r'C:\\Users\\Christoffer Brodin\\Documents\Academy\\' + query_name + '.xlsx')
            print(df)
        else:
            df = pd.read_sql_query(query, connection)
            # if you wish to export your query to excel:
            df.to_excel(r'C:\\Users\\Christoffer Brodin\\Documents\Academy\\' + query_name + '.xlsx')
            print(df)

def sorting_sql(sql_data):
    sql_data.loc[(sql_data["age"] > 18) & (sql_data["country"] == "Sweden"), "LegalAge"] = "Yes"
    sql_data.loc[(sql_data["age"] > 21) & (sql_data["country"] == "Norway"), "LegalAge"] = "Yes"
    sql_data.loc[(sql_data["country"] != "Sweden") & (sql_data["country"] != "Norway"), "LegalAge"] = "Unknown"
    print(sql_data)



    # df.loc[(df['first_name'] != 'Bill') & (df['first_name'] != 'Emma'), 'name_match'] = 'Mismatch'
# Connection for .db file on you pc
conn = sqlite3.connect(r"C:\Users\Christoffer Brodin\Documents\Academy\Database\week4.db")
# if you have a text document with a query you can open and run with python,
query = open(r'C:\Users\Christoffer Brodin\Documents\Academy\SQL\country.sql')
# writing query in a single string
query_2 = "SELECT name, age, CASE WHEN age >= 21 THEN 'YES' ELSE 'NO' END LegalAge FROM customer ORDER BY LegalAge DESC;"

# writing query in a clean way
query_3 = '''
SELECT cus.name,  COUNT(DISTINCT(aread.article_id)) as dist_read_art, UPPER(SUBSTRING(country, 1, 3)) as CountryCode 
FROM customer cus, article_reads aread, 
article ar, paper_subscription ps
WHERE cus.id = aread.customer_id
AND aread.article_id = ar.id 
AND cus.id = ps.customer_id 
AND ps.status = 'Inactive'
GROUP BY cus.name
HAVING dist_read_art > 200
ORDER BY CountryCode,  COUNT(DISTINCT(aread.article_id)) DESC
'''
query_4 = '''
SELECT name, age, country FROM customer;
'''

query_5 = '''
CREATE TABLE spanish (word_id INTEGER PRIMARY KEY,
spanish_word VARCHAR(20),
verb_form VARCHAR(20),
yo VARCHAR(10),
tu VARCHAR(10),
elella VARCHAR(10),
nosotros VARCHAR(10),
ellosellas VARCHAR(10),
swedish_translate VARCHAR(20)

INSERT INTO spanish ('spanish_word', 'verb_form','yo', 'tu', 'elella', 'nosotros', 'ellosellas', 'swedish_translate')
VALUES ('comer', 'infinitive','como', 'comes', 'come', 'comemos', 'comen', 'att äta'), 
('escribir', 'infinitive','escribo', 'escribes', 'escribe', 'escribemos', 'escriben', 'att skriva')

SELECT * FROM spanish;
'''
# calling function:
# reading_sql(query, conn, "test")
# reading_sql(query_2, conn, "test_2")
# reading_sql(query_3, conn, "test_3")
# reading_sql(query_4, conn, "no")
reading_sql(query_4, conn, "no")


# df = pd.read_sql_query(query_5, conn)
# print(df)
# calling function, sorting with pandas:
# sorting_sql(reading_sql(query_4, conn, "no"))
# closing connection
conn.close()

