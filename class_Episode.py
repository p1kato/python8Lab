
class Episode:
    def __init__(self, dauletsuper):
        self.id = dauletsuper.get("id")
        self.name = dauletsuper.get("name")
        self.air_date = dauletsuper.get("air_date")
        self.episode = dauletsuper.get("episode")
        self.characters = dauletsuper.get("characters", [])
        self.url = dauletsuper.get("url")
        self.created = dauletsuper.get("created")

    def __str__(self):
        return f"Episode ID: {self.id}\n" \
               f"Episode Name: {self.name}\n" \
               f"Air Date: {self.air_date}\n" \
               f"Episode Code: {self.episode}\n" \
               f"Characters: {self.characters}\n" \
               f"URL: {self.url}\n" \
               f"Created: {self.created}\n"

    def __del__(self):
        return f"Deleted {self.id}"
