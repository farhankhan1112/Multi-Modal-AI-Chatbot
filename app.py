import streamlit as st
import google.generativeai as genai
from PIL import Image
from pypdf import PdfReader

# ================= CONFIG =================
genai.configure(api_key="Enter GEMINI API KEY")

TEXT_MODEL = genai.GenerativeModel("gemini-2.5-flash")
VISION_MODEL = genai.GenerativeModel("gemini-2.5-flash")

# ================= PAGE SETUP =================
st.set_page_config(page_title="Multi-Modal AI Chatbot", layout="centered")
st.title("🤖 Multi-Modal AI Chatbot")
st.caption("Text • Image • Document Intelligence")

# ================= SESSION STATE =================
if "messages" not in st.session_state:
    st.session_state.messages = []

# ================= CLEAR CHAT BUTTON =================
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()



# ================= CHAT HISTORY =================
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ================= MODE SELECTION =================
mode = st.selectbox(
    "Choose Interaction Mode",
    ["Text Chat", "Image + Text Analysis", "PDF Document Chat"]
)

# ================= TEXT CHAT =================
if mode == "Text Chat":
    user_input = st.chat_input("Ask me anything...")

    if user_input:
        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )

        response = TEXT_MODEL.generate_content(user_input)

        st.session_state.messages.append(
            {"role": "assistant", "content": response.text}
        )

        with st.chat_message("assistant"):
            st.markdown(response.text)

# ================= IMAGE CHAT =================
if mode == "Image + Text Analysis":
    uploaded_image = st.file_uploader(
        "Upload an image",
        type=["png", "jpg", "jpeg"]
    )

    image_prompt = st.text_input(
        "What do you want to know about this image?"
    )

    if uploaded_image:
        image = Image.open(uploaded_image)
        st.image(
            image,
            caption="Uploaded Image",
            width=150   # 👈 passport-size control
        )

    if st.button("Analyze Image"):
        if not uploaded_image or not image_prompt.strip():
            st.warning("Upload an image and enter a prompt.")
        else:
            response = VISION_MODEL.generate_content(
                [image_prompt, image]
            )

            st.session_state.messages.append(
                {"role": "assistant", "content": response.text}
            )

            with st.chat_message("assistant"):
                st.markdown(response.text)

# ================= PDF DOCUMENT CHAT =================
if mode == "PDF Document Chat":
    uploaded_pdf = st.file_uploader(
        "Upload a PDF document",
        type=["pdf"]
    )

    pdf_question = st.text_input(
        "Ask a question about the document"
    )

    if uploaded_pdf:
        reader = PdfReader(uploaded_pdf)
        document_text = ""

        for page in reader.pages:
            document_text += page.extract_text()

    if st.button("Ask Document"):
        if not uploaded_pdf or not pdf_question.strip():
            st.warning("Upload a PDF and enter a question.")
        else:
            prompt = f"""
            You are an AI assistant.
            Answer the question using ONLY the content from the document below.

            DOCUMENT:
            {document_text}

            QUESTION:
            {pdf_question}
            """

            response = TEXT_MODEL.generate_content(prompt)

            st.session_state.messages.append(
                {"role": "assistant", "content": response.text}
            )

            with st.chat_message("assistant"):
                st.markdown(response.text)

