import json
import pandas as pd
import os
import schedule
import time


# Set the full path
main_path = os.path.join(os.path.dirname(__file__), '..')
main_path = os.path.abspath(main_path)
os.chdir(main_path)


def get_tabular_data():
    '''This function receives raw json file and transform it into tabular data.
        Input: json file at  "1. Dados Recebidos" folder.
        Output: csv file saved automatically at "3. Output/1. TabularData.csv". 
    '''

    # Read json file
    with open("./1. Dados Recebidos/sales.json", "r") as f:
        file = json.load(f)

    lst = []
    for index in range(len(file)):
        # Extract sales info
        sale_date = file[index]['sale_date']
        sale_id = file[index]['sale_id']
        customer_id = file[index]['customer_id']
        distribution_center_id = file[index]['distribution_center_id']
        delivery_kind = file[index]['delivery_kind']
        item_id = file[index]['products'][0]['items']
        item_qty = file[index]['products'][0]['quantity']

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

    # Final Dataframe and export it
    tabular = pd.concat(lst)
    tabular.to_csv("./3. Output/1. TabularData.csv", index=False)
    return "File was sent."


# Schedule everyday at 19 o'clock
schedule.every().day.at("19:00").do(get_tabular_data)
while True:
    schedule.run_pending()
    time.sleep(1)
