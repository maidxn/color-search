import os

import streamlit as st
from PIL import Image
import time
from helper import *

st.set_page_config(page_title='Image Search', page_icon=':frame_with_picture')
st.title("Hệ thống tìm kiếm hình ảnh :sunny:")

st.sidebar.header("Tìm kiếm")
st.sidebar.write(":open_file_folder: Tải hình ảnh từ máy")
uploaded_image = st.sidebar.file_uploader("")
st.sidebar.write("Hoặc chụp hình ảnh :camera_with_flash:")
picture = st.sidebar.camera_input("")

top = st.sidebar.selectbox(
     'Lựa chọn số lượng hình ảnh trả về:',
     (10, 20, 50, 100, 200, "All"))

run_model = st.sidebar.button("Tìm kiếm")
flag = False
camera = False

if run_model:
    if not uploaded_image and not picture:
        st.sidebar.write("Vui lòng hãy chọn hình ảnh muốn tìm kiếm!")
    else:
        flag = True

with open("imagespath_holiday.pkl", "rb") as file:
    image_paths = pickle.load(file)
data_feature = np.load('demo/histogram_holiday_bin_8.npy')
top = top if top != "All" else len(data_feature)

if flag:
    img_path = uploaded_image if uploaded_image is not None else picture
    if uploaded_image is not None:
        img_name = uploaded_image.name
    else:
        camera = True
    query_img = Image.open(img_path)
    query_img = query_img.resize((250, 300), Image.ANTIALIAS)
    st.image(query_img, "Ảnh tải lên")
    start_time = time.time()
    in_dataset = True
    with st.spinner("Xin vui lòng chờ một chút..."):
        query_arr = np.array(query_img)
        query_arr = query_arr[:, :, ::-1]
        cosine_arr = CalculateCosine_Holiday(query_arr, data_feature, [8, 8, 8])
        top_indices = cosine_arr.argsort()[:-(top+1):-1]
        top_paths = [image_paths[i] for i in top_indices]
    st.success("Tìm kiếm hoàn tất! :tada:")
    end_time = time.time()
    st.write(":stopwatch: Top {} kết quả trả về trong {} s".format(top, round(end_time - start_time, 4)))
    col = st.columns(4)
    paths = []
    for i in range(top):
        res_path = top_paths[i]
        res_path = res_path.replace('/gdrive/MyDrive/', '/')
        image_path = os.getcwd() + res_path
        paths.append(image_path)
    for i in range(top):
        image = Image.open(paths[i])
        image = image.resize((250, 300), Image.ANTIALIAS)
        col[i % 4].image(image)
