import json

from service import service
from LogicClasses.App import App

with open("file.json", "r") as file:
    json_text = file.read()
    data = json.loads(json_text)
    app = App(**data)

service(app)