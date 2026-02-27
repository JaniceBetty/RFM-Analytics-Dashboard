from flaskplot import app
from flaskplot.models import Order
from flask import render_template
import pandas as pd
from flaskplot.rfm import calculate_rfm, score_rfm, segment_customer


@app.route('/')
def dashboard():

    orders = Order.query.all()

    data = []
    for order in orders:
        data.append({
            "id": order.id,
            "customer_id": order.customer_id,
            "order_date": order.order_date,
            "order_amount": order.order_amount
        })

    orders_df = pd.DataFrame(data)

    if orders_df.empty:
        return "No data available"
    
    # 🔹 KPI Calculations
    total_orders = len(orders_df)
    total_revenue = round(orders_df["order_amount"].sum(), 2)
    total_customers = orders_df["customer_id"].nunique()

    rfm = calculate_rfm(orders_df)
    rfm = score_rfm(rfm)
    rfm['segment'] = rfm.apply(segment_customer, axis=1)

    # KPIs
    total_customers = len(rfm)
    total_revenue = orders_df['order_amount'].sum()
    avg_order_value = round(orders_df['order_amount'].mean(), 2)
    champions = len(rfm[rfm['segment'] == "Champions"])

    

    # Segment distribution
    segment_counts = rfm['segment'].value_counts().to_dict()
    
    orders_df['order_date'] = pd.to_datetime(orders_df['order_date'])
    orders_df['month'] = orders_df['order_date'].dt.to_period('M')

    monthly_revenue = (
    orders_df.groupby('month')['order_amount']
    .sum()
    .astype(float)
    )

    monthly_revenue = {
    str(k): float(v)
    for k, v in monthly_revenue.items()
    }

    scatter_data = rfm[['recency', 'frequency']].to_dict(orient='records')

    # Top 10 customers by total spend
    top_customers = (
    orders_df.groupby('customer_id')['order_amount']
    .sum()
    .sort_values(ascending=False)
    .head(10)
    )

    top_customers = {
    str(k): float(v)
    for k, v in top_customers.items()
    }

    monetary_bins = pd.cut(rfm['monetary'], bins=5)

    monetary_distribution = monetary_bins.value_counts().sort_index()

    monetary_distribution = {
    str(k): int(v)
    for k, v in monetary_distribution.items()
    }

    rfm_score_dist = rfm['rfm_score'].value_counts().sort_index()

    rfm_score_dist = {
    str(k): int(v)
    for k, v in rfm_score_dist.items()
    }

    return render_template(
    "dashboard.html",
    total_orders=total_orders,
    total_customers=total_customers,
    total_revenue=total_revenue,
    avg_order_value=avg_order_value,
    champions=champions,
    segment_counts=segment_counts,
    monthly_revenue=monthly_revenue,
    scatter_data=scatter_data,
    top_customers=top_customers,
    monetary_distribution=monetary_distribution,
    rfm_score_dist=rfm_score_dist
    )
