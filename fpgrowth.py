import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth, association_rules

df = pd.read_csv('data.csv', encoding='utf-8')  
print("df",df)

separators = r',|，|!|\s+'
transactions = df['comments'].str.split(separators) 
print("transactions", transactions)

te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df_encoded = pd.DataFrame(te_ary, columns=te.columns_)

frequent_itemsets = fpgrowth(df_encoded, min_support=0.07, use_colnames=True)

rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)

rules = rules.drop_duplicates(subset=['antecedents', 'consequents'])


frequent_itemsets.to_csv('frequent_itemsets.csv', index=False, encoding='utf-8')
rules.to_csv('association_rules.csv', index=False, encoding='utf-8')
