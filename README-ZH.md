# 基于Ollama的本地打标工具
你可以使用本地大语言模型对图片进行打标

[English README](https://github.com/zuco1111/TagTool-With-Ollama/blob/main/README.md)

# 准备

### 安装Ollama和大语言模型

1. 从[Ollama官网](https://www.ollama.com)下载并安装Ollama；

2. 打开Powershell，使用`ollama pull`命令下载LLM, 例如:
    ```
    ollama pull llava
    ```
    
3. 使用以下命令启动ollama服务（一般情况下安装后会自动运行，无需手动运行，可忽略这一步）
   ```
   ollama serve
   ```

# 安装并使用


### Windows

1. 打开Powershell并使用`cd`命令切换至你想要安装的目录；

2. 使用以下命令拉取项目到本地：
    ```
    git clone https://github.com/zuco1111/TagTool-With-Ollama.git
    ```
    
3. 双击`setup_win.bat`来安装依赖；

4. 编辑`run_win.ps1`，将`IMAGE_DIRECTORY`后面的路径改成图片路径，将`MODEL`后面的模型名称改成你想要使用的模型名称；

5. 右键`run_win.ps1`选择使用Powershell运行即可


### MacOS

1. 打开终端并使用`cd`命令切换至你想要安装的目录;

2. 使用以下命令拉取项目到本地：
   ```
   git clone https://github.com/zuco1111/TagTool-With-Ollama.git
   ```

3. 切换至项目路径：
   ```
   cd TagTool-With-Ollama
   ```

4. 修改脚本权限为可执行：
   ```
   chmod +x setup_mac.sh; chmod +x run_mac.sh
   ```

5. 安装依赖：
   ```
   ./setup_mac.sh
   ```
   
6. 编辑`run_win.sh`，将`IMAGE_DIRECTORY`后面的路径改成图片路径，将`MODEL`后面的模型名称改成你想要使用的模型名称；

5. 开始打标：
   ```
   ./run_mac.sh
   ```
