![Valorant banner](valorant-banner.jpeg)

# 🎮 Valorant Agent Viewer

A simple **Python GUI application** built with **Tkinter** and **Pillow (PIL)** that displays detailed information and images of agents from **Valorant**.
The project demonstrates **Object-Oriented Programming (OOP)**, GUI development, and image handling in Python through a clean and structured design.

---

## 🌟 Features

- 🎯 Browse all Valorant agents via an interactive dropdown menu.
- 📄 Display detailed agent information, including:
  - Name
  - Age
  - Role (Category)
  - Origin (Country)
  - Abilities
  - Description
- 🖼️ Display agent images dynamically alongside the information.
- ⚠️ Gracefully handles missing or unavailable images.

---

##  🖼️ Screenshots

<details>
<summary>Dashboard Image</summary>

The main dashboard showing the image and agent information:

![Dashboard Screenshot](ss-jett.jpeg)

</details>

---
## 📂 File Structure
``` 
Valorant-Agent-Viewer/        <-- Root project folder
├─ images/                    <-- Folder for all agent images
│  ├─ Brimstone.jpeg
│  ├─ Phoenix.jpeg
│  ├─ Sage.jpeg
│  ├─ ss-jett.jpeg
│  └─ ... (other agent images)
├─ main.py                    <-- Your main Python GUI code
└─ README.md                  <-- Project documentation
```

## 🚀 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/DevGopi-17/valorant-agent-viewer.git
cd valorant-agent-viewer
```

---

### 2️⃣ Create a Virtual Environment (Recommended)

#### 🔹 macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 🔹 Windows
```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install pillow
```

> Tkinter comes pre-installed with standard Python installations.

---

### 4️⃣ Run the Application

```bash
python main.py
```
---
### ✅ Requirements

- Python 3.10+
- Pillow
