import sqlite3
import pandas as pd


connection = sqlite3.connect('books.db')
#Select all authors' last names from authors table in descending order
pd.options.display.max_columns = 10
print(pd.read_sql('SELECT last FROM authors ORDER BY last DESC', connection))


#Select all book titles from the titles table in ascending order

print(pd.read_sql('SELECT * FROM titles ORDER BY copyright ASC', connection))

#use inner join to select all the books for a specific author, include the title, copyuright year and ISBN
#Order the information alphabetically by title
'''
pd.read_sql("""SELECT first, last, isbn
                    FROM authors
                    INNER JOIN author_ISBN
                    ON authors.id = author_ISBN.id
                    ORDER BY last, first"""
, connection)
'''
#Insert a new author into the authors table

cursor = connection.cursor()
insertAuthor = cursor.execute("""INSERT INTO authors (first, last) VALUES ('Mathias', 'Kniesel')""")
print(pd.read_sql('SELECT last FROM authors ORDER BY last DESC', connection))
#insert a new title for an author. Remember that the book must have an entry in the author_ISBN table 
#and an entry in the titles table
'''

updateAuthor = cursor.execute("""  UPDATE authors SET last='Black' WHERE last='Red' AND first='Sue' """)

'''
connection.close()

#OUTPUT
'''
     last
0    Wald
1   Quirk
2  Deitel
3  Deitel
4  Deitel
         isbn                             title  edition copyright
0  0136151574         Visual C++ How to Program        2      2008
1  0132151006     Internet & WWW How to Program        5      2012
2  0133406954  Visual Basic 2012 How to Program        6      2014
3  0133976890                  C How to Program        8      2016
4  0134289366         Android 6 for Programmers        3      2016
5  0134601548          Visual C# How to Program        6      2017
6  0134448235                C++ How to Program       10      2017
7  0134444302            Android How to Program        3      2017
8  0134743350               Java How to Program       11      2018
9  0135404673     Intro to Python for CS and DS        1      2020
      last
0     Wald
1    Quirk
2  Kniesel
3   Deitel
4   Deitel
5   Deitel
'''