import streamlit as st
from groq import Groq

# 1. Page Configuration
st.set_page_config(page_title="Ibadat AI Assistant", page_icon="🎓", layout="centered")

st.title("🎓 Ibadat AI Assistant")
st.info("Ask me about your courses, assignments, or general knowledge!")

# 2. Access Secret API Key (From Streamlit Secrets Cloud)
# This replaces the manual text input for a better user experience
try:
    gen_api_key = st.secrets["GROQ_API_KEY"]
except:
    st.error("API Key not found in Secrets! Please add GROQ_API_KEY to Streamlit Cloud settings.")
    st.stop()

client = Groq(api_key=gen_api_key)

# 3. Initialize Chat History & System Instructions
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system", 
            "content": """
            You are Ms. Sarah, a dedicated English Teacher at Ibadat International University. 
            
            Your personality: Patient, articulate, and highly observant.
            
            Your rules:
            1. Help students improve their English proficiency.
            2. If the student makes a grammatical error, gently point it out at the end of your response.
            3. Encourage the use of academic vocabulary.
            4. If they ask for a definition, provide the meaning and an example sentence.
            """
        }
    ]
# 4. Display Chat History
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# 5. User Input and Logic
if prompt := st.chat_input("What is on your mind?"):
    # Add user message to state
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate Assistant Response
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        # Stream the response for a "typing" effect
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
            stream=True
        )

        for chunk in completion:
            content = chunk.choices[0].delta.content
            if content:
                full_response += content
                response_placeholder.markdown(full_response + "▌")
        
        response_placeholder.markdown(full_response)
    
    # Save assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# 6. Sidebar Utilities
with st.sidebar:
    st.divider()
    if st.button("Clear Conversation"):
        st.session_state.messages = [st.session_state.messages[0]] # Reset but keep system prompt
        st.rerun()
