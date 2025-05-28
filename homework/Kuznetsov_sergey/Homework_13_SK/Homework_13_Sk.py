import os
from datetime import timedelta
from datetime import datetime

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
eugene_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')

with open(eugene_file_path, 'r') as data_file:
    first_line = data_file.readline().strip()
    second_line = data_file.readline().strip()
    third_line = data_file.readline().strip()
    if first_line:
        data_time_str = first_line.split(' - ')[0].split('. ', 1)[1]
        data_time = datetime.strptime(data_time_str, '%Y-%m-%d %H:%M:%S.%f')
        new_date_time = data_time + timedelta(weeks=1)

        print(new_date_time)

    if second_line:
        data_time_str = second_line.split(' - ')[0].split('. ', 1)[1]
        data_time = datetime.strptime(data_time_str, '%Y-%m-%d %H:%M:%S.%f')
        day_of_week = data_time.strftime('%A')

        print(day_of_week)

    if third_line:
        data_time_str = third_line.split(' - ')[0].split('. ', 1)[1]
        data_time = datetime.strptime(data_time_str, '%Y-%m-%d %H:%M:%S.%f')
        current_data = datetime.now()
        day_difference = (current_data - data_time).days

        print(day_difference)
