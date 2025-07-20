import streamlit as st
import os

from src.langgraphagenticai.UII.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(page_title="🥷 " + self.config.get_page_title(), layout="wide")

        # Ninja-Themed Dark Neon CSS + Readable Chat Fix
        st.markdown("""
            <style>
            body {
                background-color: #0a0a0a;
                font-family: 'Segoe UI', sans-serif;
                color: #f2f2f2;
            }
            .main {
                background-color: #0d0d0d;
                color: #f2f2f2;
            }
            .block-container {
                padding: 2rem;
                border-radius: 12px;
                background: linear-gradient(145deg, #0f0f0f, #1a1a1a);
                box-shadow: 0px 0px 12px #00ffcc44;
                color: #e6e6e6;
            }
            .sidebar .sidebar-content {
                background: linear-gradient(to bottom, #111, #1e1e1e);
                color: #f2f2f2;
                border-right: 1px solid #00ffcc55;
            }
            h1, h2, h3, h4, h5, h6 {
                color: #00ffcc;
                text-shadow: 0 0 4px #00ffcc;
            }
            .stMarkdown p, .stText, .stMarkdown {
                color: #e6e6e6 !important;
            }
            .stSelectbox > div > div {
                background-color: #121212 !important;
                color: #00ffcc !important;
            }
            .stTextInput > div > div > input {
                background-color: #121212;
                color: #00ffcc;
            }
            .stTextInput label {
                color: #00ffcc;
            }
            .stAlert {
                background-color: #2b0000;
                border-left: 5px solid red;
            }
            </style>
        """, unsafe_allow_html=True)

        # Ninja Header
        st.markdown(f"""
            <div style="background: linear-gradient(135deg, #111111, #1e1e1e); padding: 25px;
                        border-radius: 12px; border: 2px solid #00ffcc; box-shadow: 0 0 15px #00ffcc88;">
                <h1 style="color:#00ffcc; text-align:center; text-shadow: 0 0 6px #00ffcc;">🥷 {self.config.get_page_title()}</h1>
                <p style="text-align:center; color:#ccc; font-size: 16px; margin-top: 10px;">
                    Welcome to the dojo of language intelligence. Be swift. Be silent. Be smart.
                </p>
            </div>
        """, unsafe_allow_html=True)

        with st.sidebar:
            st.markdown("## 🗡️ Select Your Weapon (LLM)")
            st.divider()

            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            # LLM Selection
            self.user_controls["selected_llm"] = st.selectbox("🎴 Choose LLM", llm_options)

            if self.user_controls["selected_llm"] == 'Groq':
                st.markdown("## ⚙️ Groq Configuration")
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("🧠 Select Model", model_options)

                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("🔐 Enter API Key", type="password")

                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("🚫 API Key Missing! [Generate one](https://console.groq.com/keys)", icon="⚠️")

            st.markdown("---")
            st.markdown("## 🎯 Choose Your Mission")
            self.user_controls["selected_usecase"] = st.selectbox("🎯 Select Usecases", usecase_options)

            st.markdown("---")
            st.markdown("🕶️ <small>Stay hidden, strike precisely.</small>", unsafe_allow_html=True)

        return self.user_controls
