import os
import pandas as pd
from flaskplot.models import Order
from flaskplot import db

def load_data():
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(BASE_DIR, "data", "online_retail.xlsx")

    df = pd.read_excel(file_path)

    for _, row in df.iterrows():
        order = Order(
            customer_id=row['CustomerID'],
            order_date=row['InvoiceDate'],
            order_amount=row['Quantity'] * row['UnitPrice']
        )
        db.session.add(order)

    db.session.commit()
    print("Data loaded successfully!")