import streamlit as st
from streamlit_folium import st_folium
import folium

st.set_page_config(page_title="VelaTiew", layout="wide")
st.title("🌏 VelaTiew - แอพแนะนำสถานที่ท่องเที่ยว")

st.markdown("เลือกตำแหน่งของคุณ และจุดหมายเพื่อดูเส้นทางและเวลาประมาณการเดินทาง")

# ปุ่มเปิดแผนที่ให้ผู้ใช้เลือกตำแหน่ง
with st.expander("📍 ปักหมุดตำแหน่ง"):
    m = folium.Map(location=[13.736717, 100.523186], zoom_start=6)
    folium.Marker([13.736717, 100.523186], tooltip="Bangkok", popup="คุณอยู่ที่นี่").add_to(m)
    output = st_folium(m, width=700, height=500)

# ความชอบของผู้ใช้
with st.sidebar:
    st.header("🧭 ความชอบของคุณ")
    time = st.selectbox("เวลาที่ชอบเที่ยว", ["เช้า", "บ่าย", "เย็น", "กลางคืน"])
    style = st.selectbox("สไตล์", ["ธรรมชาติ", "คาเฟ่", "ห้าง", "วัด", "ทะเล", "ผจญภัย"])

st.success(f"คุณเลือกสไตล์: {style} เวลาเที่ยว: {time}")
st.info("🎯 ระบบแนะนำสถานที่ตามที่คุณชอบ จะอยู่ตรงนี้ในเวอร์ชันถัดไป 😉")
