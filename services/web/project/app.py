import json

from flask import request

from . import create_app, database
from .models import Projects

app = create_app()


@app.route("/", methods=["GET"])
def fetch():
    projects = database.get_all(Projects)
    all_projects = []
    for project in projects:
        new_project = {
            "id": project.id,
            "name": project.name,
            "description": project.description,
            "tags": project.tags,
            "hourly_rate": project.hourly_rate,
        }

        all_projects.append(new_project)
    return json.dumps(all_projects), 200


@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    name = data["name"].strip()
    description = data["description"].strip()
    tags = data["tags"]
    hourly_rate = data["hourly_rate"].strip()

    database.add_instance(
        Projects,
        name=name,
        description=description,
        tags=tags,
        hourly_rate=hourly_rate,
    )

    return json.dumps("added"), 200


@app.route("/remove/<project_id>", methods=["DELETE"])
def remove(project_id):
    database.delete_instance(Projects, id=project_id)
    return json.dumps("removed"), 200


@app.route("/edit/<project_id>", methods=["PATCH"])
def edit(project_id):
    data = request.get_json()
    new_hourly_rate = data["hourly_rate"]
    database.edit_instance(Projects, id=project_id, hourly_rate=new_hourly_rate)
    return json.dumps("updated"), 200
