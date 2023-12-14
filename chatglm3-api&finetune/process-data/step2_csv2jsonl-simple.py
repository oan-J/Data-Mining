import pandas as pd
import json

df = pd.read_csv('文章内容-分割-去重.csv')

with open('文章内容-分割-去重.jsonl', 'w') as json_file:
    for index, row in df.iterrows():
        content = row[0]
        json_obj = {
            "prompt": "生成发疯文学",
            "response": content
        }
        json_file.write(json.dumps(json_obj, ensure_ascii=False))
        json_file.write('\n')  