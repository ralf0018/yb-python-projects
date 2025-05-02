import pandas as pd
path='./week4/inclass_activities/sample_junk_mail.csv'
df = pd.read_csv(path)
print(df.head(2))