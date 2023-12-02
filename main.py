import requests
import random


def task_1():
    post_id = 1

    class ToDo:
        def __init__(self, userId, id, title, completed):
            self.userId = userId
            self.id = id
            self.title = title
            self.completed = completed

    url = f'https://jsonplaceholder.typicode.com/todos/{post_id}'

    response = requests.get(url)
    todo = response.json()

    new_ToDo = ToDo(
        userId=todo['userId'],
        id=todo['id'],
        title=todo['title'],
        completed=todo['completed']
    )

    # Converted JSON file to dict

    studentDias = {
        'userId': new_ToDo.userId,
        'id': new_ToDo.id,
        'title': new_ToDo.title,
        'completed': new_ToDo.completed
    }

    # Posted the request
    post_requests = requests.post('https://jsonplaceholder.typicode.com/todos/', json=studentDias)

    print(post_requests.json())

    if post_requests.status_code >= 400:
        print('Error')


# task_1()


def task_4():
    post_id = 1

    class ToDo:
        def __init__(self, userId, id, title, completed):
            self.userId = userId
            self.id = id
            self.title = title
            self.completed = completed

    url = f'https://jsonplaceholder.typicode.com/todos/{post_id}'

    response = requests.get(url)
    todo = response.json()

    new_ToDo = ToDo(
        userId=todo['userId'],
        id=todo['id'],
        title=todo['title'],
        completed=todo['completed']
    )

    # Edit our title and completed
    new_title = 'dauletsuper'

    new_ToDo.title = new_title
    new_ToDo.completed = not new_ToDo

    random_id = random.randint(1, 15)

    # Converted JSON file to dict

    dauletsuper = {
        'userId': new_ToDo.userId,
        'id': random_id,
        'title': new_ToDo.title,
        'completed': new_ToDo.completed
    }

    # Posted the request
    post_requests = requests.post('https://jsonplaceholder.typicode.com/todos/', json=dauletsuper)

    print(post_requests.json())

    if post_requests.status_code >= 400:
        print('Error')


def task_6():
    post_id = 1

    class ToDo:
        def __init__(self, userId, id, title, completed):
            self.userId = userId
            self.id = id
            self.title = title
            self.completed = completed

    url = f'https://jsonplaceholder.typicode.com/todos/{post_id}'

    response = requests.get(url)
    todo = response.json()

    new_ToDo = ToDo(
        userId=todo['userId'],
        id=todo['id'],
        title=todo['title'],
        completed=todo['completed']
    )

    # Edit our title and completed
    new_title = 'dauletsuper'

    new_ToDo.title = new_title
    new_ToDo.completed = not new_ToDo

    random_id = random.randint(1, 15)

    # Converted JSON file to dict

    dauletsuper = {
        'userId': new_ToDo.userId,
        'id': random_id,
        'title': new_ToDo.title,
        'completed': new_ToDo.completed
    }
    chosen_id = 2
    response_put = requests.put(f'https://jsonplaceholder.typicode.com/todos/{chosen_id}', json=dauletsuper)

    print(response_put.json())
    if response_put.status_code >= 400:
        print('Error!')


# task_6()


def task2_1():
    random_id = random.randint(1, 826)

    response = requests.get(f'https://rickandmortyapi.com/api/character/{random_id}')

    print(response.json())
    text_response = response.text

    def task2_3():
        with open('character(punk under my skin).txt', 'w') as file:
            file.write(text_response)

    # task2_3()


# task2_1()

def task2_4():
    random_id = random.randint(1, 826)

    response = requests.get(f'https://rickandmortyapi.com/api/episode/{random_id}')

    episode = ["https://rickandmortyapi.com/api/episode/10",
               "https://rickandmortyapi.com/api/episode/28",
               f"https://rickandmortyapi.com/api/episode/{random_id}"]

    with open('all episode with character(punk under my skin).txt', 'w') as file:
        for string in episode:
            file.write(string + '\n')


# task2_4()


def task2_5():
    response = requests.get(url='https://rickandmortyapi.com/api/episode/1')

    dauletsuper = response.json()

    for k, v in dauletsuper.items():
        # if k == 'name':
        print(f'{k}: {type(v).__name__}')


# task2_5()

def task2_7():
    from class_Episode import Episode

    def augustus(id):
        response = requests.get(f'https://rickandmortyapi.com/api/character/{id}')
        dauletsuper = response.json()
        return Episode(dauletsuper)

    lists = []

    for x in range(1, 15):
        random_id = random.randrange(1, 826)
        lists.append(augustus(random_id))

    for y in lists:
        print(f"Episode ID: {y.id}")
        print(f"Episode Name: {y.name}")
        print(f"Air Date: {y.air_date}")
        print(f"Episode Code: {y.episode}")
        print(f"Characters: {y.characters}")
        print(f"URL: {y.url}")
        print(f"Created: {y.created}")
        print("-------------------------------------")


# task2_7()

def task2_8():
    import class_Episode
    del class_Episode.Episode


def task2_9():
    id = random.randrange(1, 826)
    response = requests.get(f'https://rickandmortyapi.com/api/character/{id}')
    dauletsuper = response.json()
    print(dauletsuper)


# task2_9()

def task2_11():
    from class_Character import Character

    def get_random_character_data():
        response = requests.get("https://rickandmortyapi.com/api/character/1")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Unable to fetch character data. Status code: {response.status_code}")
            return None

    character_data = get_random_character_data()
    if character_data:
        random_character = Character(character_data)
        print(random_character)

        def task2_12():
            random_character = Character(character_data)
            print(random_character)

            # Example of using methods
            print(f"Is {random_character.name} alive? {'Yes' if random_character.is_alive() else 'No'}")

            new_location = {"name": "New Location"}
            random_character.relocate(new_location)
            print(f"{random_character.name} has been relocated to {random_character.location['name']}")