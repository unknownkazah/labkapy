import requests
import random
import json

class ToDo:
    def __init__(self, userId, id, title, completed):
        self.userId = userId
        self.id = id
        self.title = title
        self.completed = completed

    def __repr__(self):
        return f"ToDo ID: {self.id}, Title: {self.title}, Completed: {self.completed}"

class Character:
    def __init__(self, character_data):
        self.id = character_data['id']
        self.name = character_data['name']
        self.status = character_data['status']
        self.species = character_data['species']
        self.type = character_data['type']
        self.gender = character_data['gender']
        self.origin = character_data['origin']
        self.location = character_data['location']
        self.image = character_data['image']
        self.episode = character_data['episode']
        self.url = character_data['url']
        self.created = character_data['created']

    def __repr__(self):
        return f"Character ID: {self.id}, Name: {self.name}, Status: {self.status}, Species: {self.species}, " \
               f"Type: {self.type}, Gender: {self.gender}, Origin: {self.origin}, Location: {self.location}"
# Task 1
post_id = 1  # Replace this with the desired post ID
response = requests.get(f'https://jsonplaceholder.typicode.com/todos/{post_id}')

if response.status_code >= 400:
    print(f"Error: {response.status_code} - {response.text}")
else:
    todo_data = response.json()
    print("Response Content (JSON):", todo_data)

    new_todo = ToDo(userId=todo_data['userId'], id=todo_data['id'],
                    title=todo_data['title'], completed=todo_data['completed'])

    new_todo_dict = {
        "userId": new_todo.userId,
        "title": new_todo.title,
        "completed": new_todo.completed
    }

    post_response = requests.post('https://jsonplaceholder.typicode.com/todos', json=new_todo_dict)

    if post_response.status_code >= 400:
        print(f"Error: {post_response.status_code} - {post_response.text}")
    else:
        print("POST Response Content:", post_response.json())

        new_todo.title = "Updated Title"

        put_todo_dict = {
            "userId": new_todo.userId,
            "id": new_todo.id,
            "title": new_todo.title,
            "completed": new_todo.completed
        }

        chosen_id = 1  # Replace this with the chosen todo item ID to update
        put_response = requests.put(f'https://jsonplaceholder.typicode.com/todos/{chosen_id}', json=put_todo_dict)

        if put_response.status_code >= 400:
            print(f"Error: {put_response.status_code} - {put_response.text}")
        else:
            print("PUT Response Content:", put_response.json())

# Task 2
random_character_id = random.randint(1, 826)
character_url = f'https://rickandmortyapi.com/api/character/{random_character_id}'
character_response = requests.get(character_url)

if character_response.status_code == 200:
    character_data = character_response.json()
    print("JSON Response:")
    print(json.dumps(character_data, indent=4))  # Вывести ответ в формате JSON
    print("\nKeys of the JSON Structure:")
    print(character_data.keys())  # Вывести ключи структуры JSON

    # Save to File
    with open(f"info_character_{random_character_id}.json", "w") as character_file:
        json.dump(character_data, character_file, indent=4)

    # Episode List
    episode_urls = character_data['episode']
    episode_ids = [int(url.split('/')[-1]) for url in episode_urls]

    with open(f"all_episodes_with_character_{random_character_id}.txt", "a") as episode_file:
        for url in episode_urls:
            episode_file.write(url + "\n")

    # Episode Data Retrieval
    episode_objects = []
    for episode_id in episode_ids:
        episode_url = f'https://rickandmortyapi.com/api/episode/{episode_id}'
        episode_response = requests.get(episode_url)
        if episode_response.status_code == 200:
            episode_info = episode_response.json()
            episode_objects.append(episode_info)

    # Character Response Structure
    character_structure_response = requests.get('https://rickandmortyapi.com/api/character/1')
    if character_structure_response.status_code == 200:
        character_structure = character_structure_response.json()
        print("\nCharacter Response Structure:")
        print(json.dumps(character_structure, indent=4))

        # Character Object Creation
        random_character = Character(character_data)
        print("\nRandom Character Information:")
        print(random_character)

        # Display Episodes Information
        print("\nEpisodes Information:")
        for episode_obj in episode_objects:
            print(json.dumps(episode_obj, indent=4))

else:
    print(f"Failed to retrieve character. Status code: {character_response.status_code}")
