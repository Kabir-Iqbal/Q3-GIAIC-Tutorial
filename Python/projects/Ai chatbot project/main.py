# import google.generativeai as genai
# import streamlit as st


# # **Chat History Initialize کریں**
# if "history" not in st.session_state:
#     st.session_state.history = []


# def gemini_process(c): 
# # Apni API key yahan replace karo
#     genai.configure(api_key="AIzaSyAVAIytHZ8twHge1I6LdZfT2l5sV8u3Wfg")

#     try:
#     # Gemini 1.5 Flash model initialize karna
#         model = genai.GenerativeModel("gemini-1.5-flash")

#         # System Prompt define karna
#         system_prompt = """
#         You are an AI assistant named Jarvis.Your age is 21 years old, and you were created by Kabir Iqbal.
#         You can only reply in these language English or Urdu. If the user writes in **Roman Urdu or Roman English**,
#         then reply in the same format, and your bestfriend is Chaudhry palipoto and your Teacher is Sir Ameen Alam and Sir Zia.
#         """

#         # Chat session initialize karna
#         chat = model.start_chat(history=[])

#         # System Prompt ko history mein add karna
#         chat.send_message(system_prompt)

#         # User ka input
#         user_input = c
    
#         # AI se response lena
#         response = chat.send_message(user_input)

#         # Output print karna
#         print(response.text)

#     except Exception as e:
#         print(f"Error: {e}")
#     return response.text




# # **Streamlit UI**
# st.title("🤖 Chatbot")

# user_question = st.text_input("Ask anything:")

# if st.button("Ask"):
#     if user_question.strip():  # Input خالی نہ ہو
#           # **User کا سوال فوراً Print کریں**
#         user_message = st.empty()
#         user_message.write(f"🧑 **You:** {user_question}")
#         st.session_state.history.append(("🧑 You:", user_question))
        
#         # **Gemini سے جواب لینا اور اسے بھی محفوظ کرنا**
#         response = gemini_process(user_question)
#         st.session_state.history.append(("🤖 Jarvis:", response))

#         # **UI فوری Update کریں**
#         st.rerun()

        
       
#     else :
#         "Please enter a question"


# # **Chat History Display کریں**
# for role, text in st.session_state.history:
#     st.write(f"**{role}** {text}")
    



import google.generativeai as genai       #import gemini
import streamlit as st                    # import streamlit for ui

# **Chat History Initialize کریں**
if "history" not in st.session_state:              # agr histor variable st.session_state m na ho to khali array dekhaye 
    st.session_state.history = []

# **Gemini API Function**
def gemini_process(c): 
    genai.configure(api_key="AIzaSyAVAIytHZ8twHge1I6LdZfT2l5sV8u3Wfg")     # google studio key
    
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")                  # use 1.5 flash model which give fastest reply
        
        # give a prompt to model what you are and how can you reply response
        system_prompt = """
        You are an AI assistant named Jarvis. Your age is 21 years old, and you were created by Kabir Iqbal. and You are learning Agentic Ai from GIAIC
        You can only reply in English or Urdu. If the user writes in **Roman Urdu or Roman English**, then reply in the same format.
        Your best friend is Hussain , and your Teachers are Sir Ameen Alam and Sir Zia.
        """
        
        chat = model.start_chat(history=[])      #Gemini se ek nayi chatt start ki gayi he or history khali raakhi he taky nayi chatt saff dikhy
        chat.send_message(system_prompt)         # yahn gemini ko pehly se guide kr diya he propmpt variable deky

        response = chat.send_message(c)       # gemini ko usermessage bheja he fr wo jawab dega badly m
        return response.text                 # yahan gemini response return kiya  he 

    except Exception as e:             # error handling
        return f"⚠️ Error: {e}"

# **Streamlit UI**
st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="centered")             # ui ko behtr look deny k leye use ki
st.title("🤖 AI Chatbot ")

# **Stylish Chat Container**
chat_container = st.container()         # yahan ek chatt container bnaya he

# **Chat History Display (Professional UI)**
with chat_container:
    for role, text in st.session_state.history:            # yahan hr session.state ka  message ko loop m challa raha he 
        with st.chat_message("user" if "You" in role else "assistant"):      # agr your he to role you hoga nahi to assistant
            st.markdown(f"**{role}** {text}")              # st.markdown se role ko bold kiya gaya he 

# **User Input Box**
user_question = st.chat_input("Ask anything...")

if user_question:
    # **User کا سوال فوراً Print کریں**
    # st.session_state.history.append(("🧑 You:", user_question))
    # with st.chat_message("user"):
    #     st.markdown(f"**🧑 You:** {user_question}")

       # **یوزر کا سوال فوراً پرنٹ کریں**
    st.session_state.history.append(("🧑 You:", user_question))
    with st.chat_message("user"):
        st.markdown(f"**🧑 You:** {user_question}")


        # **جب تک Gemini جواب نہ دے، تب تک "Typing..." دکھائیں**
    with st.chat_message("assistant"):
        with st.spinner("Typing..."):  # ⏳ لوڈنگ انڈیکیٹر
            response = gemini_process(user_question)  # Gemini API Call
            st.session_state.history.append(("🤖", response))


         # **API response کے بعد اصل جواب دکھائیں**
        st.markdown(f"**🤖 :** {response}")
        st.rerun()  # فوراً UI ری لوڈ کریں





    # # **Gemini سے جواب لینا اور اسے بھی محفوظ کرنا**
    # response = gemini_process(user_question)
    # st.session_state.history.append(("🤖", response))
    
    # with st.chat_message("assistant"):
    #     st.markdown(f"**🤖 :** {response}")

