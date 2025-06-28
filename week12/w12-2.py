from flask import Flask, request, redirect, url_for, send_from_directory
import os
from werkzeug.utils import secure_filename

# Configuration
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'week12/uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB limit

# Create uploads directory if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def index():
    return """
    <h1>Upload Image</h1>
    <form method="post" action="/upload" enctype="multipart/form-data">
        <input type="file" name="image" accept="image/*">
        <input type="submit" value="Upload">
    </form>
    <p>Allowed file types: jpg, jpeg, png, gif</p>
    <p>Maximum file size: 16 MB</p>
    """

@app.route("/upload", methods=["GET", "POST"])
def upload_image():
    if request.method == "GET":
        return redirect(url_for('index'))
    
    # This is a POST request
    if 'image' not in request.files:
        return "No file part", 400
    
    file = request.files['image']
    if file.filename == '':
        return "No selected file", 400
    
    if file and allowed_file(file.filename):
        # Secure the filename to prevent path traversal attacks
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('view_file', filename=filename))
    else:
        return "Invalid file type. Allowed types: jpg, jpeg, png, gif", 400

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route("/view/<filename>")
def view_file(filename):
    image_url = url_for('uploaded_file', filename=filename)
    return f"""
    <h1>File Uploaded Successfully</h1>
    <img src="{image_url}" alt="Uploaded Image" style="max-width: 800px;">
    <p>Image path: {image_url}</p>
    <p><a href="/">Upload another image</a></p>
    """

if __name__ == "__main__":
    app.run(debug=True)