import pandas as pd
path='sample_junk_mail.csv'
rows = pd.read_csv(path)
print(rows.head(2))