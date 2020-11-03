
from flask import Flask, render_template

import sys

app = Flask(__name__)

@app.route("/")
def articles():

    return render_template('index.html')



# --------pre calculation-----------
print("Server start.")
# --------end of pre calculation-----------

