import streamlit as st


def set_ui_settings() -> None:

    st.set_page_config(page_title="streamlit_audio_recorder")
    st.markdown('''<style>.css-1egvi7u {margin-top: -3rem;}</style>''',
                unsafe_allow_html=True)
    st.markdown('''<style>.stAudio {height: 45px;}</style>''',
                unsafe_allow_html=True)
    st.markdown('''<style>.css-v37k9u a {color: #ff4c4b;}</style>''',
                unsafe_allow_html=True)
    st.markdown('''<style>.css-nlntq9 a {color: #ff4c4b;}</style>''',
                unsafe_allow_html=True)
    st.title('Audio Recorder')
    st.write('\n\n')
