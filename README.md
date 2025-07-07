# 🧠 GenAI Deployment Lifecycle Manager (GDLM)

A Streamlit-based interactive dashboard simulating a real-world **Product Management + MLOps** scenario for deployed LLMs.

---

## 🚀 About the Project

This tool was developed to demonstrate product thinking for AI/ML lifecycle management. It helps PMs and MLOps engineers visualize and manage latency, token usage, and model versioning — all in an interactive, user-friendly format.

---

## 🎯 Key Features

- 📈 Line charts for **Latency** and **Token Usage** (30-day time series)
- 🔁 **Retrain** / ⏪ **Rollback** model actions (simulated)
- 📊 KPI cards with day-over-day **delta**
- ⚠️ Alert and Drift Detection Display
- 📅 **Date Range Filter** and **Version Selector**
- 💬 Team Comment Simulation
- 🧪 Logs, audit trail, and mock data-driven decisions

---

## 🗂️ Files Included

| File                  | Purpose                                          |
|-----------------------|--------------------------------------------------|
| `app_v2.py`           | Main Streamlit dashboard script                  |
| `gdlm_dummy_data.json`| Model metadata, accuracy, alerts, logs, etc.     |
| `gdlm_metrics_data.json` | 30-day metrics for latency and token usage   |

---

## 🛠️ Tech Stack

- **Python 3.10+**
- [Streamlit](https://streamlit.io/)
- Altair Charts
- JSON (mocked data)

---

## 🧪 How to Run

```bash
pip install streamlit
streamlit run app_v2.py
```

If you're using Google Colab + ngrok, follow these steps:
- Upload all three files
- Set your ngrok authtoken
- Launch using:
  ```python
  !streamlit run app_v2.py &
  ```

---

## 🌐 Demo

🔗 **Live Demo:** [Available on request or paste your ngrok/Streamlit Cloud link here]

---

## 📸 Screenshots

_Add dashboard screenshots or gifs here_

---

## 👨‍💻 Author

**Sukrit Kashyap Goswami**  
[LinkedIn](https://www.linkedin.com/in/sukritkashyapgoswami/) | [Email](mailto:6sukritgoswami@gmail.com)

---
