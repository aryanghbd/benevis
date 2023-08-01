from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from bninterpreter import interpret
from contextlib import redirect_stdout

import os
import io

app = Flask(__name__, static_folder='../benevisreact/build')
CORS(app)  # This will enable CORS for all routes

@app.route('/', defaults={"path": ""})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

@app.route('/interpret', methods=['POST'])
def interpret_code():
    code = request.get_json().get('code')

    # Create a StringIO object to capture stdout
    buffer = io.StringIO()

    # Redirect stdout to the buffer
    with redirect_stdout(buffer):
        # Interpret the code (this should print to stdout)
        interpret(code)

    # Get the output from the buffer
    result = buffer.getvalue()

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
