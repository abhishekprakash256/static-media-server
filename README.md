# static-media-server

A lightweight Flask-based server to host and serve static media (images, videos, files) organized by category. Designed for personal portfolios or small projects, deployable on an EC2 instance or any Linux server.

## 🚀 Features

- Serve static media files from categorized folders like `project`, `tech`, `life`
- Dynamic routing to access files via URL paths
- Easy integration with portfolio frontends
- Compatible with SCP for bulk uploads
- Lightweight and easy to deploy (no database or external storage needed)

## 📁 Folder Structure

On your EC2 or server:

```

uploads/
└── blog/
    └── section/
        ├── project/
        │   ├── ai/
        │   └── web/
        ├── tech/
        │   ├── flask/
        │   └── docker/
        ├── life/
        │   ├── philosphy/
        │   └── docker/
        ├── Research/
        ├── travel/
        └── food/


```

## 🌐 Example Routes

```

/blog/section/project/ai/your_image.jpg
/blog/section/tech/docker/docker101.png
/blog/section/life/philosphy/thoughts.png
/blog/section/travel/europe-trip.png


```

Each URL maps to a file in the server like:

```

/uploads/blog/section/<category>/<subfolder>/<filename>


````

## ⚙️ Setup & Run

1. **Clone the repo**

```bash
git clone https://github.com/your-username/static-media-server.git
cd static-media-server
````

2. **Install dependencies**

```bash
pip install flask
```

3. **Edit configuration**

Update the `BASE_UPLOAD_DIR` in `app.py` to match your file storage path.

4. **Run the server**

```bash
python app.py

flask run --host=0.0.0.0 --port=8080

```

Or for production:

```bash
gunicorn -w 4 -b 0.0.0.0:8080 app:app_wsgi

```

## 📤 Uploading Files (From Local)

Use `scp` to upload:

```bash
scp path/to/image.jpg ec2-user@your-ec2-ip:/home/ec2-user/uploads/blog/section/project/ai/

```

## 🛡️ Optional Enhancements

* Add authentication for private access
* Use NGINX as reverse proxy for better performance
* Add logging or analytics
* Dockerize for easier deployment



