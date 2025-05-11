from flask import Flask, send_from_directory, abort
import os

app = Flask(__name__)

# Root directory for static media
BASE_UPLOAD_DIR = './blog/section'  # Make sure this is correct

# Allowed top-level categories
ALLOWED_CATEGORIES = ['project', 'tech', 'life', 'Research']

@app.route('/')
def home():
    return "<h1> Welcome to the server </h1>"


@app.route('/static/<filename>')
def serve_static_file(filename):
    """
    The test route to serve static files from the 'static' directory.
    """

    print("in serve_static_file")  # Debug print to check if this route is hit

    return send_from_directory('static', filename)


@app.route('/blog/section/<category>/<subfolder>/<filename>', methods=['GET'])
def serve_file(category, subfolder, filename):

    print("in blog function")  # Debug print to check if this route is hit

    if category not in ALLOWED_CATEGORIES:
        abort(404, description="Category not found.")

    # Build path to the requested file
    dir_path = os.path.join(BASE_UPLOAD_DIR, category, subfolder)
    file_path = os.path.join(dir_path, filename)

    print(f"Requested File Path: {file_path}")  # Debug print to check the path

    if os.path.isfile(file_path):
        print(f"File exists at {file_path}")  # Debug print if file exists
        return send_from_directory(directory=dir_path, path=filename)
    else:
        print(f"File not found at {file_path}")  # Debug print if file doesn't exist
        abort(404, description="File not found.")

# Gunicorn will use this
app_wsgi = app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
