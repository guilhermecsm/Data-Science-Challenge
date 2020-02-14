import json
import pandas as pd
import os
from time import time


# Set the full path
main_path = os.path.join(os.path.dirname(__file__), '..')
main_path = os.path.abspath(main_path)
os.chdir(main_path)

# Read json file
with open("./1. Dados Recebidos/coding_challenge_data (3).json", "r") as f:
    file = json.load(f)

print(f'There are {len(file)} sales sample.')  # There are 50 sales sample.

# Increasing to 1000 sales sample just reapeting 20 times.
ntimes = 20
file_20_times = [file for repetition in range(ntimes)]

# Fixing the list hierarchy
big_file = []
for index in range(ntimes):
    big_file += file_20_times[index]

# Now there are 1000 sales sample.
print(f'Now there are {len(big_file)} sales sample.')

# Starting time ...
start_time = time()

lst = []
for index in range(len(big_file)):
    # Extract sales info
    sale_date = big_file[index]['sale_date']
    sale_id = big_file[index]['sale_id']
    customer_id = big_file[index]['customer_id']
    distribution_center_id = big_file[index]['distribution_center_id']
    delivery_kind = big_file[index]['delivery_kind']
    item_id = big_file[index]['products'][0]['items']
    item_qty = big_file[index]['products'][0]['quantity']

    # Save sales info into dict
    data = {
        "sale_date": sale_date,
        "sale_id": sale_id,
        "customer_id": customer_id,
        "distribution_center_id": distribution_center_id,
        "delivery_kind": delivery_kind,
        "item_id": item_id,
        "item_qty": item_qty
    }

    # Convert to Dataframe
    data_to_df = pd.DataFrame(data)

    # Save into list
    lst.append(data_to_df)

# Final Dataframe
tabular = pd.concat(lst)

# End time
passed_time = time() - start_time
print(f"It took {passed_time}")
