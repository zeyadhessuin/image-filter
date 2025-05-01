import os
import shutil
import csv
from flask import Flask, render_template, request, jsonify
from tkinter import Tk, filedialog, messagebox
import threading
import webbrowser

app = Flask(__name__)
input_folder = ""
output_folder = ""
UPLOAD_FOLDER = "static/uploads"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/load_images')
def load_images():
    image_names = []
    if not os.path.exists(input_folder):
        return jsonify({'images': []})

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    for f in os.listdir(UPLOAD_FOLDER):
        os.remove(os.path.join(UPLOAD_FOLDER, f))

    for fname in os.listdir(input_folder):
        if fname.lower().endswith(".jpg"):
            shutil.copy(os.path.join(input_folder, fname), os.path.join(UPLOAD_FOLDER, fname))
            image_names.append(fname)

    return jsonify({'images': image_names})

@app.route('/export', methods=['POST'])
def export():
    selected = request.json['selected']
    os.makedirs(output_folder, exist_ok=True)

    csv_path = os.path.join(output_folder, "selected_images.csv")
    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Image Name"])
        for img in selected:
            writer.writerow([img])
            shutil.copy(os.path.join(input_folder, img), os.path.join(output_folder, img))
    return jsonify({"message": f"Exported {len(selected)} images and saved CSV."})

def start_flask():
    app.run(debug=False)

def select_folders():
    global input_folder, output_folder
    root = Tk()
    root.withdraw()

    messagebox.showinfo("Info", "Select the input folder with JPG images, then select an output folder for saving results.")

    input_folder = filedialog.askdirectory(title="Select Input Folder (with JPGs)")
    if not input_folder:
        print("Input folder not selected.")
        return

    output_folder = filedialog.askdirectory(title="Select Output Folder")
    if not output_folder:
        print("Output folder not selected.")
        return

    threading.Thread(target=start_flask).start()
    webbrowser.open("http://127.0.0.1:5000")

if __name__ == "__main__":
    select_folders()