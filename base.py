import streamlit as st
import os
from PIL import Image


def play_video(vid_path):
    try:
        video_file = open(vid_path, 'rb')
        video_bytes = video_file.read()
        st.video(vid_path)
    except FileNotFoundError:
        pass

def filter_frame(txt_search):
    files = [f for f in os.listdir("./encoded_images") if os.path.isfile(os.path.join("./encoded_images", f))]
    files.sort(key = lambda x: int(x.split()[1][:-4]))
    indices = [i for i, s in enumerate(files) if txt_search.lower() in s]
    return files[indices[0]]


