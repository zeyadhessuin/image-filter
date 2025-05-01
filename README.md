# 📸 Image Selection Tool (Folder-Based with Web UI)

This project is a Python + Flask desktop tool that lets you:

- Select **input and output folders** from your OS.
- View `.jpg` images in a **scrollable web UI**, 4 per page.
- **Select images** across multiple pages (selections are remembered).
- Save:
  - A CSV file with selected image filenames.
  - Copies of selected images into the output folder.

## 🔧 Features

- Folder selection via a GUI popup (Tkinter).
- Responsive web interface (Flask + HTML + JS).
- Pagination (4 images per page).
- Remember selections across pages.
- CSV export + image file copy.

---

## 🚀 How to Run

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/image-selection-tool.git
cd image-selection-tool
pip install -r requirements.txt