import toml
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)

        data = toml.loads(content)
        print(data)

        name = data["tool"]["poetry"]["name"]
        description = data["tool"]["poetry"].get("description", "No description")
        dependencies = list(data["tool"]["poetry"]["dependencies"].keys())
        dev_dependencies = list(data["tool"]["poetry"].get("dev-dependencies", {}).keys())

        return Project(name, description, dependencies, dev_dependencies)