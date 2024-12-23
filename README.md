# ai-music-composer
AI-powered music composition tool with customizable genres, moods, and collaboration features.

**AI Music Composer** is an open-source project aimed at creating an AI-powered music generation tool that composes melodies, harmonies, and even full arrangements based on user inputs like mood, genre, or style. The ultimate goal is to make this a collaborative platform that evolves into a monetizable solution for music enthusiasts, content creators, and professionals.

## **Features**
- Generate music in various genres (e.g., classical, jazz, pop).
- Input options for mood, theme, or existing compositions.
- Outputs in MIDI and audio formats (.wav or .mp3).
- Pretrained and fine-tuned AI models for symbolic music and direct audio generation.

## **Technologies and Models**

### **Symbolic Music Generation (MIDI):**
- **Music Transformer:** A transformer-based model fine-tuned for sequential music data.
- **MuseNet:** OpenAI's 4-layer GPT-like model for multi-instrument compositions.
- **RNNs (LSTMs/GRUs):** For generating melodies and harmonies sequentially.

### **Audio-Based Generation:**
- **WaveNet:** For high-quality audio waveform generation.
- **GANs (e.g., MelGAN, WaveGAN):** For realistic audio synthesis.
- **DDSP:** Combining traditional DSP techniques with deep learning.

### **Pretrained Resources:**
- **MAESTRO Dataset**: A large dataset of MIDI and aligned audio recordings.
- **NSynth Dataset**: Audio dataset for learning sound characteristics.

## **Architecture Overview**
1. **User Interface (UI):** Web-based interface for users to input preferences and download outputs.
2. **Backend:** Handles user inputs, model inference, and postprocessing.
3. **Model Pipeline:** Preprocessing, training, and inference modules.
4. **Database:** Stores user preferences, generated files, and training datasets.
5. **Cloud Integration:** For model training and deployment (e.g., Google Cloud, AWS).
![diagram-export-23-12-2024-7_13_50-pm](https://github.com/user-attachments/assets/809f11dc-fab4-4d8b-a34d-805e94eaa454)

## **Installation**
### Prerequisites:
- Python 3.8+
- TensorFlow/PyTorch
- MIDI and audio libraries: `pretty_midi`, `librosa`

### Steps:
1. Clone the repository:
   ```bash
   https://github.com/karunakadam2003/ai-music-composer.git
   cd ai-music-composer
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```

## **Usage**
- Input your preferred genre, mood, or a MIDI file.
- Click `Generate` to create music.
- Download the output in MIDI or audio format.

## **Contributing**
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request with detailed explanations.

## **Future Enhancements**
- Real-time collaborative music composition.
- Integration with DAWs (Digital Audio Workstations).
- Advanced customization for genres, instruments, and styles.

## **License**
This project is licensed under the MIT License. See the LICENSE file for details.

---
## **Papers**
[1] Curtis Hawthorne, Andriy Stasyuk, Adam Roberts, Ian Simon, Cheng-Zhi Anna Huang,
    Sander Dieleman, Erich Elsen, Jesse Engel, and Douglas Eck. "Enabling
    Factorized Piano Music Modeling and Generation with the MAESTRO Dataset."
    In International Conference on Learning Representations, 2019.

## **Acknowledgments**
- Research and models from OpenAI, Google Magenta, and others.
- Datasets like MAESTRO and NSynth for providing training data.
- The open-source community for their contributions and inspiration.
