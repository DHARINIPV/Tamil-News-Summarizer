import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Page config
st.set_page_config(page_title="Tamil News Summarizer", page_icon="📰")
st.title("📰 AI-Powered Tamil News Summarizer")
st.markdown("Paste any Tamil or English news article and get an instant AI summary!")

# Input
news_text = st.text_area("📝 Paste your news article here:", height=300, placeholder="Paste the full news article text here...")

language = st.selectbox("🌐 Summarize in which language?", ["English", "Tamil"])

if st.button("🔍 Summarize"):
    if news_text.strip() == "":
        st.warning("Please paste a news article first!")
    else:
        with st.spinner("Summarizing..."):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "user",
                        "content": f"""You are a professional news summarizer.
Summarize the following news article in {language} in 5 clear bullet points.
Keep it simple and easy to understand.

Article:
{news_text}"""
                    }
                ]
            )
            summary = response.choices[0].message.content
            st.success("✅ Summary Ready!")
            st.markdown("### 📋 Summary:")
            st.write(summary)