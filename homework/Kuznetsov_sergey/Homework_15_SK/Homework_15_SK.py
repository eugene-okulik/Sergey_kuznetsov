import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor()

name = input("Имя: ")
second_name = input("Фамилия: ")

cursor.execute("INSERT INTO students (name, second_name) VALUES (%s, %s)", (name, second_name))
stud_id = cursor.lastrowid
cursor.execute('SELECT * from students where id = %s', (stud_id,))
print(cursor.fetchone())
db.commit()

book_titles = []
for i in range(2):
    title = input(f"Название книги {i + 1}: ")
    book_titles.append((title, stud_id))

insert_query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
cursor.executemany(insert_query, book_titles)
db.commit()

gr_title = input("Название группы: ")
start_date = input("Дата начала: ")
end_date = input("Дата окончания: ")

cursor.execute("insert INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)",
               (gr_title, start_date, end_date))
gr_id = cursor.lastrowid
cursor.execute('SELECT * from `groups` where id = %s', (gr_id,))
print(cursor.fetchone())
db.commit()

cursor.execute("UPDATE students set group_id = %s where id = %s", (gr_id, stud_id))
cursor.execute('SELECT * from students where id = %s', (stud_id,))
print(cursor.fetchone())
db.commit()

subjects_titles = [('Математика',), ('Русский',), ('Литература',)]
insert_query = "INSERT INTO subjets (title) VALUES (%s)"
subj_id = []
for subject in subjects_titles:
    cursor.execute(insert_query, subject)
    subj_id.append(cursor.lastrowid)
sub1, sub2, sub3 = subj_id

db.commit()

lessons_titles = [('Первый', sub1), ('Второй', sub1),
                  ('Третий', sub2), ('Четвертый', sub2),
                  ('Пятый', sub3), ('Шестой', sub3)
                  ]

insert_query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
lessons_id = []
for title in lessons_titles:
    cursor.execute(insert_query, title)
    lessons_id.append(cursor.lastrowid)
les1, les2, les3, les4, les5, les6 = lessons_id

db.commit()

insert_query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
cursor.executemany(
    insert_query, [
        ('5', les1, stud_id),
        ('4', les2, stud_id),
        ('5', les3, stud_id),
        ('4', les4, stud_id),
        ('5', les5, stud_id),
        ('4', les6, stud_id),
    ]
)

cursor.execute(f"SELECT * FROM marks WHERE student_id = {stud_id}")
print(cursor.fetchall())
db.commit()

cursor.execute("Select value from marks where student_id = %s", (stud_id,))
data1 = cursor.fetchall()
res1 = [item[0] for item in data1]
print(' '.join(res1))

cursor.execute("SELECT title from books where taken_by_student_id = %s", (stud_id,))
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
where s.id = %s
'''

cursor.execute(select_query, (stud_id,))
print(cursor.fetchall())

db.close()
