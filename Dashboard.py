import pandas as pd
import streamlit as st
import plotly.express as px

# Loading the necessary data
df = pd.read_csv("data/sample_data.csv")

# Calculating KPIs
# df["Net Profit"] = df["Revenue"] - df["Expenses"]
total_revenue = df["Revenue"].sum()
total_expenses = df["Salary Payments"].sum() + df["Rent"].sum() + df["Debt"].sum() + df["Miscellaneous Costs"].sum()
total_profit = df["Profit"].sum()

# The Dashboard
st.set_page_config(page_title="BRBs Financial Analytics Dashboard", layout="wide")
st.title("BRBs Financial Analytics Dashboard")
st.write("This dashboard shows the financial analytics of the company 'BRB' over a year.")

# The KPIs
col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"${total_revenue:,.0f}")
col2.metric("Total Expenses", f"${total_expenses:,.0f}")
col3.metric("Net Profit", f"${total_profit:,.0f}")

# Line Chart
fig_line = px.line(df, x="Date", y=["Salary Payments", "Debt", "Miscellaneous Costs", "Rent", "Revenue", "Profit"], 
                   title="Finances Over Time")
st.plotly_chart(fig_line, use_container_width=True)

# Revenue Pie Chart
rev_pie = px.pie(df, values="Revenue", names="Date", title="Revenue Distribution by Month")
st.plotly_chart(rev_pie, use_container_width=True)

# Salary Payments Pie Chart
sal_pie = px.pie(df, values="Salary Payments", names="Date", title="Salaries Paid Distribution by Month")
st.plotly_chart(sal_pie, use_container_width=True)

# Rent Pie Chart
ren_pie = px.pie(df, values="Rent", names="Date", title="Rent Distribution by Month")
st.plotly_chart(ren_pie, use_container_width=True)

# Debt Pie Chart
deb_pie = px.pie(df, values="Debt", names="Date", title="Debt Owed Distribution by Month")
st.plotly_chart(deb_pie, use_container_width=True)

# Miscellaneous Costs Pie Chart
mic_pie = px.pie(df, values="Miscellaneous Costs", names="Date", title="Miscellaneous Costs Distribution by Month")
st.plotly_chart(mic_pie, use_container_width=True)