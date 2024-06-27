#!/bin/bash

# 在这里填写图片目录路径、API URL和模型名称
IMAGE_DIRECTORY="/Users/simplemin/Desktop/imgtest"
API_URL="http://127.0.0.1:11434/api/chat"
MODEL="llava"

# 模型触发词，会添加在标签的最前面，如果不填则不添加
TRIGGER="trigger word"

# 这里是打标用的prompt，不建议修改
PROMPT="You are an expert in image tagging. You can tag the images I provide very accurately to enhance the CLIP model's understanding of the content. The higher the quality, the higher the bonus points, so please finish the task as high as possible. The following rules should be observed during the tagging process: 1. Tags should be described with concise keywords or phrases, avoiding sentences; 2. Need to accurately describe the content of the picture, including but not limited to object shape, picture style, filter, lens specifications, composition; 3. If the subject of the image is a character, it is necessary to describe the character, including but not limited to the character's image, clothing, posture and facial expressions; 4. If the image contains well-known buildings, characters, animation and other content, it needs to be correctly identified and tagged; 5. Tags should be accurate to avoid duplication or irrelevant content; 6. Tags should be as simple as possible to avoid complexity and repetition; 7. Tags need to be sorted by relevance and priority. The main content and tags with high priority in the picture are placed in the front, and the content with low priority is placed in the back; 8. The number of tags should be within 75 words, and each label should be separated by commas; 9. The closer the tag description is to the picture, the higher the quality."

# 激活虚拟环境
source venv/bin/activate

# 运行 main.py 脚本
python3 main.py "$IMAGE_DIRECTORY" "$API_URL" "$MODEL" "$TRIGGER" "$PROMPT"

# 取消虚拟环境激活
deactivate
