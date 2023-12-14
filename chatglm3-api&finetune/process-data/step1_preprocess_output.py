import pandas as pd
import re

df = pd.read_csv('../data_output/文章内容-分割-去重_output.csv')

df = df.dropna()

df = df[~df['场景识别'].astype(str).str.contains(r'\d')]

english_rows = df[df['场景识别'].astype(str).apply(lambda x: bool(re.search('[a-zA-Z]', x)))]['场景识别'].astype(str)
df = df.drop(df[df['场景识别'].isin(english_rows)].index)

df.to_csv('../data_output_processed/文章内容-分割-去重_output_processed.csv', index=False)
