import ollama
import streamlit as st

# 获取客户端
client = ollama.Client(host="http://localhost:11434")

# 初始化消息记录
if "message" not in st.session_state:
    st.session_state["message"] = []

# 添加标题
st.title("AI模型")

# 添加分割线
st.divider()

# 添加输入框
prompt = st.text_input("请输入问题: ")

# 接收到了输入, 则开始工作
if prompt:
    
    # 将用户提出的问题加入历史记录中
    st.session_state["message"].append({"role": "user", "content": prompt})

    # for循环将历史记录全部输出到消息容器内
    for message in st.session_state["message"]:
        st.chat_message(message["role"]).markdown(message["content"])

    with st.spinner("思考中..."):
        response = client.chat(model="deepseek-r1:7b", messages=[{"role": "user", "content": prompt}])

        # 从response中取出来message和content两个key
        st.session_state["message"].append({"role": "assistant", "content": response["message"]["content"]})

        # 在页面中渲染出AI的回答
        st.chat_message("assistant").markdown(response["message"]["content"])
