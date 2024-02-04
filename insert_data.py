from pymongo import MongoClient

# Kết nối tới MongoDB
client = MongoClient('localhost', 27017)
database = client['dep302_asm2']

# Hàm chèn dữ liệu vào các bộ sưu tập
def insert_data():
    educations_collection = database['educations']
    occupations_collection = database['occupations']
    relationships_collection = database['relationships']
    finances_collection = database['finances']
    users_collection = database['users']
    
    # Hàm nhập dữ liệu cho 'educations'
    def input_educations(num_entries):
        education_data = []
        for i in range(num_entries):
            education = input("Nhập education: ")
            education_num = int(input("Nhập education_num: "))
            education_data.append({'education': education, 'education_num': education_num})
        educations_collection.insert_many(education_data)
    
    # Hàm nhập dữ liệu cho 'occupations'
    def input_occupations(num_entries):
        occupation_data = []
        for i in range(num_entries):
            occupation = input("Nhập occupation: ")
            occupation_data.append({'occupation': occupation})
        occupations_collection.insert_many(occupation_data)
    
    # Hàm nhập dữ liệu cho 'relationships'
    def input_relationships(num_entries):
        relationship_data = []
        for i in range(num_entries):
            marital_status = input("Nhập marital_status: ")
            relationship = input("Nhập relationship: ")
            relationship_data.append({'marital_status': marital_status, 'relationship': relationship})
        relationships_collection.insert_many(relationship_data)
    
    # Hàm nhập dữ liệu cho 'finances'
    def input_finances(num_entries):
        finance_data = []
        for i in range(num_entries):
            total = int(input("Nhập total: "))
            capital_gain = int(input("Nhập capital_gain: "))
            capital_loss = int(input("Nhập capital_loss: "))
            hours_per_week = int(input("Nhập hours_per_week: "))
            income_bracket = input("Nhập income_bracket: ")
            finance_data.append({'total': total, 'capital_gain': capital_gain, 'capital_loss': capital_loss, 'hours_per_week': hours_per_week, 'income_bracket': income_bracket})
        finances_collection.insert_many(finance_data)
    
    # Hàm nhập dữ liệu cho 'users'
    def input_users(num_entries):
        user_data = []
        for i in range(num_entries):
            age = int(input("Nhập age: "))
            gender = input("Nhập gender: ")
            race = input("Nhập race: ")
            native_country = input("Nhập native_country: ")
            education_id = input("Nhập education_id: ")
            occupation_id = input("Nhập occupation_id: ")
            relationship_id = input("Nhập relationship_id: ")
            finance_id = input("Nhập finance_id: ")
            user_data.append({'age': age, 'gender': gender, 'race': race, 'native_country': native_country, 'education_id': education_id, 'occupation_id': occupation_id, 'relationship_id': relationship_id, 'finance_id': finance_id})
        users_collection.insert_many(user_data)
    
    # Nhập số lượng mục 'users' cần chèn
    num_users = int(input("Nhập số lượng mục 'users' cần chèn: "))
    
    # Nhập dữ liệu cho các collection khác
    input_educations(num_users)
    input_occupations(num_users)
    input_relationships(num_users)
    input_finances(num_users)
    input_users(num_users)

# Gọi hàm chèn dữ liệu
insert_data()
