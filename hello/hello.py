# SPDX-FileCopyrightText: 2019-2020 Magenta ApS
# SPDX-License-Identifier: MPL-2.0

from flask import Flask
import xmlsec

# We don't actually need anything from xmlsec, but we wan't to make sure it is
# installed.
manager = xmlsec.KeysManager()

app = Flask(__name__)


@app.route("/")
def hello():
    return f"Hello, World!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
