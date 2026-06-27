
# 🔮 Epic Tale Studio

Epic Tale Studio is an immersive, interactive narrative engine that instantly weaves rich, imagery-packed prose across 15 literary genres. Built with a modern glassmorphic interface, it combines creative AI storytelling with powerful, real-time literacy tools—featuring automated text-to-speech tracking and a native click-to-define vocabulary panel.

![Epic Tale Studio Dashboard](SS-EPIC.PNG)

## ✨ Features

* **15 Dynamic Genres:** Tailor stories seamlessly using presets ranging from High Fantasy, Sci-Fi, and Cyberpunk to Noir Mystery and Gothic Horror.
* **Smart Audio Synthesis:** Integrated Web Speech API (`speechSynthesis`) narrates the story aloud, stripping out raw Markdown formatting for a natural audio stream.
* **Real-Time Word Highlighting:** Synchronizes audio boundaries to highlight every individual word token in real-time as it is spoken.
* **Click-to-Define Widget:** Click any word in the narrative to trigger an elegant, docked slide-out panel on the right side of the screen displaying its part of speech and dictionary meaning.
* **Adaptive Aesthetic Engine:** Injects custom-vector doodle graphics and ambient color configurations that dynamically update based on your chosen genre.

## 🛠️ Tech Stack

* **Frontend:** HTML5, Tailwind CSS (via CDN)
* **Markdown Parser:** `marked.js`
* **Avatars:** DiceBear API (Adventurer set)
* **Dictionary Engine:** Free Dictionary API
* **Backend Integration:** Expects a JSON POST endpoint at `/api/generate`

## 🚀 Quick Start

### Prerequisites
To run the frontend out of the box, you'll need a local server environment or backend running on port `8000` to serve the API endpoint `/api/generate`.

### Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/epic-tale-studio.git](https://github.com/your-username/epic-tale-studio.git)
   cd epic-tale-studio

```

2. Open the `index.html` file using a local live server extension (e.g., Live Server in VS Code) or map it behind your backend proxy configuration.

## 🔌 API Contract

The application sends a `POST` request to `/api/generate` with the following payload structure:

```json
{
  "theme": "Ancient Artifacts",
  "genre": "Fantasy",
  "characters": ["Jax", "Lyra"],
  "word_count": 400
}

```

The backend is expected to return a JSON response matching:

```json
{
  "success": true,
  "story": "# The Hidden Vault\n\nThe stone doors scraped open..."
}

```

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

