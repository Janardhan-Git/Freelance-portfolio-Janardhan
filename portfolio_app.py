import streamlit as st

st.set_page_config(page_title="Janardhan | Freelance AI & Cloud Security Engineer", layout="wide", page_icon="💼")

st.title("\U0001F468‍\U0001F4BB Janardhan - Freelance AI/Cloud Security Engineer")
st.write("Helping companies build secure, smart, and scalable tech")

st.markdown("## 🚀 Services I Offer")
st.markdown("""
- \U0001F916 AI/ML Tools: Spam detection, log anomaly detection, ML agents
- ☁️ Cloud Security: AWS audits, SIEM integrations, tfstate/IaC security
- \U0001F40D Python Apps: FastAPI/Flask APIs, automation scripts, FFmpeg tools
""")

st.markdown("## 💼 Portfolio Projects GitHub")
projects = {
    "SIEM Log Analyzer": "https://github.com/Janardhan-Git/log-analysis-agent-streamlit",
    "Phishing Email Classifier": "https://github.com/Janardhan-Git/phishing-email-detector",
    "YouTube Video Editor Tool": "https://github.com/Janardhan-Git/youtube-downloader-app",
}
for name, link in projects.items():
    st.markdown(f"- [{name}]({link})")
    
st.markdown("## 🌐 Live Apps")
projects = {
    "SIEM Log Analyzer": "https://cloud-siem-analyzer.streamlit.app/",
    "Phishing Email Classifier": "https://spam-email-classifier-2v3ht7ynf9uf8qcsajdoyb.streamlit.app/",
    "YouTube Video Editor Tool": "https://yt-vid-downloader-editor.streamlit.app/",
}
for name, link in projects.items():
    st.markdown(f"- [{name}]({link})")   

st.markdown("## 📬 Contact Me")
st.markdown("""
- 📧 Email: janardhanap12@gmail.com  
- 🌐 [LinkedIn](www.linkedin.com/in/janardhanp)  
- 🧰 [GitHub](https://github.com/Janardhan-Git)
""")
