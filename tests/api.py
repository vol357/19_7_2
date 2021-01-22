import requests
from settings import my_mail, my_pass, base_url, api_key
import json
import os
from requests_toolbelt.multipart.encoder import MultipartEncoder

def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

class PetFriends:
    """апи библиотека к веб приложению Pet Friends"""

    def __init__(self):
        self.base_url = base_url

    def get_api_key(self, email: str, passwd: str):
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате
        JSON с уникальным ключем пользователя, найденного по указанным email и паролем"""

        headers = {
            'email': email,
            'password': passwd,
        }
        res = requests.get(self.base_url+'api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def get_list_of_pets(self, auth_key: json, filter: str = ""):
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате JSON
        со списком наденных питомцев, совпадающих с фильтром. На данный момент фильтр может иметь
        либо пустое значение - получить список всех питомцев, либо 'my_pets' - получить список
        собственных питомцев"""

        headers = {'auth_key': api_key}
        filter = {'filter': filter}

        res = requests.get(self.base_url + 'api/pets', headers=headers, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def add_new_pet(self, auth_key: json, name: str, animal_type: str,
                    age: str, pet_photo: str) -> json:
        """Метод отправляет (постит) на сервер данные о добавляемом питомце и возвращает статус
        запроса на сервер и результат в формате JSON с данными добавленного питомца"""
        run = False
        if not is_number(age):
            print("возраст - не число")
        elif float(age)<0:
            print("неверные данные для возраста, отрицательный возраст")
        elif is_number(name):
            print("неверные данные для имени")
        elif is_number(animal_type):
            print("неверные данные для типа животного")
        elif not os.path.isfile(os.path.join(os.path.dirname(__file__), pet_photo)):
            print(f"файл "+pet_photo+" не существует по указанному пути")
        else:
            run = True
            data = MultipartEncoder(
                fields={
                  'name': name,
                  'animal_type': animal_type,
                  'age': age,
                  'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
               })
        if run:
            # headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
            headers = {'auth_key': api_key, 'Content-Type': data.content_type}
            res = requests.post(self.base_url + 'api/pets', headers=headers, data=data)
            status = res.status_code
            result = ""
            try:
               result = res.json()
            except json.decoder.JSONDecodeError:
                result = res.text
            print(result)
        else:
            status = 0
            result = "error in data"
        return status, result

    def old_add_new_pet(self, auth_key: json, name: str, animal_type: str,
                    age: str, pet_photo: str) -> json:
        """Метод отправляет (постит) на сервер данные о добавляемом питомце и возвращает статус
        запроса на сервер и результат в формате JSON с данными добавленного питомца"""
        data = MultipartEncoder(
                fields={
                  'name': name,
                  'animal_type': animal_type,
                  'age': age,
                  'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
               })

        # headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
        headers = {'auth_key': api_key, 'Content-Type': data.content_type}
        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
            #print(result)

        return status, result


    def delete_pet(self, auth_key: json, pet_id: str) -> json:
        """Метод отправляет на сервер запрос на удаление питомца по указанному ID и возвращает
        статус запроса и результат в формате JSON с текстом уведомления о успешном удалении.
        На сегодняшний день тут есть баг - в result приходит пустая строка, но status при этом = 200"""

        #headers = {'auth_key': auth_key['key']}
        headers = {'auth_key': api_key}

        res = requests.delete(self.base_url + 'api/pets/' + pet_id, headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def update_pet_info(self, auth_key: json, pet_id: str, name: str,
                        animal_type: str, age: int) -> json:
        """Метод отправляет запрос на сервер о обновлении данных питомуа по указанному ID и
        возвращает статус запроса и result в формате JSON с обновлённыи данными питомца"""

        #headers = {'auth_key': auth_key['key']}
        headers = {'auth_key': api_key}
        data = {
            'name': name,
            'age': age,
            'animal_type': animal_type
        }

        res = requests.put(self.base_url + 'api/pets/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def update_pet_photo(self, pet_id: str, pet_photo: str) -> json:
        """Метод отправляет запрос на сервер о обновлении данных питомуа по указанному ID и
        возвращает статус запроса и result в формате JSON с обновлённыи данными питомца"""

        # headers = {'auth_key': auth_key['key']}
        #headers = {'auth_key': api_key}
        #headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
        data = MultipartEncoder(
            fields={
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })
        #data = {
        #    'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
        #}
        headers = {'auth_key': api_key, 'Content-Type': data.content_type}
        res = requests.post(self.base_url + 'api/pets/set_photo/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

