# TagTool-With-Ollama
You can tag image in your computer by Ollama

[中文说明](https://github.com/zuco1111/TagTool-With-Ollama/blob/main/README-ZH.md)

# Preparation

### Install Ollama and LLM

1. Download Ollama from [the official Website](https://www.ollama.com);

2. Open Powershell, use `ollama pull` to download LLM, example:
    ```
    ollama pull llava
    ```
    
3. Start Ollama server (Usually you can ignore this step)
   ```
   ollama serve
   ```

# Installation and Start

### Windows

1. Open Powershell and navigate to the directory where you want to clone the repository;

2. Clone the repository:
    ```
    git clone https://github.com/zuco1111/TagTool-With-Ollama.git
    ```
    
3. Double-click `setup_win.bat` to install dependencies;

4. Edit `run_win.ps1`, `IMAGE_DIRECTORY` and `MODEL`;

5. Run `run_win.ps1` with Powershell


### MacOS

1. Open Terminal and navigate to the directory where you want to clone the repository;

2. Clone the repository:
   ```
   git clone https://github.com/zuco1111/TagTool-With-Ollama.git
   ```

3. Navigate to the fold:
   ```
   cd TagTool-With-Ollama
   ```

4. Make these scripts executable:
   ```
   cd TagTool-With-Ollama
   ```

5. Install dependencies:
   ```
   ./setup_mac.sh
   ```   
   
6. Edit `run_mac.sh`, `IMAGE_DIRECTORY` and `MODEL`

5. Run:
   ```
   ./setup_mac.sh
   ```   
