import streamlit as st

st.set_page_config(page_title="ร้านอาหารออนไลน์", page_icon="🍔", layout="centered")

st.title("🍔 ร้านอาหารอร่อยเด็ด (Food Delivery)")
st.write("ยินดีต้อนรับ! เลือกรายการอาหารที่คุณต้องการสั่งซื้อด้านล่างได้เลยครับ")

# ตรวจสอบการย่อหน้าตรงนี้
if 'cart' not in st.session_state:
    st.session_state.cart = []

menu = [
    {"id": 1, "name": "กะเพราหมูกรอบ ไข่ดาว", "price": 65, "emoji": "🍳"},
    {"id": 2, "name": "ข้าวผัดต้มยำกุ้ง", "price": 80, "emoji": "🍤"},
    {"id": 3, "name": "ผัดไทยกุ้งสด", "price": 70, "emoji": "🍝"},
    {"id": 4, "name": "ชาไทยเย็น", "price": 35, "emoji": "🧋"}
]

st.subheader("📋 เมนูอาหาร")
for item in menu:
    col1, col2, col3 = st.columns([3, 2, 2])
    with col1:
        st.write(f"**{item['emoji']} {item['name']}**")
    with col2:
        st.write(f"{item['price']} บาท")
    with col3:
        if st.button("เพิ่มลงตะกร้า", key=f"btn_{item['id']}"):
            st.session_state.cart.append(item)
            st.toast(f"เพิ่ม '{item['name']}' ลงในตะกร้าแล้ว!", icon="✅")

st.divider()

st.subheader("🛒 ตะกร้าสินค้าของคุณ")

if not st.session_state.cart:
    st.info("ยังไม่มีสินค้าในตะกร้า")
else:
    total_price = 0
    for idx, cart_item in enumerate(st.session_state.cart):
        c1, c2 = st.columns([4, 1])
        c1.write(f"- {cart_item['name']} ({cart_item['price']} บาท)")
        total_price += cart_item['price']
        
    st.markdown(f"### **ราคารวมทั้งหมด: {total_price} บาท**")
    
    st.subheader("📍 ข้อมูลการจัดส่ง")
    address = st.text_area("กรอกชื่อ และ ที่อยู่จัดส่ง/เบอร์โทรศัพท์")
    
    col_order, col_clear = st.columns([2, 1])
    with col_order:
        if st.button("✅ ยืนยันการสั่งซื้อ", type="primary"):
            if not address:
                st.warning("กรุณากรอกที่อยู่จัดส่งก่อนครับ")
            else:
                st.balloons()
                st.success("สั่งซื้อเรียบร้อยแล้ว! ร้านค้ากำลังเตรียมอาหารให้คุณครับ")
                st.session_state.cart = []
    with col_clear:
        if st.button("ล้างตะกร้า"):
            st.session_state.cart = []
            st.rerun()
