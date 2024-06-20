import allure
import requests
from typing import Dict, Any

class EmployeesApi:
    def __init__(self, url: str) -> None:
        self.url = url

    @allure.step("api.Создание компании {name}:{description}")
    def create_company(self, name: str, description: str = "") -> Dict[str, Any]:
        company = {
            'name': name,
            'description': description
        }
        my_headers = {}
        my_headers['x-client-token'] = self.get_token()
        resp = requests.post(self.url + '/company', json=company, headers=my_headers)
        return resp.json()

    @allure.step("api.Получение компании по {id}")
    def get_company(self, id: int) -> Dict[str, Any]:
        resp = requests.get(self.url + '/company/' + str(id))
        return resp.json()

    @allure.step("api.Получение сотрудника по {id}")
    def get_employee(self, id: int) -> Dict[str, Any]:
        resp = requests.get(self.url + '/employee/' + str(id))
        return resp.json()

    @allure.step("api.Получение списка сотрудников компании {companyId}")
    def get_employees_list(self, companyId: int) -> Dict[str, Any]:
        params = {'company': companyId}
        resp = requests.get(self.url + '/employee', params=params)
        return resp.json()

    @allure.step("API.Получение токена авторизации {user}:{password}")
    def get_token(self, user: str = 'bloom', password: str = 'fire-fairy') -> str:
        """
        Получение токена авторизации
        :params user(str): логин 
        :params password(str): пароль 

        :return: str: token
        """
        creds = {
           'username': user,
           'password': password
        }
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()['userToken']

    @allure.step("api.Добавление нового сотрудника {firstName}:{lastName}:{middleName}:{companyId}:{email}:{url}:{phone}:{birthdate}:{isActive}")
    def create_employee(self, firstName: str, lastName: str, middleName: str, companyId: int, email: str, url: str, phone: int, birthdate: str, isActive: bool) -> Dict[str, Any]:
        employee = {
            'firstName': firstName,
            'lastName': lastName,
            'middleName': middleName,
            'companyId': companyId,
            'email': email,
            'url': url,
            'phone': phone,
            'birthdate': birthdate,
            'isActive': isActive
        }
        my_headers = {}
        my_headers['x-client-token'] = self.get_token()
        resp = requests.post(self.url + '/employee', json=employee, headers=my_headers)
        return resp.json()

    @allure.step("api.Редактирование сотрудника {new_lastName}:{new_email}:{new_url}:{new_phone}:{new_isActive}:{id}")
    def edit_employee(self, new_lastName: str, new_email: str, new_url: str, new_phone: int, new_isActive: bool, id: int) -> Dict[str, Any]:
        employee = {
            'lastName': new_lastName,
            'email': new_email,
            'url': new_url,
            'phone': new_phone,
            'isActive': new_isActive
        }
        my_headers = {'x-client-token': self.get_token()}
        resp = requests.patch(self.url + '/employee/' + str(id), headers=my_headers, json=employee)
        return resp.json()

    @allure.step("api.Удаление сотрудника по {id}")
    def delete_employee(self, id: int) -> Dict[str, Any]:
        my_headers = {'x-client-token': self.get_token()}
        resp = requests.delete(self.url + f'/employee/{id}', headers=my_headers)
        return resp.json()