from flask import Flask, request, redirect, url_for, send_from_directory
import os

# Create uploads directory if it doesn't exist
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <h1>Upload Image</h1>
    <form method="post" action="/upload" enctype="multipart/form-data">
        <input type="file" name="image" accept="image/*">
        <input type="submit" value="Upload">
    </form>
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
    
    if file:
        # Just use the original filename directly
        filename = file.filename
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        return redirect(url_for('view_file', filename=filename))

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    print(f"Serving file: {filename}")
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route("/view/<filename>")
def view_file(filename):
    image_url = url_for('uploaded_file', filename=filename)
    return f"""
    <h1>File Uploaded Successfully</h1>
    <img src="{image_url}" alt="Uploaded Image">
    <p>Image path: {image_url}</p>
    """

if __name__ == "__main__":
    app.run(debug=True)