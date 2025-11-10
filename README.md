Projektas kaip ir pavyko, dauguma funkcijų veikia, bent jau pas mane :) o apie pamąstymus, tai reikia galingesnio kompiuterio, nes daug kur susiduri su tokiomis bėdomis, kaip pvz. gemma3:4b reikia min 4,9 GB RAM laisvų pas mane iš 8 tik 3,9 GB laisvi, tada renkasi mažesnį modelį, bet tas tada sako , kad ne visas komandas gali vykdyti :) dar labai labai keista, kai pythonas ir kitos programos instaliuotos, ojis vis tikrina kuria tas aplinkas, kurios užtrunka ir gan nemažai laiko. Bet visumoje viskas labai įdomu!

# UAB Sveikata - AI Health Assistant
 
A professional Streamlit web application that generates personalized weekly exercise routines using AI models. Developed for UAB Sveikata to provide safe, medically-aware health and exercise recommendations.

## 🏥 Professional Health Features

- **Medical Compliance**: All AI responses include required UAB Sveikata branding and medical disclaimers
- **Health-Focused**: AI assistant only answers health and exercise related questions  
- **Safety First**: Comprehensive safety considerations for all age groups and health conditions
- **Professional Standards**: Follows healthcare industry standards for AI-assisted recommendations
- **Input Validation**: Ensures only appropriate data formats (numbers for age, specific goal options)
- **Response Validation**: Verifies AI responses meet medical compliance requirements

## 🔧 Technical Features

- **Dual AI Provider Support**: Choose between local Ollama models or cloud-based OpenRouter models
- **Personalized Exercise Plans**: Get custom weekly exercise routines based on your age, health issues, available time, and fitness goals
- **Local & Cloud Options**: 
  - **Ollama**: Privacy-focused local models (no internet required after setup)
  - **OpenRouter**: Powerful cloud models with latest AI capabilities
- **Professional Interface**: Clean, medical-grade user experience optimized for health applications
- **Flexible Goals**: Support for weight loss and muscle gain objectives
- **Health-Conscious**: Takes into account age and existing health conditions
- **Time-Adaptive**: Routines adapted to your available daily exercise time (15-120 minutes)

## Requirements

- Python 3.8+
- **For Ollama**: Ollama installed and running locally
- **For OpenRouter**: Internet connection and OpenRouter API key
- Streamlit and requests Python packages

## Installation

### Option 1: Local AI with Ollama

1. **Install Ollama** (if not already installed):
   - Visit [https://ollama.ai](https://ollama.ai) and download for your OS
   - Start Ollama service: `ollama serve`

2. **Pull AI models** (run these commands in terminal):
   ```bash
   ollama pull gemma3:270m  # Lightweight model for limited RAM
   ```

### Option 2: Cloud AI with OpenRouter

1. **Get OpenRouter API Key**:
   - Visit [https://openrouter.ai](https://openrouter.ai)
   - Sign up and get your API key from [https://openrouter.ai/keys](https://openrouter.ai/keys)

### Setup Python Environment

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

4. **Choose AI Provider**:
   - **Ollama (Local)**: Select local model and ensure Ollama is running
   - **OpenRouter (Cloud)**: Enter your API key and select a cloud model

5. **Generate routine** and download it as a text file

## AI Models Available

### Ollama (Local)
- **gemma3:270m** - Ultra-lightweight model (works with limited RAM)
- Privacy-focused (no data sent to cloud)
- Requires local setup but runs offline

### OpenRouter (Cloud)  
- **google/gemma-2-9b-it** - Advanced Gemma model
- **google/gemma-2-27b-it** - Large Gemma model
- **anthropic/claude-3.5-sonnet** - Claude 3.5 Sonnet
- **openai/gpt-4o-mini** - GPT-4 Omni Mini
- **meta-llama/llama-3.1-8b-instruct** - Llama 3.1
- **mistralai/mistral-7b-instruct** - Mistral 7B
- Latest AI capabilities but requires internet and API costs

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