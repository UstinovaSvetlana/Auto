import allure
from sqlalchemy import create_engine, Engine
from sqlalchemy.sql import text
from sqlalchemy.engine import ResultProxy
from typing import List, Tuple, Any

class EmployeesTable:
    __scripts = {
        "insert company": text("insert into company (\"name\", \"description\") values (:new_name, :new_descr)"),
        "get max id company": text("select MAX(id) from company"),
        "select": text("select * from employee where company_id = :id"),
        "insert new employee": text("insert into employee (first_name, last_name, middle_name, phone, email, birthdate, avatar_url, is_active, company_id) values (:first_name, :last_name, :middle_name, :phone, :email, :birthdate, :avatar_url, :is_active, :company_id)"),
        "get max id empl": text("select MAX(id) from employee"),
        'edited employee': text("update employee set last_name = :new_lastName, email = :new_email, url = :new_url, phone = :new_phone, isActive = :new_isActive where id = :employeeId"),
        'delete id employee': text("delete from employee where id = :id_to_delete"),
        "delete by id": text("delete from company where id = :id_to_delete")
    }

    def __init__(self, connection_string: str) -> None:
        self.__db: Engine = create_engine(connection_string)

    @allure.step("БД.Создание компании {name}:{description}")
    def create_company_db(self, name: str, description: str) -> None:
        query: ResultProxy = self.__db.execute(self.__scripts["insert company"], new_name=name, new_descr=description)
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)

    @allure.step("БД. Получение максимального {id} компании")
    def get_max_id_company(self, id: int) -> int:
        query: ResultProxy = self.__db.execute(self.__scripts["get max id company"], max_id=id)
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
        return query.fetchall()[0][0]

    @allure.step("БД. Получение списка сотрудников компании {company_id}")
    def get_emploees_db(self, company_id: int) -> List[Tuple[Any]]:
        query: ResultProxy = self.__db.execute(self.__scripts["select"], id=company_id)
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
        return query.fetchall()

    @allure.step("БД. Удаление компании по {id}")
    def delete(self, id: int) -> None:
        query: ResultProxy = self.__db.execute(self.__scripts["delete by id"], id_to_delete=id)
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)

    @allure.step("БД.Создание сотрудника {first_name}:{last_name}:{middle_name}:{phone}:{email}:{birthdate}:{avatar_url}:{company_id}:{is_active}")
    def create_employee_db(self, first_name: str, last_name: str, middle_name: str, phone: int, email: str, birthdate: str, avatar_url: str, company_id: int, is_active: bool) -> None:
        query: ResultProxy = self.__db.execute(self.__scripts["insert new employee"], first_name=first_name, last_name=last_name, middle_name=middle_name, phone=phone, email=email, birthdate=birthdate, avatar_url=avatar_url, company_id=company_id, is_active=is_active)
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)

    @allure.step("БД. Получение максимального {id} сотрудника")
    def get_max_id_employee(self, id: int) -> int:
        query: ResultProxy = self.__db.execute(self.__scripts['get max id empl'], max_id_empl=id)
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
        return query.fetchall()[0][0]

    @allure.step("БД. Редактирование сотрудника {employeeId}:{new_lastName}:{new_email}:{new_url}:{new_phone}:{new_isActive}")
    def update_employee(self, employeeId: int, new_lastName: str, new_email: str, new_url: str, new_phone: int, new_isActive: bool) -> None:
        query: ResultProxy = self.__db.execute(self.__scripts['edited employee'], employeeId=employeeId, new_lastName=new_lastName, new_email=new_email, new_url=new_url, new_phone=new_phone, new_isActive=new_isActive)
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)

    @allure.step("БД. Удаление сотрудника по {id}")
    def delete_employee_db(self, id: int) -> None:
        query: ResultProxy = self.__db.execute(self.__scripts['delete id employee'], id_to_delete=id)
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)