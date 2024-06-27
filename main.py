import os
import sys
import base64
import requests
import json

def get_image_files(directory):
    supported_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif')
    image_files = [f for f in os.listdir(directory) if f.endswith(supported_extensions)]
    return image_files

def llama3_recognize(api_url, image_path, model, trigger, prompt):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    
    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",  # 确保角色为 "user"
                "content": prompt,
                "images": [encoded_string]
            }
        ],
        "stream": False  # 关闭流式输出
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(api_url, json=payload, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        recognized_text = response_data.get('message', {}).get('content', 'No content')
        if trigger:
            recognized_text = f"{trigger},{recognized_text}"
        return recognized_text
    else:
        return f"Error: {response.status_code}, {response.text}"

def save_text_file(directory, image_name, content):
    base_name = os.path.splitext(image_name)[0]
    text_file_path = os.path.join(directory, base_name + '.txt')
    with open(text_file_path, 'w', encoding='utf-8') as file:  # 使用 'w' 模式以覆盖已有文件
        file.write(content)
    return text_file_path

def process_images(directory, api_url, model, trigger, prompt):
    image_files = get_image_files(directory)
    total_images = len(image_files)

    if total_images == 0:
        print("\n--------文件夹中没有图片--------\n")
        return

    for i, image_name in enumerate(image_files, 1):
        image_path = os.path.join(directory, image_name)
        recognized_content = llama3_recognize(api_url, image_path, model, trigger, prompt)
        text_file_path = save_text_file(directory, image_name, recognized_content)

        # 显示进度信息
        print(f"Processing {i}/{total_images}")
        print(f"Image: {image_name}")
        print(f"Text File: {text_file_path}")
        print(f"Content: {recognized_content}\n")

    print("--------打标已完成--------\n")

if __name__ == '__main__':
    if len(sys.argv) != 6:
        print("Usage: python main.py <image_directory> <api_url> <model> <trigger> <prompt>")
        sys.exit(1)

    image_directory = sys.argv[1]
    api_url = sys.argv[2]
    model = sys.argv[3]
    trigger = sys.argv[4]
    prompt = sys.argv[5]

    process_images(image_directory, api_url, model, trigger, prompt)
