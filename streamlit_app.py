import streamlit as st
import os
from PIL import Image

st.set_page_config(page_title='Image Search', page_icon=':frame_with_picture')
st.title("Hệ thống tìm kiếm hình ảnh :sunny:")

st.sidebar.header("Tìm kiếm")
st.sidebar.write(":open_file_folder: Tải hình ảnh từ máy")
uploaded_image = st.sidebar.file_uploader("")
st.sidebar.write("Hoặc chụp hình ảnh :camera_with_flash:")
picture = st.sidebar.camera_input("")

run_model = st.sidebar.button("Tìm kiếm")
flag = False

if run_model:
    if not uploaded_image and not picture:
        st.sidebar.write("Vui lòng hãy chọn hình ảnh muốn tìm kiếm!")
    else:
        flag = True


if flag:
    st.write(":tada:")
    col = st.columns(4)
    image_path = os.getcwd() + '/dataset/sunrise/'
    l = os.listdir(image_path)
    for i in range(20):
        image = Image.open(image_path + l[i])
        image = image.resize((250, 300), Image.ANTIALIAS)
        col[i % 4].image(image)

