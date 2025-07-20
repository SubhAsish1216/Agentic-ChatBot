import streamlit as st
import os

from src.langgraphagenticai.UII.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(page_title="🤖 " + self.config.get_page_title(), layout="wide")
        
        # Inject custom Ninja CSS
        st.markdown("""
            <style>
            /* Background Ninja Blade Animation */
            body {
                background: linear-gradient(315deg, #0f0f0f 0%, #1a1a1a 74%);
                color: #e0e0e0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                overflow-x: hidden;
            }

            .block-container {
                background: rgba(0,0,0,0.3);
                padding: 2rem;
                border-radius: 15px;
                box-shadow: 0 0 30px #ff0000a1;
            }

            /* Sidebar Theme */
            section[data-testid="stSidebar"] {
                background: linear-gradient(135deg, #111 0%, #1b1b1b 100%);
                color: #fff;
                border-right: 2px solid #ff3131;
            }

            /* Header style */
            h1 {
                color: #ff3131;
                text-shadow: 1px 1px 8px black;
                font-size: 3rem;
                font-weight: 900;
            }

            /* Selectbox styling */
            .stSelectbox div[data-baseweb="select"] {
                background-color: #1c1c1c;
                border: 1px solid #ff3131;
                border-radius: 8px;
            }

            /* Text input styling */
            input {
                background-color: #1c1c1c !important;
                color: #fff !important;
            }

            /* Warning styling */
            .stAlert {
                background-color: #330000;
                border-left: 6px solid red;
            }

            /* Ninja GIF */
            .ninja-gif {
                position: fixed;
                bottom: 10px;
                right: 10px;
                z-index: 9999;
                width: 130px;
            }

            /* Blade Animation */
            @keyframes blade-spin {
                0% { transform: rotate(0deg) scale(1); opacity: 0.4;}
                50% { transform: rotate(180deg) scale(1.2); opacity: 0.8;}
                100% { transform: rotate(360deg) scale(1); opacity: 0.4;}
            }

            .blade {
                position: fixed;
                top: 50%;
                left: 50%;
                width: 120px;
                height: 120px;
                background-image: url('https://i.imgur.com/jxWqIBf.png'); /* Ninja blade PNG */
                background-size: contain;
                background-repeat: no-repeat;
                animation: blade-spin 6s linear infinite;
                transform: translate(-50%, -50%);
                opacity: 0.2;
                z-index: 0;
            }
            </style>

            <div class="blade"></div>
            <img src="https://media.tenor.com/NXH0-GjJdGQAAAAi/ninja-jump.gif" class="ninja-gif" />
        """, unsafe_allow_html=True)

        # Header
        st.header("🤖 " + self.config.get_page_title())

        with st.sidebar:
            # Get options from config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            # LLM selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == 'Groq':
                # Model selection
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("API Key", type="password")

                # Validate API key
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("⚠️ Please enter your GROQ API key to proceed. Don't have? refer : https://console.groq.com/keys")

            # Usecase selection
            self.user_controls["selected_usecase"] = st.selectbox("Select Usecases", usecase_options)

        return self.user_controls
