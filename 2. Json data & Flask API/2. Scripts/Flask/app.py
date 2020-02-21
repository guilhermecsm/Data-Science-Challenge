from flask import Flask, render_template
import pandas as pd
import os


# Set the full path
main_path = os.path.join(os.path.dirname(__file__), '..', '..')
main_path = os.path.abspath(main_path)
os.chdir(main_path)

# init app
app = Flask(__name__)

# Data
df = pd.read_csv("./3. Output/1. TabularData.csv")

# ROUTE
@app.route('/')
def index():
    return "Welcome to the API by Guilherme Martins"

# API ROUTE
@app.route('/api/v1/sales', methods=["GET"])
def get_sales():
    return df.to_html()

# Customize API ROUTE
@app.route('/api/v1/sales/<delivery_kind>', methods=["GET"])
def get_delivery_kind(delivery_kind="delivery"):
    df_mod = df.loc[df.delivery_kind == delivery_kind, :]
    return df_mod.to_html()


if __name__ == '__main__':
    app.run(debug=False)
