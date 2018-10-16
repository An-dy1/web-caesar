from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config["DEBUG"] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px
            }
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="POST">
            <label>Rotate by:
                <input name="rot" type="text" placeholder="0" />
            </label>
            <label>
                <textarea name="text">{0}</textarea>
            </label>
            <input type="submit" value="Submit">
    </body>
</html>            
"""

@app.route("/")
def index():
    return form.format()

@app.route("/", methods=["POST"])
def encrypt():
    rot_str = request.form("rot")
    rot_int = int(rot_str)

    text = request.form("text")

    encrypted_string = rotate_string(text, rot)
    final_string = "<h1>" + encrypted_string + "</h1>"

    return form.format(final_string)

app.run()    