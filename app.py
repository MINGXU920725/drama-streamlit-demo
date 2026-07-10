import streamlit as st
from zhipuai import ZhipuAI

st.title("LLM Demo")

question = st.text_input("Question")

if st.button("Generate"):

    client = ZhipuAI(api_key=st.secrets["ZHIPU_API_KEY"])

    response = client.chat.completions.create(
        model="glm-4.5-air",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    st.write(response.choices[0].message.content)
