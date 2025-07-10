
import streamlit as st
import json
import pandas as pd
import datetime
import altair as alt

# --- Load Data ---
with open("gdlm_dummy_data.json", "r") as f:
    model_data = json.load(f)

with open("gdlm_metrics_data_v2.json", "r") as f:
    metrics_data = json.load(f)

# --- Sidebar Selections ---
model_names = [model["name"] for model in model_data["models"]]
selected_model_name = st.sidebar.selectbox("Select a Model", model_names)

# Version selector
available_versions = [m["version"] for m in model_data["models"] if m["name"] == selected_model_name]
selected_version = st.sidebar.selectbox("Select Version", available_versions)

# Date filter
st.sidebar.subheader("📅 Select Date Range")
start_date = st.sidebar.date_input("Start Date", datetime.date.today() - datetime.timedelta(days=14))
end_date = st.sidebar.date_input("End Date", datetime.date.today())

# Fetch selected model
selected_model = next(
    m for m in model_data["models"]
    if m["name"] == selected_model_name and m["version"] == selected_version
)
model_metrics = metrics_data[selected_model_name]

# --- Header ---
st.title("🧠 GenAI Deployment Lifecycle Manager (GDLM)")
st.markdown(f"### Model: `{selected_model_name}` | Version: `{selected_model['version']}`")

# --- Filtered Time-Series Data ---
df = pd.DataFrame({
    "Date": pd.to_datetime(model_metrics["dates"]),
    "Latency": model_metrics["latency"],
    "Token Usage": model_metrics["token_usage"]
})
filtered_df = df[(df["Date"] >= pd.to_datetime(start_date)) & (df["Date"] <= pd.to_datetime(end_date))]

# --- KPIs with delta ---
yesterday = df.iloc[-2]
today = df.iloc[-1]
col1, col2, col3, col4 = st.columns(4)
col1.metric("Latency (ms)", today["Latency"], round(today["Latency"] - yesterday["Latency"], 2))
col2.metric("Accuracy (%)", selected_model["accuracy"])
col3.metric("Token Usage", selected_model["token_usage"])
col4.metric("Inference Cost ($)", selected_model["inference_cost"])

# --- Charts ---
st.subheader("📈 Model Latency Over Time")
latency_chart = alt.Chart(filtered_df).mark_line().encode(
    x="Date:T", y="Latency", tooltip=["Date", "Latency"]
).properties(width=700, height=300)
st.altair_chart(latency_chart, use_container_width=True)

st.subheader("📊 Token Usage Over Time")
token_chart = alt.Chart(filtered_df).mark_line(color="orange").encode(
    x="Date:T", y="Token Usage", tooltip=["Date", "Token Usage"]
).properties(width=700, height=300)
st.altair_chart(token_chart, use_container_width=True)

# --- Alerts ---
st.subheader("⚠️ Alerts")
if selected_model["alerts"]:
    for alert in selected_model["alerts"]:
        st.error(alert)
else:
    st.success("No active alerts.")

# --- Action Buttons ---
st.subheader("🛠️ Actions")
if st.button("🔁 Retrain Model"):
    st.info(f"Model `{selected_model_name}` marked for retraining ✅")

if st.button("⏪ Rollback Model"):
    st.warning(f"Model `{selected_model_name}` rolled back to previous version ⏮️")

# --- Logs ---
st.subheader("📝 Logs")
log_df = pd.DataFrame(selected_model["logs"])
st.table(log_df)

# --- Comment Box ---
st.subheader("💬 Team Comments")
comment = st.text_input("Add your comment here:")
if st.button("Post Comment"):
    st.success("Comment posted! (simulated)")
