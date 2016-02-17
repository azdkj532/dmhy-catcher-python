import json
from bottle import Bottle, run, request

from db import Task, Resource
from dmhy import dmhy

app = Bottle()


@app.route('/task')
def task_list():
    tasks = [task for task in Task.select().dicts()]
    return json.dumps({"task_list": tasks}, ensure_ascii=False)


@app.route('/resource')
def resource_list():
    resources = [_ for _ in Resource.select().dicts()]
    return json.dumps({"resource": resources}, ensure_ascii=False)


@app.route('/search')
def search():
    keyword = request.query.get('q', '')
    res = [{"title": topic.title, "last_update": topic.date} for topic in dmhy.Search(keyword)]
    return json.dumps({"resource": res}, ensure_ascii=False)


run(app, host='localhost', port=8080)
