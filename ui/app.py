import streamlit as st
st.set_page_config(page_title='Cyber Triage', layout='wide')
st.title('???? Evidence-Locked Agentic Cyber Triage')
st.markdown('### Streamlining Digital Forensics')
choice = st.sidebar.radio('Navigation:', ['1. Case Intake', '2. Live Investigation Trace', '3. Ranked Hosts', '8. Final Report'])
if choice == '1. Case Intake':
    st.header('?? Evidence Intake')
    st.file_uploader('Upload Log Bundle', type=['evtx', 'log'])
else:
    st.header(choice)
    st.write('Module ready!')
