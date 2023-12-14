import pandas as pd
import json

df = pd.read_csv('../data_output_processed/文章内容-分割-去重_output_processed.csv')

with open('../data_output_processed/文章内容-分割-去重_output_processed.jsonl', 'w', encoding='utf-8') as json_file:
    for index, row in df.iterrows():
        scene_recognition = row['场景识别']
        emotion_classification = row['情感分类']
        emotion_score = row['情感打分']
        madness_score = row['发疯程度打分']
        response = row['输入']
        
        json_obj = {
            "prompt": f"生成一段发疯文学，场景为{scene_recognition}，情感分类为{emotion_classification}，情感打分为{emotion_score}，发疯程度为{madness_score}",
            "response": response
        }
        json_file.write(json.dumps(json_obj, ensure_ascii=False))
        json_file.write('\n')  
