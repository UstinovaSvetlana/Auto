import allure
import random
from faker import Faker
from EmployeesApi import EmployeesApi
from EmployeesTable import EmployeesTable

api = EmployeesApi("https://x-clients-be.onrender.com")
db = EmployeesTable("postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx")

fake = Faker("ru_RU")

@allure.step("Создание компании")
def test_generate_company()  -> tuple[str, str]:
    name = fake.name()
    description = fake.text(max_nb_chars=20)
    return name, description

@allure.step("Создание сотрудника")
def test_generate_employee(companyId: int) -> tuple[str, str, str, str, str, str, str, bool]:
    firstName = fake.first_name()
    lastName = fake.last_name()
    middleName = fake.first_name() + "ович"
    phone = fake.bothify(text='+79#########')
    email = fake.email(domain = "example.com")
    birthdate = '1989-01-21'
    url = fake.url(schemes = ['http', 'https'])
    isActive = random.choice([True, False])
    return firstName, lastName, middleName, phone, email, birthdate, url, isActive

@allure.step("Редактирование сотрудника")
def test_generate_edit_employee(companyId: int) -> tuple[str, str, str, str, bool]:
    new_lastName = fake.last_name()
    new_email = fake.email(domain = "example.com")
    new_url = fake.url(schemes = ['http', 'https'])
    new_phone = fake.bothify(text='+79#########')
    new_isActive = random.choice([True, False])
    return new_lastName, new_email, new_url, new_phone, new_isActive
    
@allure.title("Получение полного списка сотрудников")
@allure.description("Проверка полного списка сотрудников")
@allure.feature("READ")
@allure.severity("blocker")
def test_get_list_employee()  -> None:
    with allure.step("Cоздание компании"):
        name, description = test_generate_company()
        db.create_company_db(name, description)

    max_id = db.get_max_id_company(id)

    new_company = api.get_company(max_id)
    api_list = api.get_employees_list(max_id)

    db_list = db.get_emploees_db(max_id)

    with allure.step("Проверить, что список сотрудников в API и db одинаковый"):
        assert len(api_list) == len(db_list)

@allure.title("Добавление нового сотрудника")
@allure.description("Тест проверяет возможность добавления новых сотрудников")
@allure.feature("CREATE")
@allure.severity("blocker")
def test_add_new_employee()  -> None:
    with allure.step("Cоздание компании"):
        name, description = test_generate_company()
        db.create_company_db(name, description)

    max_id = db.get_max_id_company(id)

    new_company = api.get_company(max_id)

    api_list_before = api.get_employees_list(max_id)
    db_list_before = db.get_emploees_db(max_id)

    with allure.step("Добавление нового сотрудника"):
        firstName, lastName, middleName, phone, email, birthdate, url, isActive = test_generate_employee(max_id)
        db.create_employee_db(firstName, lastName, middleName, phone, email, birthdate, url, max_id, isActive)

    max_id_empl = db.get_max_id_employee(id)

    api_list_after = api.get_employees_list(max_id)
    db_list_after = db.get_emploees_db(max_id)

    db.delete_employee_db(max_id_empl)

    db.delete(max_id)

    with allure.step("Проверка разницу"):
        with allure.step("Проверить, что список API = db до создания сотрудника"):
            assert len(api_list_before) == len(db_list_before)
        with allure.step("Проверить, что список API = db после создания сотрудника"):
            assert len(api_list_after) == len(db_list_after)
        with allure.step("Проверить, что список до меньше списка после на 1 в API"):
            assert len(api_list_after) - len(api_list_before) == 1
        with allure.step("Проверить, что список до меньше списка после на 1 в db"):
            assert len(db_list_after) - len(db_list_before) == 1

    with allure.step("Проверить, что поля нового сотрудника заполнены верно"):
        assert api_list_after[-1]['firstName'] == firstName
        assert api_list_after[-1]['lastName'] == lastName
        assert api_list_after[-1]['middleName'] == middleName
        assert api_list_after[-1]['email'] == email
        assert api_list_after[-1]['birthdate'] == birthdate
        assert api_list_after[-1]['avatar_url'] == url
        assert api_list_after[-1]['isActive'] == isActive
        assert api_list_after[-1]['id'] == max_id_empl

@allure.title("Редактирование данных сотрудника")
@allure.description("Тест проверяет возможность редактирования данных сотрудника")
@allure.feature("UPDATE")
@allure.severity("blocker")
def test_patch_employee()  -> None:
    with allure.step("Cоздать новую компанию"):
        name, description = test_generate_company()
        db.create_company_db(name, description)

    max_id = db.get_max_id_company(id)

    new_company = api.get_company(max_id)

    api_list_before = api.get_employees_list(max_id)
    db_list_before = db.get_emploees_db(max_id)

    with allure.step("Добавить нового сотрудника"):
        firstName, lastName, middleName, phone, email, birthdate, url, isActive = test_generate_employee(max_id)
        db.create_employee_db(firstName, lastName, middleName, phone, email, birthdate, url, max_id, isActive)

    max_id_empl = db.get_max_id_employee(id)

    api_list_after = api.get_employees_list(max_id)
    db_list_after = db.get_emploees_db(max_id)

    with allure.step("Редактировать данные сотрудника"):
        new_lastName, new_email, new_url, new_phone, new_isActive = test_generate_edit_employee(max_id)
        edited = api.edit_employee(new_lastName, new_email, new_url, new_phone, new_isActive, max_id_empl)
   
    db.delete_employee_db(max_id_empl)

    db.delete(max_id)

    with allure.step("Проверить,что поля сотрудника заполнены верно и изменены"):
        assert edited["url"] == new_url
        assert edited["isActive"] == new_isActive
        assert edited["email"] == new_email
        
@allure.title("Удаление сотрудника по id")
@allure.description("Проверка удаления сотрудника")
@allure.feature("DELETE")
@allure.severity("blocker")
def test_delete_employee()  -> None:
    with allure.step("Cоздание компании"):
        name, description = test_generate_company()
        db.create_company_db(name, description)

    max_id = db.get_max_id_company(id)

    new_company = api.get_company(max_id)

    api_list_before = api.get_employees_list(max_id)
    db_list_before = db.get_emploees_db(max_id)

    with allure.step("Добавление сотрудника"):
        firstName, lastName, middleName, phone, email, birthdate, url, isActive = test_generate_employee(max_id)
        db.create_employee_db(firstName, lastName, middleName, phone, email, birthdate, url, max_id, isActive)

    max_id_empl = db.get_max_id_employee(id)

    api_list_after = api.get_employees_list(max_id)
    db_list_after = db.get_emploees_db(max_id)

    db.delete_employee_db(max_id_empl)

    db.delete(max_id)

    with allure.step("Проверить удаление сотрудника в компании с максимальным id"):
        assert not db.get_emploees_db(max_id)
        
@allure.title("Добавить и удалить сразу нескольких сотрудников")
@allure.description("Тест проверяет возможность добавления и удаления сразу нескольких сотудников")
@allure.feature("ADD, DELETE")
@allure.severity("blocker")
def test_add_del_several_empl()  -> None:
    with allure.step("Cоздать новую компанию"):
        name, description = test_generate_company()
        db.create_company_db(name, description)

    max_id = db.get_max_id_company(id)

    new_company = api.get_company(max_id)

    api_list_before = api.get_employees_list(max_id)
    db_list_before = db.get_emploees_db(max_id)

    with allure.step("Добавление нескольких сотрудников в компанию"):
        with allure.step("Цикл для добавления сотрудников"):
            for i in range(10):
                firstName, lastName, middleName, phone, email, birthdate, url, isActive = test_generate_employee(max_id)
                db.create_employee_db(firstName, lastName, middleName, phone, email, birthdate, url, max_id, isActive)

    max_id_empl = db.get_max_id_employee(id)

    api_list_after = api.get_employees_list(max_id)
    db_list_after = db.get_emploees_db(max_id)

    with allure.step("Удаление несколько сотрудников"):
        with allure.step("Цикл для удаления всех сотрудников"):
            for i in range(10):
                db.delete_employee_db(max_id_empl - i)

    db.delete(max_id)

    with allure.step("Проверить, что список до меньше списка после на 10 в API "):
        assert len(api_list_after) - len(api_list_before) == 10

    with allure.step("Проверить, что список до меньше списка после на 10 в db"):
        assert len(db_list_after) - len(db_list_before) == 10

    with allure.step("Проверить удаление в организации с максимальным id"):
        assert not db.get_emploees_db(max_id)