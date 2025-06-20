import csv
import os
import dotenv
import mysql.connector as mysql

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

abs_path = "/Users/user/Project/Sergey_kuznetsov/homework/eugene_okulik/Lesson_16/hw_data/data.csv"
with open(abs_path, newline='') as csv_file:
    file_data = list(csv.DictReader(csv_file))
    for row in file_data:
        print(row)

mis_data = []

with db.cursor() as cursor:
    for row in file_data:
        query = """
        Select s.name, s.second_name, g.title, b.title, m.value, l.title, s2.title
        from students s join `groups` g on s.group_id = g.id
        join books b on s.id = b.taken_by_student_id
        join marks m on s.id = m.student_id
        join lessons l on l.id = m.lesson_id
        join subjets s2 on s2.id = l.subject_id
        WHERE s.name = %s
        AND s.second_name = %s
        AND g.title = %s
        AND b.title = %s
        AND m.value = %s
        AND l.title = %s
        AND s2.title = %s
        """

        params = (
            row['name'],
            row['second_name'],
            row['group_title'],
            row['book_title'],
            row['mark_value'],
            row['lesson_title'],
            row['subject_title']
        )

        cursor.execute(query, params)
        count = cursor.fetchone()

        if count == 0:
            mis_data.append(row)

if mis_data:
    print("Данные, отсутствующие в базе:")
    for data in mis_data:
        print(data)
else:
    print("Все данные из CSV присутствуют в базе.")

db.close()
