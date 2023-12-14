from modelscope import AutoTokenizer, AutoModel, snapshot_download
model_dir = './ChatGLM3-main/chatglm3-6b'
tokenizer = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
model = AutoModel.from_pretrained(model_dir, trust_remote_code=True).half().cuda()
model = model.eval()

response, history = model.chat(tokenizer, "这句话‘我起床了 这个点起床的人 是未来之星 是国家栋梁 是都市小说里的商业大鳄 是吾日三省吾身的自律者 是相亲节目里的心动嘉宾 是自然界的丛林之王 是世间所有丑与恶的唾弃者 是世间所以美与好的创造者‘，我需要你对这句话进行场景识别+情感分类+情感打分+发疯程度打分，你的输出为‘场景识别’：x，‘情感分类’：x，‘情感打分’：x，‘发疯程度打分’：x，其中，打分以100为满分，你只要给一个分数即可，比如90分你只要说：’90‘，场景识别部分输出小于等于5个字，是你对这句话产生场景的判断，情感分类小于四个字", history=[])
# 这句话‘我起床了 这个点起床的人 是未来之星 是国家栋梁 是都市小说里的商业大鳄 是吾日三省吾身的自律者 是相亲节目里的心动嘉宾 是自然界的丛林之王 是世间所有丑与恶的唾弃者 是世间所以美与好的创造者‘，我需要你对这句话进行场景识别+情感分类+情感打分+发疯程度打分，你的输出为‘场景识别’：x，‘情感分类’：x，‘情感打分’：x，‘发疯程度打分’：x，其中，打分以100为满分，你只要给一个分数即可，比如90分你只要说：’90‘，场景识别部分输出小于等于5个字，是你对这句话产生场景的判断，情感分类小于四个字"
print(response)

