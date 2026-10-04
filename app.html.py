import streamlit as st

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="ร้านอาหารออนไลน์", page_icon="🍔", layout="centered")

st.title("🍔 ร้านอาหารอร่อยเด็ด (Food Delivery)")
st.write("ยินดีต้อนรับ! เลือกรายการอาหารที่คุณต้องการสั่งซื้อด้านล่างได้เลยครับ")

# ระบบจัดการตะกร้าสินค้า
if 'cart' not in st.session_state:
    st.session_state.cart = []

# --- 1. เมนูแนะนำประจำวัน ---
st.subheader("⭐ เมนูแนะนำวันนี้")
rec_col1, rec_col2 = st.columns([1, 2])
with rec_col1:
    st.image("https://images.unsplash.com/photo-1589301760014-d929f3979dbc?w=500", caption="กะเพราหมูกรอบ ไข่ดาว", use_container_width=True)
with rec_col2:
    st.markdown("### **🍳 กะเพราหมูกรอบ ไข่ดาว (พิเศษ)**")
    st.write("หมูกรอบผัดพริกแห้งเข้มข้น กรอบนอกนุ่มใน เสิร์ฟพร้อมไข่ดาวกรอบๆ")
    st.write("💰 **ราคา: 75 บาท**")
    if st.button("➕ เพิ่มเมนูแนะนำลงตะกร้า", key="rec_btn", type="primary"):
        st.session_state.cart.append({"name": "กะเพราหมูกรอบ ไข่ดาว (พิเศษ)", "price": 75})
        st.toast("เพิ่มเมนูแนะนำลงในตะกร้าแล้ว!", icon="✅")

st.divider()

# --- 2. หมวดหมู่และรายการอาหาร ---
st.subheader("📋 เมนูทั้งหมด")

# ข้อมูลเมนูแยกตามหมวดหมู่
menu_data = {
    "⚡ อาหารจานด่วน": [
        {"id": 101, "name": "ข้าวผัดต้มยำกุ้ง", "price": 80, "img": "https://images.unsplash.com/photo-1559847844-5315695dadae?w=500"},
        {"id": 102, "name": "ผัดไทยกุ้งสด", "price": 70, "img": "https://images.unsplash.com/photo-1559847844-5315695dadae?w=500"},
        {"id": 103, "name": "ข้าวมันไก่ทอด", "price": 60, "img": "https://images.unsplash.com/photo-1562967914-608f82629710?w=500"},
    ],
    "🍟 ของกินเล่น": [
        {"id": 201, "name": "เฟรนช์ฟรายส์ทอด", "price": 49, "img": "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?w=500"},
        {"id": 202, "name": "นักเก็ตไก่ (6 ชิ้น)", "price": 59, "img": "https://images.unsplash.com/photo-1562967914-608f82629710?w=500"},
        {"id": 203, "name": "เกี๊ยวซ่าทอด", "price": 55, "img": "https://images.unsplash.com/photo-1496116218417-1a781b1c416c?w=500"},
    ],
    "🥤 เครื่องดื่ม": [
        {"id": 301, "name": "ชาไทยเย็น", "price": 35, "img": "https://images.unsplash.com/photo-1558857563-b371033873b8?w=500"},
        {"id": 302, "name": "กาแฟโบราณ", "price": 35, "img": "https://images.unsplash.com/photo-1517701604599-bb29b565090c?w=500"},
        {"id": 303, "name": "น้ำมะนาวโซดา", "price": 40, "img": "https://images.unsplash.com/photo-1513558161293-cdaf765ed2fd?w=500"},
    ]
}

# สร้าง Tab สลับหมวดหมู่
tabs = st.tabs(list(menu_data.keys()))

for tab, (category, items) in zip(tabs, menu_data.items()):
    with tab:
        for item in items:
            col_img, col_detail, col_btn = st.columns([1.5, 2.5, 1.5])
            with col_img:
                st.image(item["img"], use_container_width=True)
            with col_detail:
                st.markdown(f"**{item['name']}**")
                st.write(f"ราคา: **{item['price']} บาท**")
            with col_btn:
                if st.button("➕ สั่งซื้อ", key=f"btn_{item['id']}"):
                    st.session_state.cart.append(item)
                    st.toast(f"เพิ่ม '{item['name']}' ลงตะกร้าแล้ว!", icon="🛒")
            st.write("---")

st.divider()

# --- 3. สรุปตะกร้าสินค้าและรวมยอด ---
st.subheader("🛒 ตะกร้าสินค้าของคุณ")

if not st.session_state.cart:
    st.info("ยังไม่มีสินค้าในตะกร้า เลือกเมนูอร่อยๆ ด้านบนได้เลย!")
else:
    total_price = 0
    
    # แสดงรายการสินค้าในตะกร้า
    for idx, cart_item in enumerate(st.session_state.cart):
        c1, c2 = st.columns([3, 1])
        c1.write(f"{idx+1}. {cart_item['name']}")
        c2.write(f"**{cart_item['price']} ฿**")
        total_price += cart_item['price']
        
    st.markdown("---")
    st.markdown(f"### 💰 **ราคารวมทั้งหมด: {total_price} บาท**")
    
    # ฟอร์มกรอกที่อยู่จัดส่ง
    st.subheader("📍 ข้อมูลการจัดส่ง")
    address = st.text_area("กรอกชื่อ ที่อยู่จัดส่ง และเบอร์โทรศัพท์ติดต่อ", placeholder="ตัวอย่าง: นายใจดี มีสุข 123/45 ถ.สุขุมวิท โทร. 081-234-5678")
    
    col_order, col_clear = st.columns([2, 1])
    with col_order:
        if st.button("✅ ยืนยันการสั่งซื้อ", type="primary", use_container_width=True):
            if not address.strip():
                st.warning("⚠️ กรุณากรอกที่อยู่จัดส่งก่อนยืนยันครับ")
            else:
                st.balloons()
                st.success("🎉 สั่งซื้อสำเร็จ! ร้านค้าได้รับออเดอร์และกำลังจัดเตรียมอาหารให้คุณครับ")
                st.session_state.cart = []
    with col_clear:
        if st.button("🗑️ ล้างตะกร้า", use_container_width=True):
            st.session_state.cart = []
            st.rerun()
