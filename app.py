from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
import streamlit as st

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

st.title("Streamlitを活用したWebアプリ開発")
st.write("##### 動作モード1: おすすめの料理を提案します")
st.write("入力フォームに料理のジャンル、好みなどを入力することで、おすすめの料理を3つ提案します")
st.write("##### 動作モード2: おすすめの国内旅行プランを提案します")
st.write("入力フォームに旅行の目的地、日程、予算などを入力することで、おすすめの旅行プランを提案します")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["おすすめの料理提案", "おすすめの旅行プラン提案"]
)

st.divider()

if selected_item == "おすすめの料理提案":
    input_message = st.text_input(label="料理のジャンルや好みを入力してください。")

else:
    input_message = st.text_input(label="旅行の目的地や日程、予算などを入力してください。")

if st.button("実行"):

    st.divider()

    if selected_item == "おすすめの料理提案":
        if input_message:

            messages = [

                SystemMessage(content="あなたは料理の専門家です。料理のジャンルや好みに応じて、おすすめの料理を3つ提案してください。"),

                HumanMessage(content=input_message)

            ]
            result = llm(messages)

            st.write(f"提案された料理: {result[0].content}")

        else:
            st.error("料理のジャンルや好みを入力してから「実行」ボタンを押してください。")

    else:
        if input_message:

            messages = [

                SystemMessage(content="あなたは旅行の専門家です。旅行の目的地や日程、予算などに応じて、おすすめの旅行プランを3つ提案してください。"),

                HumanMessage(content=input_message)

            ]
            result = llm(messages)

            st.write(f"提案された旅行プラン: {result[0].content}")

        else:
            st.error("旅行の目的地や日程、予算などを入力してから「実行」ボタンを押してください。")
