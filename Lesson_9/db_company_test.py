import random
from faker import Faker
from CompanyApi import CompanyApi
from CompanyTable import CompanyTable

api = CompanyApi("https://x-clients-be.onrender.com")
db = CompanyTable("postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx")

fake = Faker("ru_Ru")

def generate_random_company_data():
    name = fake.name()
    description = fake.text(max_nb_chars=20)
    return name, description

def generate_employee():
    firstName = fake.first_name()
    lastName = fake.last_name()
    middleName = fake.first_name() + "ович"
    mail = fake.email()
    url = fake.url()
    phone = fake.random_number(digits=11)
    birthdate = fake.date_of_birth(minimum_age=18,maximum_age=65).strftime('%Y-%m-%d')
    isActive = random.choice([True, False])
    return firstName, lastName, middleName, mail, url, phone, birthdate, isActive, id, company_id

def generate_random_update_company():
    new_name = fake.name()
    new_description = fake.text(max_nb_chars=20)
    return new_name, new_description

def test_get_companies():
    api_result = api.get_company_list()
    db_result = db.get_company_list()
    assert len(api_result) == len(db_result)

def test_get_active_companies():
    filtered_list = api.get_company_list(params_to_add={'active': 'true'})
    db_list = db.get_active_company()
    assert len(filtered_list) == len(db_list)

def test_add_company():
    api_result_before = api.get_company_list()
    db_result_before = db.get_company_list()

    name, description = generate_random_company_data()
    db.create_comp(name, description)
    max_id = db.get_max_id_comp(id)

    api_result_after = api.get_company_list()
    db_result_after = db.get_company_list()

    db.delete_company(max_id)

    assert len(api_result_before) == len(db_result_before)
    assert len(api_result_after) == len(db_result_after)
    assert len(db_result_after) - len(db_result_before) == 1
    assert len(api_result_after) - len(api_result_before) == 1
    assert api_result_after[-1]["name"] == name
    assert api_result_after[-1]["description"] == description
    assert api_result_after[-1]["id"] == max_id

def test_get_one_company():
    name, description = generate_random_company_data()
    db.create_comp(name, description)
    max_id = db.get_max_id_comp(id)

    new_company = api.get_company(max_id)

    db.delete_company(max_id)

    assert new_company["id"] == max_id
    assert new_company["name"] == name
    assert new_company["description"] == description
    assert new_company["isActive"] == True

def test_edit():
    name, description = generate_random_company_data()
    db.create_comp(name, description)
    max_id = db.get_max_id_comp(id)

    new_name, new_description = generate_random_update_company()
    edited = api.edit(max_id, new_name, new_description)

    db.delete_company(max_id)

    assert edited["id"] == max_id
    assert edited['name'] == new_name
    assert edited['description'] == new_description
    assert edited['isActive'] == True

def test_delete():
    name, description = generate_random_company_data()
    db.create_comp(name, description)
    max_id = db.get_max_id_comp(id)

    deleted = api.delete(max_id)
    db.delete_company(max_id)

    assert deleted["id"] == max_id
    assert deleted["name"] == name
    assert deleted["description"] == description
    assert deleted["isActive"] == True

    rows = db.get_company_by_id(max_id)
    assert len(rows) == 0

def test_deactivate():
    name, description = generate_random_company_data()
    db.create_comp(name, description)
    max_id = db.get_max_id_comp(id)

    body = api.set_active_state(max_id, False)

    db.delete_company(max_id)

    assert body["isActive"] == False

def test_deactivate_and_activate_back():
    name, description = generate_random_company_data()
    db.create_comp(name, description)
    max_id = db.get_max_id_comp(id)

    api.set_active_state(max_id, False)

    body = api.set_active_state(max_id, True)
    db.delete_company(max_id)

    assert body["isActive"] == True