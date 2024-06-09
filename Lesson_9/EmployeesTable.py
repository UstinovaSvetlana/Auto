from sqlalchemy import create_engine
from sqlalchemy.sql import text

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

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def create_company_db(self, name, description):
        self.__db.execute(self.__scripts["insert company"], new_name = name, new_descr = description)

    def get_max_id_company(self):
        return self.__db.execute(self.__scripts["get max id company"]).fetchall()[0][0]

    def get_emploees_db(self, company_id):
        return self.__db.execute(self.__scripts["select"], id = company_id).fetchall()

    def delete(self, id):
        return self.__db.execute(self.__scripts["delete by id"], id_to_delete = id)

    def create_employee_db(self, first_name, last_name, middle_name, phone, email, birthdate, avatar_url, company_id, is_active):
        self.__db.execute(self.__scripts["insert new employee"], first_name = first_name, last_name = last_name, middle_name = middle_name, phone = phone, email = email, birthdate = birthdate, avatar_url =avatar_url, company_id = company_id, is_active = is_active)

    def get_max_id_employee(self):
        return self.__db.execute(self.__scripts['get max id empl']).fetchall()[0][0]

    def update_employee(self, employeeId, new_lastName, new_email, new_url, new_phone, new_isActive):
        return self.__db.execute(self.scripts['edited employee'], employeeId=employeeId, new_lastName=new_lastName, new_email=new_email, new_url=new_url, new_phone=new_phone, new_isActive=new_isActive)

    def delete_employee_db(self, id):
        return self.__db.execute(self.__scripts['delete id employee'], id_to_delete = id)