import pandas as pd

# Get tabular data from API
tabular = pd.read_html("http://127.0.0.1:5000/api/v1/sales")
print(tabular)
