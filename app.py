import os

from marshmallow.exceptions import ValidationError  # type: ignore
from flask import Flask, request, abort

from classes.command import Commands, CommandsSchema
from classes.search import Search
from config import DATA_DIR

app = Flask(__name__)


@app.route("/perform_query/", methods=['POST'])
def perform_query():  # type: ignore
    try:
        commands: Commands = CommandsSchema().load(request.json)
        if not os.path.exists(DATA_DIR):
            raise FileNotFoundError('Передано неверное имя файла')

        # Выполнять переданные команды и возвращать результаты в ответ
        with open(DATA_DIR, 'r') as file:
            cmd1_result = getattr(Search, commands.cmd1)(file, commands.value1)
            cmd2_result = getattr(Search, commands.cmd2)(cmd1_result, commands.value2)
            return app.response_class(cmd2_result, content_type="text/plain")

    except (ValueError, FileNotFoundError, TypeError, IndexError, ValidationError) as e:
        abort(400, e)


if __name__ == '__main__':
    app.run(debug=True)
