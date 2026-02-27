import pandas as pd
from datetime import datetime

def calculate_rfm(orders_df):

    today = datetime.today()

    rfm = orders_df.groupby('customer_id').agg({
        'order_date': lambda x: (today - x.max()).days,
        'id': 'count',
        'order_amount': 'sum'
    }).reset_index()

    rfm.columns = ['customer_id', 'recency', 'frequency', 'monetary']

    return rfm

def score_rfm(rfm):

    rfm['r_score'] = pd.qcut(rfm['recency'], 4, labels=[4,3,2,1])
    rfm['f_score'] = pd.qcut(rfm['frequency'], 4, labels=[1,2,3,4])
    rfm['m_score'] = pd.qcut(rfm['monetary'], 4, labels=[1,2,3,4])

    rfm['rfm_score'] = (
        rfm['r_score'].astype(int) +
        rfm['f_score'].astype(int) +
        rfm['m_score'].astype(int)
    )

    return rfm

def segment_customer(row):
    if row['rfm_score'] >= 10:
        return "Champions"
    elif row['rfm_score'] >= 7:
        return "Loyal"
    elif row['rfm_score'] >= 4:
        return "At Risk"
    else:
        return "Lost"