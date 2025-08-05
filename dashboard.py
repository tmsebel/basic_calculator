import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import io

# Setting page configuration
st.set_page_config(page_title="Subscriber Dashboard", layout="wide")

# Title and description
st.title("Subscriber Data Dashboard")
st.markdown("Explore subscriber data dispense, payment types, and revenue trends.")

# Loading data
@st.cache_data
def load_data():
    data = """
Cell Number,Name,Amount Paid,Payment Type,Date Joined,Renewal Date,Status
0810707868,Sharmaine Tlou,600.00,Capitec,2025-02-10,2025-08-09,Active
0787638254,Jerry,300.00,Capitec,2025-03-02,2025-08-29,Active
0619775987,Sisasenkosi Moyo,600.00,FNB,2025-03-12,2025-09-08,Active
0836478498,Siphokazi,600.00,Capitec,2025-03-12,2025-09-08,Active
0615996162,Paul Mathebula,600.00,Capitec,2025-03-14,2025-09-10,Active
0736828288,Grace Tsheola,600.00,Capitec,2025-03-14,2025-09-10,Active
0679732231,Namhla Dayinane,600.00,Capitec,2025-03-18,2025-09-14,Active
0839886673,Andries Moale ,600.00,Capitec,2025-03-18,2025-09-14,Active
0710476111,Filiphi Mabunda,600.00,Capitec,2025-03-19,2025-09-15,Active
0736178594,Jabulane Mahlangu,600.00,Capitec,2025-03-25,2025-09-21,Active
0611528124,Princess Sibanda,600.00,Capitec,2025-03-27,2025-09-23,Active
+26662627474,Tsotang V Makhetha,600.00,Mukuru,2025-03-29,2025-09-25,Active
0633163211,Simelokuhle,600.00,Capitec,2025-03-29,2025-09-25,Active
0726422278,Eva,600.00,Capitec,2025-03-31,2025-09-27,Active
+263772845712,Josephine Matanga,600.00,Mukuru,2025-04-10,2025-10-07,Active
0786681625,Bhekinkosi Ndlovu,300.00,Capitec,2025-04-15,2025-10-12,Active
0722860837,Thabane,300.00,Capitec,2025-04-15,2025-10-12,Active
0614920410,Mapule,600.00,Capitec,2025-04-18,2025-10-15,Active
0823464855,Nthabiseng,600.00,Capitec,2025-04-22,2025-10-19,Active
0763188054,Judas,600.00,Capitec,2025-04-23,2025-10-20,Active
+26659344458,Marelebohile,500.00,Capitec,2025-04-24,2025-10-21,Active
0792835597,Samson,600.00,Capitec,2025-04-27,2025-10-24,Active
0711822756,Sthembile,500.00,Capitec,2025-04-28,2025-10-25,Active
0790931506,Mokuru Nation Gee,400.00,FNB,2025-05-03,2025-10-30,Active
0662724616,Pranesh,300.00,Capitec,2025-05-11,2025-11-07,Active
0790756269,Isivile,300.00,Capitec,2025-05-11,2025-11-07,Active
0815994551,Letticia,600.00,Capitec,2025-05-14,2025-11-10,Active
0726654576,Josias,600.00,Capitec,2025-05-24,2025-11-20,Active
0609838055,Elias Mugari,600.00,Capitec,2025-05-26,2025-11-22,Active
0732106764,Zandile,350.00,Capitec,2025-05-31,2025-11-27,Active
0835339843,Ntombi Ndlovu,500.00,FNB,2025-06-07,2025-12-04,Active
0656567508,Zizipho Kroza,600.00,Capitec,2025-06-24,2025-12-21,Active
0839533480,Lulu,100.00,Capitec,2025-06-28,2025-12-25,Active
0829326311,Neo Ntabanyane,600.00,Capitec,2025-07-03,2025-12-30,Active
0699867668,Daisy Mazibuko,600.00,Capitec,2025-07-04,2025-12-31,Active
0767453327,Mike Mnikelo Dube,600.00,Ewallet,2025-07-05,2026-01-01,Active
0732276056,Ernest,150.00,Capitec,2025-07-09,2026-01-05,Active
0720315415,Philemon,600.00,Capitec,2025-07-12,2026-01-08,Active
26658052162,Nomthunzi,480.00,Mukuru,2025-07-15,2026-01-11,Active
0748426764,Kenneth,600.00,Capitec,2025-07-17,2026-01-13,Active
0729245853,Mthobisi,600.00,Capitec,2025-07-25,2026-01-21,Active
0754143649,Eric,600.00,Capitec,2025-07-25,2026-01-21,Active
0721527163,Banele,2000.00,Capitec,2025-07-28,2026-01-24,Active
0662384771,Boipelo Modibedi,600.00,Capitec,2025-02-02,2026-01-28,Active
0785789670,Linky Mulaudzi,350.00,Capitec,2025-01-20,2025-07-19,Inactive
0814583285,Penuel Nkosi,600.00,Capitec,2025-01-21,2025-07-20,Inactive
0732286146,Pascaline,600.00,Capitec,2025-01-23,2025-07-21,Inactive
0736926159,Gift Mkumba,600.00,Capitec,2025-01-23,2025-07-22,Inactive
0799762549,Sbu Zikode,600.00,Capitec,2025-01-29,2025-07-27,Inactive
+263788010257,Nqobile Jele,600.00,Mukuru,2025-01-29,2025-07-28,Inactive
0793254585,Zolisa Magidela,600.00,Capitec,2025-02-08,2025-08-07,Inactive
0731008920,Ouma Oumas,600.00,Capitec,2025-03-29,2025-09-25,Inactive
0725739787,Vukani Shenge,300.00,Ewallet,2025-06-25,2025-12-22,Inactive
0633268565,Warona,250.00,Capitec,2025-06-26,2025-12-23,Inactive
"""
    df = pd.read_csv(io.StringIO(data))
    df["Date Joined"] = pd.to_datetime(df["Date Joined"])
    df["Renewal Date"] = pd.to_datetime(df["Renewal Date"])
    df["Amount Paid"] = pd.to_numeric(df["Amount Paid"], errors="coerce")
    return df

df = load_data()

# Summary statistics
st.header("Summary Statistics")
total_subscribers = len(df)
active_subscribers = len(df[df["Status"] == "Active"])
total_revenue = df["Amount Paid"].sum()
avg_payment = df["Amount Paid"].mean()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Subscribers", total_subscribers)
col2.metric("Active Subscribers", active_subscribers)
col3.metric("Total Revenue", f"R {total_revenue:,.2f}")
col4.metric("Average Payment", f"R {avg_payment:,.2f}")

# Sales per month
st.header("Sales per Month")
df["Month Joined"] = df["Date Joined"].dt.to_period("M").astype(str)
sales_per_month = df.groupby("Month Joined").size().reset_index(name="Subscribers")
fig1 = px.bar(
    sales_per_month,
    x="Month Joined",
    y="Subscribers",
    title="New Subscribers per Month",
    color_discrete_sequence=["#636EFA"],
)
fig1.update_layout(xaxis_title="Month", yaxis_title="Number of Subscribers")
st.plotly_chart(fig1, use_container_width=True)

# Payment type distribution
st.header("Payment Type Distribution")
payment_counts = df["Payment Type"].value_counts().reset_index()
payment_counts.columns = ["Payment Type", "Count"]
fig2 = px.pie(
    payment_counts,
    names="Payment Type",
    values="Count",
    title="Distribution of Payment Types",
)
st.plotly_chart(fig2, use_container_width=True)

# Revenue over time by payment type
st.header("Revenue Over Time by Payment Type")
revenue_by_payment = (
    df.groupby(["Month Joined", "Payment Type"])["Amount Paid"]
    .sum()
    .reset_index()
)
fig3 = px.line(
    revenue_by_payment,
    x="Month Joined",
    y="Amount Paid",
    color="Payment Type",
    title="Revenue Trends by Payment Type",
    markers=True,
)
fig3.update_layout(xaxis_title="Month", yaxis_title="Revenue (R)")
st.plotly_chart(fig3, use_container_width=True)

# Interesting fact
st.header("Interesting Fact")
low_payments = len(df[df["Amount Paid"] < 300])
st.markdown(
    f"**Did you know?** {low_payments} subscribers paid less than R300, indicating a diverse range of payment amounts, with one subscriber paying as low as R100!"
)

# Data table
st.header("Raw Data")
st.dataframe(df, use_container_width=True)