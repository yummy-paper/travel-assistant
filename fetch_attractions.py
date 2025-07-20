import requests
import re
import json

# 从config.js中提取API密钥
with open('config.js', 'r', encoding='utf-8') as f:
    content = f.read()
    match = re.search(r'amapApiKey:\s*\'(.*?)\'', content)
    if not match:
        raise ValueError("未在config.js中找到有效的API密钥")
    api_key = match.group(1)

# 高德地图API参数
url = "https://restapi.amap.com/v3/place/text"
params = {
    "key": api_key,
    "keywords": "旅游景点",
    "city": "长沙",
    "output": "json",
    "types": "110000",  # 景点类型代码
    "citylimit": True
}

# 发送请求
response = requests.get(url, params=params)
data = response.json()

# 保存结果到JSON文件
with open('attractions.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("景点数据已保存到attractions.json")