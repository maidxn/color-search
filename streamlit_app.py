import streamlit as st

st.set_page_config(page_title='Image Search', page_icon=':frame_with_picture')
st.title("Hệ thống tìm kiếm hình ảnh :sunny:")

st.sidebar.header(":camera_with_flash: Tìm kiếm")
uploaded_image = st.sidebar.file_uploader("Tải hình ảnh")
