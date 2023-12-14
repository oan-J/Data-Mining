import csv
import pandas as pd
import re
from modelscope import AutoTokenizer, AutoModel, snapshot_download
from tqdm import tqdm

model_dir = './ChatGLM3-main/chatglm3-6b'
tokenizer = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
model = AutoModel.from_pretrained(model_dir, trust_remote_code=True).half().cuda()
model = model.eval()

def analyze_response(response):
    # print("response:")
    scene_recognition_match = re.search(r"场景识别：(.*?)[，,\n]", response)
    # print("scene:",scene_recognition_match)
    sentiment_classification_match = re.search(r"情感分类：(.*?)[，,\n]", response)
    # print("sentiment_classification_match:",sentiment_classification_match)
    sentiment_score_match = re.search(r"情感打分：(\d+)", response)
    # print("sentiment_score_matc:",sentiment_score_match)
    craziness_score_match = re.search(r"发疯程度打分：(\d+)", response)
    # print("craziness_score_match",craziness_score_match)

    scene_recognition = scene_recognition_match.group(1).strip() if scene_recognition_match else ""
    sentiment_classification = sentiment_classification_match.group(1).strip() if sentiment_classification_match else ""
    sentiment_score = sentiment_score_match.group(1) if sentiment_score_match else ""
    craziness_score = craziness_score_match.group(1) if craziness_score_match else ""

    scene_recognition = scene_recognition[:5]
    sentiment_classification = sentiment_classification[:4]

    return {
        '场景识别': scene_recognition,
        '情感分类': sentiment_classification,
        '情感打分': sentiment_score,
        '发疯程度打分': craziness_score,
    }

with open('data/文章内容-分割-去重.csv', 'r') as f:
  reader = csv.reader(f)
  inputs = list(reader)

results = []

for input in tqdm(inputs):
    request = f"这句话‘{input[0]}’，我需要你对这句话进行场景识别+情感分类+情感打分+发疯程度打分，你的输出为‘场景识别’：x，‘情感分类’：x，‘情感打分’：x，‘发疯程度打分’：x，其中，打分以100为满分，你只要给一个分数即可，比如90分你只要说：’90‘，场景识别部分输出小于等于5个字，是你对这句话产生场景的判断，情感分类小于四个字"
    response, history = model.chat(tokenizer, request, history=[])
    analysis = analyze_response(response)
    analysis['输入'] = input[0]
    results.append(analysis)

progress_bar = tqdm(total=len(inputs))
for input in inputs:
    progress_bar.update(1)
progress_bar.close()

df = pd.DataFrame(results)
df.to_csv('data_output/文章内容-分割-去重_output.csv', index=False)