from django.core.wsgi import get_wsgi_application
from django.core.files import File

import os
import numpy as np
import streamlit as st
import streamlit.components.v1 as components
from io import BytesIO

from utils import set_ui_settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
application = get_wsgi_application()


def add_text_input():
    with st.form("my_form", clear_on_submit=True):
        text = st.text_area(label="Enter text",)

        submitted = st.form_submit_button("Submit")
        if submitted:

            if len(text) < 5:
                st.markdown(
                    '<p style="color: red;">Text is too short</p>', unsafe_allow_html=True)
            else:
                from posts.models import Post
                Post.objects.create(text=text)
                st.session_state.more_stuff = True


def add_id_input():

    with st.form("id_form", clear_on_submit=True):
        st.session_state.more_stuff = True
        id_ = st.text_area(label="Enter id",)

        submitted = st.form_submit_button("Submit")
        if submitted:

            from posts.models import Post
            if Post.objects.filter(id=id_, audio__isnull=False).exists():
                st.audio(Post.objects.get(
                    id=id_).audio.read(), )

            else:
                st.markdown(
                    '<p style="color: red;">Id does not exist</p>', unsafe_allow_html=True)


def audiorec_demo_app():

    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "st_audiorec/frontend/build")
    st_audiorec = components.declare_component("st_audiorec", path=build_dir)

    from posts.models import Post

    set_ui_settings()
    area_ = st.empty()

    click = st.button("Next", key="test",)
    post = Post.objects.filter(
            audio__in=[None, '']).order_by("id").first()
    if click:
        st.session_state.more_stuff = True
        area_.text_area(label="Text to read", height=100,
                        disabled=True,)

        if post:
            area_.text_area(value=f"{post.text}", disabled=True,
                            label="Text to read")

        else:
            st.markdown(
                '<p style="color: red;">No text without audio exists</p>', unsafe_allow_html=True)

    val = st_audiorec()

    if isinstance(val, dict):
        with st.spinner('retrieving audio-recording...'):
            ind, audio_val = zip(*val['arr'].items())
            ind = np.array(ind, dtype=int)
            audio_val = np.array(audio_val)
            sorted_ints = audio_val[ind]
            stream = BytesIO(
                b"".join([int(v).to_bytes(1, "big") for v in sorted_ints]))
            wav_bytes = stream.read()

        if val['save']:
            print(val['save'])
            # post = Post.objects.filter(
            #     audio__in=[None, '']).order_by("id").first()
            file = File(stream, name="audio.wav")
            if post:
                post.audio = file
                post.save()
        st.audio(wav_bytes, format='audio/wav')

    # st.header('Add text sample')
    # add_text_input()
    add_id_input()


if __name__ == '__main__':

    audiorec_demo_app()
