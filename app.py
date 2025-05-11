from flask import Flask, send_from_directory, abort
import os

app = Flask(__name__)

# Root directory for static media
BASE_UPLOAD_DIR = '/home/ec2-user/uploads/blog/section'

# Allowed top-level categories
ALLOWED_CATEGORIES = ['project', 'tech', 'life', 'Research']

@app.route('/')
def home():
    return "<h1> Welcome to the server </h1>"


@app.route('/blog/section/<category>/<subfolder>/<filename>')
def serve_file(category, subfolder, filename):
    if category not in ALLOWED_CATEGORIES:
        abort(404, description="Category not found.")

    # Build path to the requested file
    dir_path = os.path.join(BASE_UPLOAD_DIR, category, subfolder)
    file_path = os.path.join(dir_path, filename)

    if os.path.isfile(file_path):
        return send_from_directory(directory=dir_path, path=filename)
    else:
        abort(404, description="File not found.")

# Gunicorn will use this
app_wsgi = app

if __name__ == '__main__':
    
    app.run(debug=True, host='0.0.0.0', port=8080)

