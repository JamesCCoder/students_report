# import csv
# import random
# from datetime import datetime

# Generated random student data
# def generate_simulated_data(num_students):
#     data = []
#     for i in range(num_students):
#         first_name = f"Student{i+1}"
#         last_name = f"Doe{i+1}"
#         email = f"student{i+1}@example.com"
#         course = f"Course {random.randint(101, 401)}"
#         activity_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         data.append([first_name, last_name, email, course, activity_date])
#     return data



def generate_simulated_data():
    return [
        ['James', 'Wu', 'justinwpro@gmail.com', 'Math 101', '2024-05-21T14:30:00Z'],
        ['Jane', 'White', 'jane.white@gmail.com', 'Chemistry 201', '2024-05-21T10:15:00Z'],
        ['Alice', 'Michael', 'alice.michael@gmail.com', 'Physics 301', '2024-05-22T08:45:00Z'],
        ['Bob', 'Smith', 'bob.smith@gmail.com', 'Business 401', '2024-05-23T11:00:00Z']
    ]
