import streamlit as st
import subprocess

def main():
    st.title("Eirinn's ToC Extractor 😎")
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file:
        st.write("Processing...")

        # Save the uploaded file temporarily
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.read())

        # Run your extract-toc.py script
        result = subprocess.check_output(["python", "extract-toc.py", "temp.pdf"])
        # print(result)
        # Display the result
        st.write("Text output:")
        st.code(result.decode("cp1252"))

if __name__ == "__main__":
    main()