import numpy as np
from flask import Flask, request, jsonify, render_template, session, redirect, Response

from weather_main import *

app = Flask(__name__)

weather_df = combined_df

"""
render the html page
"""
@app.route('/', methods=("POST", "GET"))
def html_table():
    return render_template('index.html',  tables=[weather_df.to_html(classes='data', header="true")])

"""
render the json data
"""
@app.route('/api')
def api_table():
    return Response(weather_df.to_json(orient="records"), mimetype='application/json')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9090)