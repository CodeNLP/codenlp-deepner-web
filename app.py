import json
from typing import Dict, Any
import streamlit as st
import requests

api_url = "http://0.0.0.0:8000/predict"


def process_text(text: str) -> Dict[str, Any]:
    resp = requests.post(api_url, data=json.dumps({"text": text}))
    return resp.json()


def main():
    st.title("PolDeepNer2")
    text = st.text_area("Enter text to process", "Type here ...")
    if st.button("Process"):
        st.json(process_text(text))


if __name__ == '__main__':
    main()


# Alexander Van der Bellen prawdopodobnie wybrany na drugą kadencję na prezydenta Austrii.