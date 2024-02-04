import csv
from pymongo import MongoClient

# Kết nối tới MongoDB
client = MongoClient('localhost', 27017)
database = client['dep302_asm2']

# Import dữ liệu vào bộ sưu tập 'educations'
educations_collection = database['educations']
education_ids = []  # Danh sách ID của các documents trong 'educations'
with open('US Adult Income.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        education_data = {
            'education': row['education'],
            'education_num': int(row['education_num'])
        }
        education_result = educations_collection.insert_one(education_data)
        education_ids.append(education_result.inserted_id)

# Import dữ liệu vào bộ sưu tập 'occupations'
occupations_collection = database['occupations']
occupation_ids = []  # Danh sách ID của các documents trong 'occupations'
with open('US Adult Income.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        occupation_data = {
            'occupation': row['occupation'],
            'workclass': row['workclass'],
            'hours_per_week': int(row['hours_per_week'])
        }
        occupation_result = occupations_collection.insert_one(occupation_data)
        occupation_ids.append(occupation_result.inserted_id)

# Import dữ liệu vào bộ sưu tập 'relationships'
relationships_collection = database['relationships']
relationship_ids = []  # Danh sách ID của các documents trong 'relationships'
with open('US Adult Income.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        relationship_data = {
            'marital_status': row['marital_status'],
            'relationship': row['relationship']
        }
        relationship_result = relationships_collection.insert_one(relationship_data)
        relationship_ids.append(relationship_result.inserted_id)

# Import dữ liệu vào bộ sưu tập 'finances'
finances_collection = database['finances']
finance_ids = []  # Danh sách ID của các documents trong 'finances'
with open('US Adult Income.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        finance_data = {
            'total': int(row['total']),
            'capital_gain': int(row['capital_gain']),
            'capital_loss': int(row['capital_loss']),
            'hours_per_week': int(row['hours_per_week']),
            'income_bracket': row['income_bracket']
        }
        finance_result = finances_collection.insert_one(finance_data)
        finance_ids.append(finance_result.inserted_id)

# Import dữ liệu vào bộ sưu tập 'users'
users_collection = database['users']
with open('US Adult Income.csv') as file:
    reader = csv.DictReader(file)
    for i, row in enumerate(reader):
        user_data = {
            'age': int(row['age']),
            'gender': row['gender'],
            'race': row['race'],
            'native_country': row['native_country'],
            'education_id': education_ids[i],
            'occupation_id': occupation_ids[i],
            'relationship_id': relationship_ids[i],
            'finance_id': finance_ids[i]
        }
        users_collection.insert_one(user_data)

# Đóng kết nối đến MongoDB
client.close()
