import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor()

cursor.execute("INSERT INTO students (name, second_name) VALUES ('Сергей', 'Кузнецов')")
stud_id = cursor.lastrowid
cursor.execute(f'SELECT * from students where id = {stud_id}')
print(cursor.fetchone())
db.commit()

insert_query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
cursor.executemany(
    insert_query, [
        ('Book1', 20662),
        ('Book2', 20662)
    ]
)

cursor.execute(f'SELECT * from books')
print(cursor.fetchall())
db.commit()

cursor.execute("insert INTO `groups` (title, start_date, end_date) VALUES ('Gr Auto', 'Mar 13', 'Dec 25')")
gr_id = cursor.lastrowid
cursor.execute(f'SELECT * from `groups` where id = {gr_id}')
print(cursor.fetchone())
db.commit()

cursor.execute("UPDATE students set group_id = 5341 where id = 20662")
cursor.execute('SELECT * from students where id = 20662')
print(cursor.fetchone())
db.commit()

cursor.execute("INSERT INTO subjets (title) VALUES ('ИЗО'), ('Музыка'), ('Ин.яз')")
cursor.execute('SELECT * from subjets')
print(cursor.fetchall())
db.commit()

insert_query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
cursor.executemany(
    insert_query, [
        ('Урок 1', 10837),
        ('Урок 2', 10837),
        ('Урок 3', 10838),
        ('Урок 4', 10838),
        ('Урок 5', 10839),
        ('Урок 6', 10839)
    ]
)

cursor.execute('SELECT * from lessons')
print(cursor.fetchall())
db.commit()

insert_query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
cursor.executemany(
    insert_query, [
        (4, 11261, 20662),
        (4, 11262, 20662),
        (3, 11263, 20662),
        (3, 11264, 20662),
        (5, 11265, 20662),
        (5, 11266, 20662)
    ]
)

cursor.execute('SELECT * from marks')
print(cursor.fetchall())
db.commit()

cursor.execute("Select value from marks where student_id = 20662")
data1 = cursor.fetchall()
res1 = [item[0] for item in data1]
print(' '.join(res1))

cursor.execute("SELECT title from books where taken_by_student_id = 20662")
data2 = cursor.fetchall()
res2 = [item[0] for item in data2]
print(' '.join(res2))

select_query = '''
Select s.name, s.second_name, g.title, b.title, m.value, l.title, s2.title
from students s join `groups` g on s.group_id = g.id 
join books b on s.id = b.taken_by_student_id  
join marks m on s.id = m.student_id 
join lessons l on l.id = m.lesson_id 
join subjets s2 on s2.id = l.subject_id 
where s.id = 20662 
'''

cursor.execute(select_query)
print(cursor.fetchall())

db.close()
