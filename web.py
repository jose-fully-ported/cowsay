"""
starts a web process
"""
import os
import random

from cowsay import cowsay
from cowsay import get_random_cow
from flask import Flask
from flask import redirect

from shared import consume_cpu
from shared import consume_memory

app = Flask(__name__)

status_codes = {
    1: 100,
    2: 200,
    3: 201,
    4: 202,
    5: 200,
    6: 200,
    7: 200,
    8: 302,
    9: 404,
    10: 500,
}


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def index(path):
    """
    default catch-all path
    """
    consume_cpu()
    consume_memory()

    status_code = status_codes[random.randint(1, 10)]
    if status_code == 301:
        return redirect("http://www.example.com", code=302)

    cow = get_random_cow()
    message = f"Hello, World! Welcome to /{path} ({status_code})"
    html = f"<pre><code>{cowsay(message, cow=cow)}</code></pre>"
    return html, status_code


@app.route("/env")
def printenv():
    """
    prints the env as json
    """

    return dict(os.environ)


if __name__ == "__main__":
    app.run()
