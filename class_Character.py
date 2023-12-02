
class Character:
    def __init__(self, character_data):
        self.id = character_data.get("id")
        self.name = character_data.get("name")
        self.status = character_data.get("status")
        self.species = character_data.get("species")
        self.type = character_data.get("type")
        self.gender = character_data.get("gender")
        self.origin = character_data.get("origin", {})
        self.location = character_data.get("location", {})
        self.image = character_data.get("image")
        self.created = character_data.get("created")

    def __str__(self):
        return f"Character ID: {self.id}\n" \
               f"Name: {self.name}\n" \
               f"Status: {self.status}\n" \
               f"Species: {self.species}\n" \
               f"Type: {self.type}\n" \
               f"Gender: {self.gender}\n" \
               f"Origin: {self.origin}\n" \
               f"Location: {self.location}\n" \
               f"Image: {self.image}\n" \
               f"Created: {self.created}\n"

    def is_alive(self):
        return self.status.lower() == "alive"

    def relocate(self, new_location):
        self.location = new_location
