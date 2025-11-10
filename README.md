# AI Exercise Routine Generator

A Streamlit web application that generates personalized weekly exercise routines using AI models through Ollama.

## Features

- **Personalized Exercise Plans**: Get custom weekly exercise routines based on your age, health issues, available time, and fitness goals
- **AI-Powered**: Uses advanced language models (Gemma, Llama) through Ollama for intelligent routine generation
- **User-Friendly Interface**: Clean, intuitive Streamlit web interface
- **Flexible Goals**: Support for weight loss and muscle gain objectives
- **Health-Conscious**: Takes into account age and existing health conditions
- **Time-Adaptive**: Routines adapted to your available daily exercise time (15-120 minutes)

## Requirements

- Python 3.8+
- Ollama installed and running locally
- Internet connection for model downloads (first time)

## Installation

1. **Install Ollama** (if not already installed):
   - Visit [https://ollama.ai](https://ollama.ai) and download for your OS
   - Start Ollama service

2. **Pull AI models** (run these commands in terminal):
   ```bash
   ollama pull gemma2:9b
   ollama pull gemma2:2b
   ollama pull llama3.2:3b
   ollama pull llama3.2:1b
   ```

3. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Start the application**:
   ```bash
   streamlit run app.py
   ```

2. **Open your browser** and navigate to `http://localhost:8501`

3. **Fill in your profile**:
   - Age (16-80 years)
   - Health issues (if any)
   - Available daily exercise time (15-120 minutes)
   - Primary goal (lose weight or gain muscle)

4. **Select an AI model** and click "Generate My Exercise Routine"

5. **Review your personalized routine** and download it as a text file

## AI Models Available

- **gemma2:9b** - Most comprehensive responses (recommended)
- **gemma2:2b** - Faster, lighter model
- **llama3.2:3b** - Good balance of speed and quality
- **llama3.2:1b** - Fastest response times

## Project Structure

```
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── Program_description.txt # Original requirements
```

## Features in Detail

### User Input Collection
- **Age Slider**: Easy age selection from 16-80 years
- **Health Issues**: Text area for medical conditions or physical limitations
- **Exercise Time**: Dropdown selection for daily time commitment
- **Goal Selection**: Radio buttons for weight loss vs muscle gain

### AI Integration
- Direct integration with Ollama API
- Multiple model options for different performance needs
- Comprehensive prompts that include safety considerations
- Error handling for connection issues

### Output Features
- Structured 7-day weekly exercise plans
- Specific exercises with sets, reps, and duration
- Safety considerations based on user profile
- Download functionality for offline access

## Safety Notes

⚠️ **Important**: This application is for informational purposes only. Always consult with healthcare professionals before starting any new exercise program, especially if you have existing health conditions.

## Troubleshooting

### Common Issues

1. **"Cannot connect to Ollama"**
   - Ensure Ollama is installed and running
   - Check if Ollama is accessible at `http://localhost:11434`
   - Try restarting Ollama service

2. **Model not found error**
   - Pull the required model: `ollama pull gemma2:9b`
   - Wait for download to complete
   - Try a different model from the dropdown

3. **Slow response times**
   - Try a smaller model (gemma2:2b or llama3.2:1b)
   - Ensure sufficient system resources
   - Close other resource-intensive applications

## Development

To modify or extend the application:

1. **Main application logic**: Edit `app.py`
2. **Add new models**: Update the `model_options` list in the sidebar
3. **Modify prompts**: Edit the `create_exercise_prompt()` function
4. **UI changes**: Modify Streamlit components and layout

## License

This project is open source and available under the MIT License.