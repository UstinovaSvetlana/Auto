from sqlalchemy import create_engine
from sqlalchemy.sql import text

class CompanyTable:
    __scripts = {
        "select": text("select * from company"),
        "select": text("select * from company where deleted_at is NULL"),
        "select by id": text("select * from company where id = :company_id"),
        "select isActive": text("select * from company where \"is_active\" = true and deleted_at is NULL"),
        "delete by id": text("delete from company  where id = :id_to_delete"),
        "insert company": text("insert into company (\"name\", \"description\") values (:new_name, :new_descr)"),
        "get max id": text("select MAX(id) from company"),
        "select empl list": text("select * from employee where company_id = :id"),
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_company_list(self):
        return self.__db.execute(self.__scripts["select"]).fetchall()

    def get_company_by_id(self,id):
        return self.__db.execute(self.__scripts["select by id"], company_id = id).fetchall()

    def get_active_company(self):
        return self.__db.execute(self.__scripts["select isActive"]).fetchall()

    def delete_company(self, id):
        self.__db.execute(self.__scripts["delete by id"], id_to_delete = id)

    def create_comp(self, name, description):
        self.__db.execute(self.__scripts["insert company"], new_name = name, new_descr = description)

    def get_max_id_comp(self, id):
        return self.__db.execute(self.__scripts["get max id"], max_id = id).fetchall()[0][0]

    def get_empl_list_db(self, company_id):
        return self.__db.execute(self.__scripts["select empl list"], id = company_id).fetchall()