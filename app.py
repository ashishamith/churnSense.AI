import streamlit as st
import pandas as pd
import plotly.express as px
import google.generativeai as genai
import time
import traceback

# -----------------------------------
# GEMINI API KEY
# -----------------------------------
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# -----------------------------------
# PAGE SETTINGS
# -----------------------------------
st.set_page_config(
    page_title="ChurnSense.AI - AI Telecom Churn Analyst ",
    page_icon="📊",
    layout="wide"
)

st.title("📊 ChurnSense.AI - AI Telecom Churn Analyst")
st.write("Ask questions about the telecom churn dataset using natural language.")

# -----------------------------------
# SAMPLE QUESTIONS FOR RECRUITERS
# -----------------------------------

st.markdown("### Example questions you can ask")

st.markdown("""
• What percentage of customers have churned?  
• How many customers churned?  
• Show churn distribution by contract type  
• Compare churn rate by internet service  
• What is the average monthly charge for churned customers?  
• Plot churn by payment method  
""")

# -----------------------------------
# LOAD DATASET
# -----------------------------------

@st.cache_data
def load_data():
    return pd.read_csv("telecom_churn.csv")

df = load_data()

# -----------------------------------
# SIDEBAR
# -----------------------------------

st.sidebar.header("Dataset Information")
st.sidebar.write("Rows:", df.shape[0])
st.sidebar.write("Columns:", df.shape[1])

if st.sidebar.checkbox("Preview dataset"):
    st.dataframe(df.head())

# -----------------------------------
# CHAT HISTORY
# -----------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# display chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# -----------------------------------
# USER INPUT
# -----------------------------------

question = st.chat_input("Ask a question about the dataset")

if question:

    st.session_state.messages.append({"role":"user","content":question})

    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):

        with st.spinner("Analyzing dataset..."):

            try:

                prompt = f"""
You are a data analyst.

A pandas dataframe called df exists.

Columns:
{list(df.columns)}

User question:
{question}

Write Python pandas code ONLY.

Rules:
- Use dataframe df
- Store final answer in variable result
- If visualization is useful create plotly figure named fig
"""

                model = genai.GenerativeModel("models/gemini-2.5-flash")

                response = model.generate_content(prompt)

                code = response.text
                code = code.replace("```python","").replace("```","")

                # run generated code
                local_vars = {"df":df,"px":px}

                exec(code,{},local_vars)

                result = local_vars.get("result")
                fig = local_vars.get("fig")

                # -----------------------------------
                # PROFESSIONAL SENTENCE
                # -----------------------------------

                if isinstance(result,(int,float)):
                    answer = f"Based on the dataset, the computed value is **{result}**."

                elif isinstance(result,pd.Series):
                    answer = "Here is the analysis based on the dataset."

                elif isinstance(result,pd.DataFrame):
                    answer = "The following table summarizes the analysis results."

                else:
                    answer = str(result)

                # -----------------------------------
                # ANIMATED CHATGPT STYLE TEXT
                # -----------------------------------

                placeholder = st.empty()

                typed_text = ""

                for char in answer:
                    typed_text += char
                    placeholder.markdown(typed_text)
                    time.sleep(0.01)

                # -----------------------------------
                # SHOW DATAFRAME
                # -----------------------------------

                if isinstance(result,pd.Series):
                    st.dataframe(result)

                if isinstance(result,pd.DataFrame):
                    st.dataframe(result)

                # -----------------------------------
                # SHOW CHART
                # -----------------------------------

                if fig:
                    st.plotly_chart(fig,use_container_width=True)

                st.session_state.messages.append(
                    {"role":"assistant","content":answer}
                )

            except Exception:

                st.error("Error running analysis")
                st.text(traceback.format_exc())
