import random
from faker import Faker
from EmployeesApi import EmployeesApi
from EmployeesTable import EmployeesTable

api = EmployeesApi("https://x-clients-be.onrender.com")
db = EmployeesTable("postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx")

fake = Faker("ru_RU")

def generate_company():
    name = fake.name()
    description = fake.text(max_nb_chars=20)
    return name, description

def generate_employee(companyId):
    firstName = fake.first_name()
    lastName = fake.last_name()
    middleName = fake.first_name() + "ович"
    phone = fake.bothify(text='+79#########')
    email = fake.email(domain = "example.com")
    birthdate = '1988-03-14'
    url = fake.url(schemes = ['http', 'https'])
    isActive = random.choice([True, False])
    return firstName, lastName, middleName, phone, email, birthdate, url, isActive

def generate_edit_employee(companyId):
    new_lastName = fake.last_name()
    new_email = fake.email(domain = "example.com")
    new_url = fake.url(schemes = ['http', 'https'])
    new_phone = fake.bothify(text='+79#########')
    new_isActive = random.choice([True, False])
    return new_lastName, new_email, new_url, new_phone, new_isActive

def test_get_list_employee():
    name, description = generate_company()
    db.create_company_db(name, description)
    max_id = db.get_max_id_company()

    new_company = api.get_company(max_id)

    api_list = api.get_employees_list(max_id)
    db_list = db.get_emploees_db(max_id)

    assert len(api_list) == len(db_list)

def test_add_new_employee():
    name, description = generate_company()
    db.create_company_db(name, description)
    max_id = db.get_max_id_company()

    new_company = api.get_company(max_id)

    api_list_before = api.get_employees_list(max_id)
    db_list_before = db.get_emploees_db(max_id)

    firstName, lastName, middleName, phone, email, birthdate, url, isActive = generate_employee(max_id)
    db.create_employee_db(firstName, lastName, middleName, phone, email, birthdate, url, max_id, isActive)
    max_id_empl = db.get_max_id_employee()

    api_list_after = api.get_employees_list(max_id)
    db_list_after = db.get_emploees_db(max_id)

    db.delete_employee_db(max_id_empl)

    db.delete(max_id)

    assert len(api_list_before) == len(db_list_before)
    assert len(api_list_after) == len(db_list_after)
    assert len(api_list_after) - len(api_list_before) == 1
    assert len(db_list_after) - len(db_list_before) == 1
    assert api_list_after[-1]['firstName'] == firstName
    assert api_list_after[-1]['lastName'] == lastName
    assert api_list_after[-1]['middleName'] == middleName
    assert api_list_after[-1]['phone'] == phone
    assert api_list_after[-1]['email'] == email
    assert api_list_after[-1]['birthdate'] == birthdate
    assert api_list_after[-1]['avatar_url'] == url
    assert api_list_after[-1]['isActive'] == isActive
    assert api_list_after[-1]['id'] == max_id_empl

def test_patch_employee():
    name, description = generate_company()
    db.create_company_db(name, description)
    max_id = db.get_max_id_company()

    new_company = api.get_company(max_id)

    api_list_before = api.get_employees_list(max_id)
    db_list_before = db.get_emploees_db(max_id)

    firstName, lastName, middleName, phone, email, birthdate, url, isActive = generate_employee(max_id)
    db.create_employee_db(firstName, lastName, middleName, phone, email, birthdate, url, max_id, isActive)
    max_id_empl = db.get_max_id_employee()

    api_list_after = api.get_employees_list(max_id)
    db_list_after = db.get_emploees_db(max_id)

    new_lastName, new_email, new_url, new_phone, new_isActive = generate_edit_employee(max_id)
    edited = api.edit_employee(new_lastName, new_email, new_url, new_phone, new_isActive, max_id_empl)

    db.delete_employee_db(max_id_empl)

    db.delete(max_id)

    assert edited["email"] == new_email
    assert edited["url"] == new_url
    assert edited["isActive"] == new_isActive    
 

def test_delete_employee():
    name, description = generate_company()
    db.create_company_db(name, description)
    max_id = db.get_max_id_company()

    new_company = api.get_company(max_id)

    api_list_before = api.get_employees_list(max_id)
    db_list_before = db.get_emploees_db(max_id)

    firstName, lastName, middleName, phone, email, birthdate, url, isActive = generate_employee(max_id)
    db.create_employee_db(firstName, lastName, middleName, phone, email, birthdate, url, max_id, isActive)
    max_id_empl = db.get_max_id_employee()

    api_list_after = api.get_employees_list(max_id)
    db_list_after = db.get_emploees_db(max_id)

    db.delete_employee_db(max_id_empl)

    db.delete(max_id)

    assert not db.get_emploees_db(max_id)

def test_add_del_several_empl():
    name, description = generate_company()
    db.create_company_db(name, description)
    max_id = db.get_max_id_company()

    new_company = api.get_company(max_id)

    api_list_before = api.get_employees_list(max_id)
    db_list_before = db.get_emploees_db(max_id)

    for i in range(10):
        firstName, lastName, middleName, phone, email, birthdate, url, isActive = generate_employee(max_id)
        db.create_employee_db(firstName, lastName, middleName, phone, email, birthdate, url, max_id, isActive)

    max_id_empl = db.get_max_id_employee()

    api_list_after = api.get_employees_list(max_id)
    db_list_after = db.get_emploees_db(max_id)

    for i in range(10):
        db.delete_employee_db(max_id_empl - i)

    db.delete(max_id)

    assert len(api_list_after) - len(api_list_before) == 10
    assert len(db_list_after) - len(db_list_before) == 10
    assert not db.get_emploees_db(max_id)