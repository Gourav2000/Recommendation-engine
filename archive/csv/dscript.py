import pandas as pd

data=pd.read_csv('olist_customers_dataset.csv')
print(data.to_json('jj.json'))
