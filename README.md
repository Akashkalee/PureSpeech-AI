# 🎙️ PureSpeech AI

An institutional-grade web interface for high-fidelity speech synthesis, powered by the **Murf AI SDK** and **FastAPI**.

---

## ✨ Features

- **Crystal Clear Audio**: Leverages Murf's studio-quality AI voices.
- **Modern UI**: A sleek, reactive dashboard built with pure CSS glassmorphism and smooth animations.
- **Real-time Customization**: Adjust speed (`rate`) and tone (`pitch`) to fine-tune the output.
- **Pause Control**: Easily insert standard, strong, or extra-strong pauses directly into your text.
- **Voice Discovery**: Automatically fetches and filters the best available English voices from the Murf library.
- **Audio Visualizer**: Interactive visual feedback during playback.
- **Download Ready**: Generate and save your synthesized speech as MP3 files instantly.

---

## 🛠️ Technology Stack

- **Backend**: Python 3.x, FastAPI, Murf SDK, Uvicorn
- **Frontend**: Vanilla HTML5, CSS3 (Glassmorphism), JavaScript (ES6+)
- **Integration**: Murf API (Text-to-Speech)
- **Styling**: Google Fonts (Outfit), CSS Variable Tokens

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Murf API Key

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "text to speech"
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   MURF_API_KEY=your_api_key_here
   ```

4. **Run the application**
   ```bash
   python -m app.main
   ```
   The app will be available at `http://localhost:8000`.

---

## 📂 Project Structure

```text
app/
├── main.py           # FastAPI backend & Murf integration
├── static/
│   ├── script.js     # Frontend logic & Audio handling
│   └── style.css     # Premium glassmorphic styles
└── templates/
    └── index.html    # Core application interface
tests/                # SDK validation & connectivity scripts
requirements.txt      # Python dependencies
```

---

## 📅 Recent Updates

- **Murf SDK Integration**: Fully migrated to the official Murf Python SDK.
- **Dynamic Voice Loading**: Voices are now fetched live from the API with gender and locale metadata.
---
- **Murf SDK Integration**: Fully migrated to the official Murf Python SDK.
- **Dynamic Voice Loading**: Voices are now fetched live from the API with gender and locale metadata.
- **Security First**: Using `.env` and `.gitignore` to keep credentials safe.
#
