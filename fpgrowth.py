import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth, association_rules

# 读取CSV文件
df = pd.read_csv('data.csv', encoding='utf-8')  
print("df",df)
# 数据预处理，假设评论列名为 'comment'
separators = r',|，|!|\s+'
transactions = df['comments'].str.split(separators) # 分割每个评论为词语列表
print("transactions", transactions)
# 使用TransactionEncoder将数据转换为布尔矩阵
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df_encoded = pd.DataFrame(te_ary, columns=te.columns_)

# 使用FP-growth算法挖掘频繁项集
frequent_itemsets = fpgrowth(df_encoded, min_support=0.07, use_colnames=True)

# 打印频繁项集
# print("Frequent Itemsets:\n")
# print(frequent_itemsets)
# print("\n\n")

# 生成关联规则
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)

# 去除重复的关联规则
rules = rules.drop_duplicates(subset=['antecedents', 'consequents'])

# 打印结果
# print("Rules:\n", rules)

# 将结果保存到CSV文件
frequent_itemsets.to_csv('frequent_itemsets.csv', index=False, encoding='utf-8')
rules.to_csv('association_rules.csv', index=False, encoding='utf-8')