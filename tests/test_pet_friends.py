from api import PetFriends
from settings import my_mail, my_pass, api_key
import os

pf = PetFriends()


# status, result = pf.get_api_key(my_mail, my_pass)
# api_key = result['key']
# print(api_key)

def test_get_api_key_for_valid_user(email=my_mail, password=my_pass):
    """ Проверяем что запрос api ключа возвращает статус 200 и в тезультате содержится слово key"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result
    assert api_key in result['key']
    # assert api_key in result
    # assert result == "'key': "+ api_key


def test_get_api_key_for_unvalid_user(email='vol2.test', password=my_pass):
    """ негатив - неверный адрес почты"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    #assert 200 < status < 500
    assert status == 403
    # 403 Forbidden («запрещено (не уполномочен)»);
    assert 'key' not in result
    # ниже проверяю - assert not 'key' in result - результат тот же
    assert "403 Forbidden" in result
    # не только статус, но и возвращаемую строку проверим


def test_get_api_key_for_no_user(email='', password=''):
        """ негатив - пустые почта и пароль"""

        # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
        status, result = pf.get_api_key(email, password)

        # Сверяем полученные данные с нашими ожиданиями
        # assert 200 < status < 500
        assert status == 403
        # 403 Forbidden («запрещено (не уполномочен)»);
        assert not 'key' in result
        assert "403 Forbidden" in result
        # не только статус, но и возвращаемую строку проверим

def test_get_all_pets_with_valid_key(filter=''):
    """ Проверяем что запрос всех питомцев возвращает не пустой список.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
    запрашиваем список всех питомцев и проверяем что список не пустой.
    Доступное значение параметра filter - 'my_pets' либо '' """

    # _, auth_key = pf.get_api_key(valid_email, valid_password)
    # !!! почему есть прочерк в строке выше: - метод возращает два значения,
    # нам нужно всего только одно, а именно -  второе

    status, result = pf.get_list_of_pets(api_key, filter)

    assert status == 200
    assert len(result['pets']) > 0


def test_add_new_pet_with_valid_data(name='случайный пес', animal_type='двортерьер',
                                     age='2', pet_photo='images/dog_random.jpeg'):
    """Проверяем что можно добавить питомца с корректными данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    # _, auth_key = pf.get_api_key(valid_email, valid_password)
    # не использую, потому что у меня сохранена глобальная переменная, чтобы не обращаться к сайт лишний раз
    # Добавляем питомца
    # status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    status, result = pf.add_new_pet(api_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_add_new_pet_with_big_data(name='случайный пес случайный пес случайный пес случайный пес случайный пес случайный пес случайный пес случайный пес', animal_type='двортерьер',
                                     age='2347593745923409273925747569476845769845674975927592457.94586798457693745', pet_photo='images/dog_random.jpeg'):
    """можно ли добавить питомца с корректными, но большими данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    # _, auth_key = pf.get_api_key(valid_email, valid_password)
    # не использую, потому что у меня сохранена глобальная переменная, чтобы не обращаться к сайт лишний раз
    # Добавляем питомца
    # status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    status, result = pf.add_new_pet(api_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_add_new_pet_without_name(name='', animal_type='двортерьер',
                                     age='2', pet_photo='images/dog_random.jpeg'):
    """можно ли добавить питомца с пустым именем"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    # _, auth_key = pf.get_api_key(valid_email, valid_password)
    # не использую, потому что у меня сохранена глобальная переменная, чтобы не обращаться к сайт лишний раз
    # Добавляем питомца
    # status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    status, result = pf.add_new_pet(api_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name



def test_add_new_pet_with_no_exist_file_photo(name='случайный пес', animal_type='двортерьер',
                                     age='2', pet_photo='images/dg_random.jpeg'):
    """можно ли добавить питомца с несуществующим файлом фото"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    # _, auth_key = pf.get_api_key(valid_email, valid_password)
    # не использую, потому что у меня сохранена глобальная переменная, чтобы не обращаться к сайт лишний раз
    # Добавляем питомца
    # status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    status, result = pf.add_new_pet(api_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 0

def test_add_new_pet_with_age_str(name='случайный пес', animal_type='двортерьер',
                                     age='dfjgh', pet_photo='images/dog_random.jpeg'):
    """можно ли добавить питомца с нечисловым возрастом по старому методу добавления"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    # _, auth_key = pf.get_api_key(valid_email, valid_password)
    # не использую, потому что у меня сохранена глобальная переменная, чтобы не обращаться к сайт лишний раз
    # Добавляем питомца
    # status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    status, result = pf.old_add_new_pet(api_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_with_age_str1(name='случайный пес', animal_type='двортерьер',
                                     age='dfjgh', pet_photo='images/dog_random.jpeg'):
    """можно ли добавить питомца с нечисловым возрастом с новым методом добавления"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    # _, auth_key = pf.get_api_key(valid_email, valid_password)
    # не использую, потому что у меня сохранена глобальная переменная, чтобы не обращаться к сайт лишний раз
    # Добавляем питомца
    # status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    status, result = pf.add_new_pet(api_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 0


def test_add_new_pet_with_without_photo_data(name='случайный пес', animal_type='двортерьер',
                                     age='2'):
    """Проверяем что можно добавить питомца без фото"""


    # Запрашиваем ключ api и сохраняем в переменую auth_key
    # _, auth_key = pf.get_api_key(valid_email, valid_password)
    # не использую, потому что у меня сохранена глобальная переменная, чтобы не обращаться к сайт лишний раз
    # Добавляем питомца
    # status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    status, result = pf.add_new_pet(api_key, name, animal_type, age,'')

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 0
    # фото - обязательно, поэтому должно возвращать 0 (file not exist)


def test_successful_delete_self_pet():
    """Проверяем возможность удаления питомца"""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    # _, auth_key = pf.get_api_key(valid_email, valid_password)
    # _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    _, my_pets = pf.get_list_of_pets(api_key, "my_pets")

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        # pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/dog_random.jpeg")
        pf.add_new_pet(api_key, "СуперПес", "пес", "3", "images/dog_random.jpeg")
    # _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    # status, _ = pf.delete_pet(auth_key, pet_id)
    status, _ = pf.delete_pet(api_key, pet_id)

    # Ещё раз запрашиваем список своих питомцев
    # _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    _, my_pets = pf.get_list_of_pets(api_key, "my_pets")

    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()


def test_successful_update_self_pet_info(name='Мурзик', animal_type='Котэ', age=5):
    """Проверяем возможность обновления информации о питомце"""

    # Получаем ключ auth_key и список своих питомцев
    # _, auth_key = pf.get_api_key(valid_email, valid_password)
    # _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    _, my_pets = pf.get_list_of_pets(api_key, "my_pets")

    # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(api_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert result['name'] == name
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")


def test_update_photo(photo='images/dog2_random.jpeg'):
    """изменение фото питомца последней моей"""
    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    photo = os.path.join(os.path.dirname(__file__), photo)

    # Получаем список своих питомцев
    _, my_pets = pf.get_list_of_pets(api_key, "my_pets")

    # Если список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_photo( my_pets['pets'][0]['id'], photo)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")



def test_successful_delete_all_self_pet():
    """ удаление всех моих питомцев"""

    # запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(api_key, "my_pets")
    # Проверяем - если список своих питомцев не пустой, то запускаем цикл на удаление, иначе - выходим
    i = len(my_pets['pets'])
    if i > 0:
        k = 0
        while k < i:
            # Берём k-ого питомца из списка и отправляем запрос на удаление
            pet_id = my_pets['pets'][k]['id']
            status, _ = pf.delete_pet(api_key, pet_id)
            assert status == 200
            k += 1
        # Ещё раз запрашиваем список своих питомцев
        _, my_pets = pf.get_list_of_pets(api_key, "my_pets")
        i = len(my_pets['pets'])
        if i == 0:
            assert i == 0
    else:
        assert i == 0
