#import streamlit as st

#st.set_page_config(
 #   page_title="AI Resume Analyzer",
  #  page_icon=" ",
   # layout="wide"
#)

#st.title(" AI Resume Analyzer + ATS Scorer")

#st.write("Welcome! Upload your resume to get started.")

#uploaded_file = st.file_uploader(
 #   "Uploaded Your Resume (PDF)",
  #  type=["pdf"]
#)

#if uploaded_file is not None:
 #   st.success("Resume Uploaded Successfully!")



#import streamlit as st
#from resume_parser import extract_text

#st.set_page_config(
 #   page_title="AI Resume Analyzer",
  #  page_icon=" ",
   # layout="wide"

#)
#st.title("AI Resume Analyzer + ATS Scorer")

#st.write("Welcome! Upload your resume to get started.")

#uploaded_file = st.file_uploader(
 #   "upload Your Resume (PDF)",
  #  type=["pdf"]
#)

#if uploaded_file is not None:
 #   st.success("Resume Uploaded Successfully!")
  #  text = extract_text(uploaded_file)
   # st.subheader("Extracted resume Text")
    #st.write(text)



import streamlit as st
from ats_score import calculate_ats_score
from resume_parser import (
    extract_text, extract_email, extract_phone, extract_name
)

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="",
    layout="wide"
)
st.title("AI Resume Analyzer + ATS scorer")

uploaded_file = st.file_uploader(
    "Uploaded Resume",
    type=["pdf"]
)

if uploaded_file:
    text = extract_text(uploaded_file)
    name = extract_name(text)
    email = extract_email(text)
    phone = extract_phone(text)

    score,matched_skills = calculate_ats_score(text)

    st.success("Resume Uploaded Successfully!")

    st.subheader("Candidate Details")

    st.write("###  Name")
    st.write(name)

    st.write("###  Email")
    st.write(email)

    st.write("###  Phone")
    st.write(phone)
    st.subheader("Resume Text")
    st.write(text)

    st.subheader("ATS Score")
    st.metric("Resume ATS Score", f"{score}/100")
    st.subheader("Matched Skills")
    if matched_skills:
        st.write(",".join(matched_skills))
    else:
        st.warning("No matching skills found.")

    


