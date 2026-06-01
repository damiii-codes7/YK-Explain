import streamlit as st
from groq import Groq
import os

try:
    api_key = st.secrets["GROQ_API_KEY"]
except:
    from dotenv import load_dotenv
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

st.set_page_config(page_title="YK Explain", page_icon="📖", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Bebas+Neue&display=swap');
.stApp { background-color: #030303 !important; color: #ffffff !important; font-family: 'Space Mono', monospace !important; }
.stButton > button { background: transparent !important; color: #F2C94C !important; border: 1px solid #F2C94C !important; font-family: 'Space Mono', monospace !important; font-size: 0.75rem !important; letter-spacing: 0.15em !important; text-transform: uppercase !important; padding: 1rem 2rem !important; transition: all 0.3s ease !important; width: 100% !important; }
.stButton > button:hover { background: #F2C94C !important; color: #030303 !important; }
.stTextArea textarea { background: #0a0a0a !important; border: 1px solid #181818 !important; color: #ffffff !important; font-family: 'Space Mono', monospace !important; font-size: 0.85rem !important; border-radius: 0 !important; }
.stTextArea textarea:focus { border-color: #F2C94C !important; }
div[data-testid="metric-container"] { background: transparent !important; border: 1px solid #181818 !important; padding: 1.5rem !important; }
div[data-testid="metric-container"] label { font-family: 'Space Mono', monospace !important; font-size: 0.6rem !important; letter-spacing: 0.2em !important; text-transform: uppercase !important; color: #888 !important; }
div[data-testid="metric-container"] div[data-testid="stMetricValue"] { font-family: 'Bebas Neue', sans-serif !important; font-size: 2.5rem !important; color: #ffffff !important; }
.stDownloadButton > button { background: #F2C94C !important; color: #030303 !important; border: 1px solid #F2C94C !important; font-family: 'Space Mono', monospace !important; font-size: 0.75rem !important; font-weight: 700 !important; padding: 1rem 2rem !important; }
.stSelectbox > div { background: #030303 !important; border: 1px solid #181818 !important; }
hr { border-color: #181818 !important; }
.stMarkdown p { color: #888 !important; font-size: 0.8rem !important; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
@keyframes ringPulse { 0%{opacity:0.15;transform:translate(-50%,-50%) scale(0.3)} 100%{opacity:0;transform:translate(-50%,-50%) scale(1)} }
@keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.5} }
@keyframes slideUp { to{transform:translateY(0)} }
@keyframes marquee { 0%{transform:translateX(0)} 100%{transform:translateX(-50%)} }
</style>
<div style='text-align:center;padding:6vh 2rem 3vh 2rem;position:relative;overflow:hidden;'>
<div style='position:absolute;width:500px;height:500px;border-radius:50%;border:1px solid #F2C94C;opacity:0;top:50%;left:50%;transform:translate(-50%,-50%);animation:ringPulse 6s ease infinite;pointer-events:none;'></div>
<div style='position:absolute;width:500px;height:500px;border-radius:50%;border:1px solid #F2C94C;opacity:0;top:50%;left:50%;transform:translate(-50%,-50%);animation:ringPulse 6s ease 2s infinite;pointer-events:none;'></div>
<div style='display:inline-flex;align-items:center;gap:0.75rem;font-family:Space Mono,monospace;font-size:0.65rem;text-transform:uppercase;letter-spacing:0.15em;color:#888;margin-bottom:2rem;padding:0.6rem 1.2rem;border:1px solid #181818;'>
<span style='width:6px;height:6px;background:#F2C94C;border-radius:50%;animation:pulse 2s infinite;display:inline-block;'></span>
AI-Powered &nbsp;|&nbsp; Any Indian Law &nbsp;|&nbsp; Powered by Llama 3.1
</div>
<div style='overflow:hidden;'>
<div style='transform:translateY(115%);animation:slideUp 1.2s cubic-bezier(0.16,1,0.3,1) 0.3s forwards;font-family:Bebas Neue,sans-serif;font-size:clamp(4rem,10vw,8rem);line-height:0.9;color:#ffffff;'>YK</div>
</div>
<div style='overflow:hidden;'>
<div style='transform:translateY(115%);animation:slideUp 1.2s cubic-bezier(0.16,1,0.3,1) 0.5s forwards;font-family:Bebas Neue,sans-serif;font-size:clamp(4rem,10vw,8rem);line-height:0.9;color:#F2C94C;'>EXPLAIN</div>
</div>
<div style='overflow:hidden;margin-bottom:2rem;'>
<div style='transform:translateY(115%);animation:slideUp 1.2s cubic-bezier(0.16,1,0.3,1) 0.7s forwards;font-family:Bebas Neue,sans-serif;font-size:clamp(1.5rem,4vw,3rem);line-height:0.9;color:#888;'>Bare Act Explainer — Indian Law in Plain English</div>
</div>
<div style='display:inline-block;padding:2rem 3rem;border:1px solid #181818;'>
<div style='font-family:Space Mono,monospace;font-size:0.6rem;text-transform:uppercase;letter-spacing:0.2em;color:#F2C94C;margin-bottom:0.5rem;'>SYSTEM STATUS</div>
<div style='font-family:Bebas Neue,sans-serif;font-size:3rem;color:#ffffff;line-height:1;'>READY</div>
<div style='font-family:Space Mono,monospace;font-size:0.65rem;color:#888;'>All Indian acts loaded // paste any section</div>
</div>
</div>
<hr style='border-color:#181818;margin:0;'>
<div style='overflow:hidden;padding:1rem 0;border-bottom:1px solid #181818;'>
<div style='display:flex;width:max-content;animation:marquee 35s linear infinite;font-family:Space Mono,monospace;font-size:0.7rem;letter-spacing:0.1em;text-transform:uppercase;color:#444;white-space:nowrap;'>
<span style='padding:0 2rem;'>IPC Section 420</span><span style='color:#F2C94C;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Article 21 Constitution</span><span style='color:#F2C94C;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Section 138 NI Act</span><span style='color:#F2C94C;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Section 9A IDA</span><span style='color:#F2C94C;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Section 4 POSH Act</span><span style='color:#F2C94C;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Section 27 Contract Act</span><span style='color:#F2C94C;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Section 302 IPC</span><span style='color:#F2C94C;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Article 19 Constitution</span><span style='color:#F2C94C;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>IPC Section 420</span><span style='color:#F2C94C;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Article 21 Constitution</span><span style='color:#F2C94C;padding:0 1rem;'>◆</span>
</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style='font-family:Space Mono,monospace;font-size:0.65rem;text-transform:uppercase;
letter-spacing:0.2em;color:#888;margin:3rem 0 1rem 0;'>
01 / SELECT THE ACT
</div>
""", unsafe_allow_html=True)

act = st.selectbox("", [
    "Indian Penal Code 1860 (IPC)",
    "Code of Criminal Procedure 1973 (CrPC)",
    "Bharatiya Nyaya Sanhita 2023 (BNS)",
    "Constitution of India",
    "Indian Contract Act 1872",
    "Companies Act 2013",
    "Code on Wages 2019",
    "POSH Act 2013",
    "Maternity Benefit Act 1961",
    "Industrial Disputes Act 1947",
    "Consumer Protection Act 2019",
    "RTI Act 2005",
    "IT Act 2000",
    "GST Act 2017",
    "Income Tax Act 1961",
    "Transfer of Property Act 1882",
    "Negotiable Instruments Act 1881",
    "Arbitration and Conciliation Act 1996",
    "Hindu Marriage Act 1955",
    "Other Indian Law"
], label_visibility="collapsed")

st.markdown("""
<div style='font-family:Space Mono,monospace;font-size:0.65rem;text-transform:uppercase;
letter-spacing:0.2em;color:#888;margin:2rem 0 1rem 0;'>
02 / PASTE THE SECTION TEXT
</div>
""", unsafe_allow_html=True)

section_text = st.text_area("",
    placeholder="Paste any section from any Indian law here...\n\ne.g. Section 420 IPC: Whoever cheats and thereby dishonestly induces the person deceived to deliver any property to any person, or to make, alter or destroy the whole or any part of a valuable security...",
    height=150,
    label_visibility="collapsed"
)

st.markdown("""
<div style='font-family:Space Mono,monospace;font-size:0.65rem;text-transform:uppercase;
letter-spacing:0.2em;color:#888;margin:2rem 0 1rem 0;'>
03 / SELECT EXPLANATION STYLE
</div>
""", unsafe_allow_html=True)

style = st.selectbox("", [
    "Simple English — Explain like I'm not a lawyer",
    "Detailed Legal Analysis — Full breakdown",
    "Practical Examples — Show me real life scenarios",
    "Elements of the Offence — What must be proved?",
    "Punishment & Penalty — What are the consequences?",
    "Landmark Cases — Famous judgments on this section",
    "Comparison — How has this law changed over time?"
], label_visibility="collapsed", key="style")

if st.button("📖 EXPLAIN THIS SECTION →", use_container_width=True):
    if not section_text.strip():
        st.warning("Please paste a section of law first!")
    else:
        with st.spinner("Analysing and explaining..."):

            explain_prompt = f"""You are an expert Indian legal educator who makes complex law simple.

Act: {act}
Section Text: {section_text}
Explanation Style: {style}

Provide a clear explanation in this format:

SECTION OVERVIEW:
[One line summary of what this section does]

PLAIN ENGLISH EXPLANATION:
[Explain in simple language anyone can understand]

KEY ELEMENTS:
[Break down the important parts of this section]

PRACTICAL EXAMPLE:
[Give a real-life example showing when this section applies]

WHO DOES THIS AFFECT:
[Who needs to know about this section]

PUNISHMENT / CONSEQUENCE:
[What happens if this section is violated - if applicable]

LANDMARK CASE:
[One famous Indian case involving this section - if known]

COMMON MISCONCEPTIONS:
[What people often get wrong about this section]"""

            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": explain_prompt}]
            )
            explanation = response.choices[0].message.content

        st.markdown("""
        <div style='font-family:Space Mono,monospace;font-size:0.65rem;text-transform:uppercase;
        letter-spacing:0.2em;color:#888;margin:2rem 0 1rem 0;'>
        04 / EXPLANATION
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div style='border:1px solid #181818;padding:2rem;
        font-family:Space Mono,monospace;font-size:0.85rem;
        color:#ffffff;line-height:1.8;'>
        {explanation.replace(chr(10), '<br>')}
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<hr style='border-color:#181818;margin:2rem 0;'>", unsafe_allow_html=True)

        st.download_button(
            label="EXPORT EXPLANATION →",
            data=f"YK EXPLAIN — BARE ACT EXPLAINER\n{'='*50}\nAct: {act}\nStyle: {style}\n\nSection:\n{section_text}\n\nExplanation:\n{explanation}",
            file_name="YKExplain_Section.txt",
            mime="text/plain",
            use_container_width=True
        )

st.markdown("""
<div style='text-align:center;padding:1rem;font-family:Space Mono,monospace;
font-size:0.55rem;color:#333;text-transform:uppercase;letter-spacing:0.1em;'>
Always verify with the original bare act and consult a qualified lawyer.<br>Adv. Damini Yasodai — YK Legal
</div>
""", unsafe_allow_html=True)