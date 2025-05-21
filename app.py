from flask import Flask,request, jsonify, send_from_directory, abort
from flask_cors import cross_origin  # Not CORS app-wide
import os

app = Flask(__name__)

# Root directory for static media
BASE_UPLOAD_DIR = './blog/section'  # Make sure this is correct

# Allowed top-level categories
ALLOWED_CATEGORIES = ['project', 'tech', 'life', 'Research']


@app.route('/')
def home():
    """
    Home route to check the server status.
    
    Returns:
        str: A simple HTML string greeting the user.
    """
    return "<h1> Welcome to the server </h1>"  


@app.route('/message/submit', methods=['POST'])
@cross_origin()  # Allow CORS on this route only
def api():
    data = request.get_json()
    if not data:
        
        return jsonify({"error": "No data provided"}), 400

    print({"message": "Data received", "data": data})
    
    return jsonify({"message": "Data received", "data": data}), 200



@app.route('/blog/section/<category>/<subfolder>/<path:filename>', methods=['GET'])
def serve_file(category, subfolder, filename):
    """
    Serve a requested file from the static media directory.

    This route checks if the requested category is valid and if the file exists in the
    corresponding folder. If both conditions are met, the file is served to the client.
    Otherwise, a 404 error is raised.

    Args:
        category (str): The category of the file (e.g., 'project', 'tech', etc.).
        subfolder (str): The subfolder where the file is stored.
        filename (str): The name of the file to be served.

    Returns:
        Response: A Flask response containing the file if it exists, or a 404 error if not.

    Raises:
        404: If the category is not allowed or the file does not exist.
    """
    
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
    """
    Starts the Flask application server for local development.

    This is only used when running the app directly and is not required in a production environment.
    The server listens on all available interfaces (0.0.0.0) and uses port 8080.
    """
    app.run(debug=True, host='0.0.0.0', port=8080)
