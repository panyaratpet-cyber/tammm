import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="ร้านอาหารออนไลน์", page_icon="🍔", layout="centered")

ORDER_FILE = "orders.csv"

# ตรวจสอบไฟล์เก็บข้อมูลถาวร
if not os.path.exists(ORDER_FILE):
    df_init = pd.DataFrame(columns=["Timestamp", "Items", "Total_Price", "Customer_Address"])
    df_init.to_csv(ORDER_FILE, index=False, encoding="utf-8-sig")

st.title("🍔 ร้านอาหารอร่อยเด็ด (Food Delivery)")
st.write("ยินดีต้อนรับ! เลือกรายการอาหารที่คุณต้องการสั่งซื้อด้านล่างได้เลยครับ")

if 'cart' not in st.session_state:
    st.session_state.cart = []

# --- เมนูแนะนำ ---
st.subheader("⭐ เมนูแนะนำวันนี้")
st.markdown("### **🍳 กะเพราหมูกรอบ ไข่ดาว (พิเศษ)**")
st.write("หมูกรอบผัดพริกแห้งเข้มข้น เสิร์ฟพร้อมไข่ดาวกรอบๆ")
st.write("💰 **ราคา: 75 บาท**")
if st.button("➕ เพิ่มเมนูแนะนำลงตะกร้า", key="rec_btn", type="primary"):
    st.session_state.cart.append({"name": "กะเพราหมูกรอบ ไข่ดาว (พิเศษ)", "price": 75})
    st.toast("เพิ่มเมนูแนะนำลงในตะกร้าแล้ว!", icon="✅")

st.divider()

# --- รายการอาหาร ---
st.subheader("📋 เมนูทั้งหมด")

menu_data = {
    "⚡ อาหารจานด่วน": [
        {"id": 101, "name": "กะเพราหมูสับ ไข่ดาว", "price": 60},
        {"id": 102, "name": "ข้าวผัดต้มยำกุ้ง", "price": 80},
        {"id": 103, "name": "ผัดไทยกุ้งสด", "price": 70},
        {"id": 104, "name": "ข้าวมันไก่ทอด", "price": 60},
        {"id": 105, "name": "ข้าวหมูกระเทียม ไข่ดาว", "price": 65},
    ],
    "🍟 ของกินเล่น": [
        {"id": 201, "name": "เฟรนช์ฟรายส์ทอด", "price": 49},
        {"id": 202, "name": "นักเก็ตไก่ (6 ชิ้น)", "price": 59},
        {"id": 203, "name": "เกี๊ยวซ่าทอด (5 ชิ้น)", "price": 55},
    ],
    "🥤 เครื่องดื่ม": [
        {"id": 301, "name": "ชาไทยเย็น", "price": 35},
        {"id": 302, "name": "ชาเขียวนมเย็น", "price": 35},
        {"id": 303, "name": "น้ำมะนาวโซดา", "price": 40},
    ]
}

tabs = st.tabs(list(menu_data.keys()))

for tab, (category, items) in zip(tabs, menu_data.items()):
    with tab:
        for item in items:
            col_detail, col_btn = st.columns([3, 1])
            with col_detail:
                st.markdown(f"**{item['name']}**")
                st.write(f"ราคา: **{item['price']} บาท**")
            with col_btn:
                if st.button("➕ สั่งซื้อ", key=f"btn_{item['id']}"):
                    st.session_state.cart.append(item)
                    st.toast(f"เพิ่ม '{item['name']}' ลงตะกร้าแล้ว!", icon="🛒")
            st.write("---")

st.divider()

# --- ตะกร้าสินค้าและการสั่งซื้อ ---
st.subheader("🛒 ตะกร้าสินค้าของคุณ")

if not st.session_state.cart:
    st.info("ยังไม่มีสินค้าในตะกร้า เลือกเมนูอร่อยๆ ด้านบนได้เลย!")
else:
    total_price = 0
    items_list = []
    
    for idx, cart_item in enumerate(st.session_state.cart):
        c1, c2 = st.columns([3, 1])
        c1.write(f"{idx+1}. {cart_item['name']}")
        c2.write(f"**{cart_item['price']} ฿**")
        total_price += cart_item['price']
        items_list.append(cart_item['name'])
        
    st.markdown("---")
    st.markdown(f"### 💰 **ราคารวมทั้งหมด: {total_price} บาท**")
    
    st.subheader("📍 ข้อมูลการจัดส่ง")
    address = st.text_area("กรอกชื่อ ที่อยู่จัดส่ง และเบอร์โทรศัพท์ติดต่อ", placeholder="ตัวอย่าง: นายใจดี มีสุข 123/45 ถ.สุขุมวิท โทร. 081-234-5678")
    
    col_order, col_clear = st.columns([2, 1])
    with col_order:
        if st.button("✅ ยืนยันการสั่งซื้อ", type="primary", use_container_width=True):
            if not address.strip():
                st.warning("⚠️ กรุณากรอกที่อยู่จัดส่งก่อนยืนยันครับ")
            else:
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                order_data = {
                    "Timestamp": [now],
                    "Items": [", ".join(items_list)],
                    "Total_Price": [total_price],
                    "Customer_Address": [address]
                }
                new_df = pd.DataFrame(order_data)
                new_df.to_csv(ORDER_FILE, mode='a', header=False, index=False, encoding="utf-8-sig")
                
                st.balloons()
                st.success("🎉 สั่งซื้อสำเร็จ! ร้านค้าได้รับออเดอร์แล้ว")
                st.session_state.cart = []
    with col_clear:
        if st.button("🗑️ ล้างตะกร้า", use_container_width=True):
            st.session_state.cart = []
            st.rerun()

# --- สำหรับผู้ดูแลระบบ ---
st.divider()
with st.expander("📊 สำหรับเจ้าของร้าน: ดูประวัติออเดอร์ทั้งหมด"):
    if os.path.exists(ORDER_FILE):
        df_orders = pd.read_csv(ORDER_FILE)
        st.dataframe(df_orders)
