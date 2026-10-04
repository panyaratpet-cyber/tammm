<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AroyDee - แอปสั่งอาหารออนไลน์</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Google Fonts (Prompt) -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        brand: {
                            50: '#fff7ed',
                            100: '#ffedd5',
                            500: '#f97316',
                            600: '#ea580c',
                            700: '#c2410c',
                        }
                    },
                    fontFamily: {
                        sans: ['Prompt', 'sans-serif'],
                    }
                }
            }
        }
    </script>
    <style>
        body { font-family: 'Prompt', sans-serif; }
        .hide-scrollbar::-webkit-scrollbar { display: none; }
        .hide-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
    </style>
</head>
<body class="bg-gray-50 text-gray-800 antialiased min-h-screen flex flex-col pb-20 md:pb-0">

    <!-- Navigation Bar -->
    <header class="sticky top-0 z-40 bg-white/95 backdrop-blur-md shadow-sm border-b border-orange-100">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex items-center justify-between h-16">
                <!-- Logo -->
                <div class="flex items-center gap-2 cursor-pointer" onclick="switchTab('menu')">
                    <div class="w-10 h-10 rounded-full bg-gradient-to-tr from-orange-500 to-amber-400 flex items-center justify-center text-white shadow-lg shadow-orange-500/30">
                        <i class="fa-solid font-bold fa-utensils text-xl"></i>
                    </div>
                    <div>
                        <span class="text-2xl font-bold bg-gradient-to-r from-orange-600 to-amber-500 bg-clip-text text-transparent">AroyDee</span>
                        <span class="hidden sm:inline-block text-xs bg-orange-100 text-orange-700 px-2 py-0.5 rounded-full ml-1 font-medium">อร่อยดี Express</span>
                    </div>
                </div>

                <!-- Navigation Desktop Links -->
                <nav class="hidden md:flex items-center space-x-1">
                    <button onclick="switchTab('menu')" id="nav-menu" class="nav-btn px-4 py-2 rounded-full font-medium text-orange-600 bg-orange-50">
                        <i class="fa-solid fa-utensils mr-2"></i>เมนูอาหาร
                    </button>
                    <button onclick="switchTab('tracking')" id="nav-tracking" class="nav-btn px-4 py-2 rounded-full font-medium text-gray-600 hover:bg-orange-50 hover:text-orange-600 transition">
                        <i class="fa-solid fa-motorcycle mr-2"></i>ติดตามคำสั่งซื้อ
                    </button>
                    <button onclick="switchTab('history')" id="nav-history" class="nav-btn px-4 py-2 rounded-full font-medium text-gray-600 hover:bg-orange-50 hover:text-orange-600 transition">
                        <i class="fa-solid fa-clock-rotate-left mr-2"></i>ประวัติการสั่งซื้อ
                    </button>
                </nav>

                <!-- Cart Button -->
                <div class="flex items-center gap-3">
                    <button onclick="toggleCartDrawer(true)" class="relative p-2.5 bg-orange-500 hover:bg-orange-600 text-white rounded-full shadow-md shadow-orange-500/20 transition flex items-center gap-2 px-4">
                        <i class="fa-solid fa-basket-shopping text-lg"></i>
                        <span class="hidden sm:inline font-medium">ตะกร้า</span>
                        <span id="cart-badge" class="bg-white text-orange-600 text-xs font-bold w-5 h-5 rounded-full flex items-center justify-center">0</span>
                    </button>
                </div>
            </div>
        </div>
    </header>

    <!-- Main Content Container -->
    <main class="flex-grow max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-6">

        <!-- TAB 1: MENU VIEW -->
        <section id="tab-menu" class="space-y-6">
            <!-- Hero Banner -->
            <div class="relative rounded-3xl overflow-hidden bg-gradient-to-r from-orange-500 to-amber-500 text-white p-6 md:p-10 shadow-xl">
                <div class="relative z-10 max-w-2xl">
                    <span class="bg-white/20 backdrop-blur-md px-3 py-1 rounded-full text-xs font-semibold uppercase tracking-wider">โปรโมชันพิเศษวันนี้</span>
                    <h1 class="text-3xl sm:text-4xl md:text-5xl font-extrabold mt-2 leading-tight">ส่งฟรีทุกออเดอร์! <br class="hidden sm:inline">เมื่อสั่งครบ 250 บาท</h1>
                    <p class="mt-2 text-orange-100 text-sm sm:text-base">อร่อย สด ใหม่ ส่งตรงถึงบ้านคุณภายใน 30 นาที Code: <span class="font-bold underline decoration-amber-200">AROY20</span> ลดเพิ่ม 20 บาท</p>
                </div>
                <div class="absolute right-[-20px] bottom-[-20px] opacity-20 sm:opacity-40 pointer-events-none">
                    <i class="fa-solid fa-burger text-[200px] text-white"></i>
                </div>
            </div>

            <!-- Search and Filter Bar -->
            <div class="flex flex-col sm:flex-row gap-3 items-center justify-between">
                <!-- Search Box -->
                <div class="relative w-full sm:w-80">
                    <i class="fa-solid fa-magnifying-glass absolute left-4 top-1/2 -translate-y-1/2 text-gray-400"></i>
                    <input type="text" id="search-input" oninput="filterMenuItems()" placeholder="ค้นหาชื่ออาหาร..." class="w-full pl-11 pr-4 py-2.5 rounded-full border border-gray-200 focus:outline-none focus:border-orange-500 focus:ring-2 focus:ring-orange-200 text-sm shadow-sm transition">
                </div>

                <!-- Sort & Spicy Filter Options -->
                <div class="flex items-center gap-2 w-full sm:w-auto overflow-x-auto pb-1 sm:pb-0 hide-scrollbar">
                    <select id="sort-select" onchange="filterMenuItems()" class="bg-white border border-gray-200 text-xs font-medium text-gray-700 py-2 px-3 rounded-full focus:outline-none focus:border-orange-500 shadow-sm">
                        <option value="default">เรียงตาม: แนะนำ</option>
                        <option value="price-low">ราคา: น้อย -> มาก</option>
                        <option value="price-high">ราคา: มาก -> น้อย</option>
                        <option value="rating">คะแนนรีวิวสูงสุด</option>
                    </select>

                    <button onclick="toggleSpicyFilter()" id="btn-spicy-filter" class="px-3 py-2 border border-gray-200 rounded-full text-xs font-medium text-gray-600 bg-white hover:bg-orange-50 whitespace-nowrap transition flex items-center gap-1 shadow-sm">
                        <i class="fa-solid fa-pepper-hot text-red-500"></i>
                        <span>เฉพาะเมนูเผ็ด</span>
                    </button>
                </div>
            </div>

            <!-- Category Tabs -->
            <div id="category-container" class="flex gap-2 overflow-x-auto pb-2 hide-scrollbar">
                <!-- Dynamic categories loaded by JS -->
            </div>

            <!-- Food Grid -->
            <div>
                <h2 id="category-title" class="text-xl font-bold text-gray-800 mb-4 flex items-center gap-2">
                    <span class="w-2 h-6 bg-orange-500 rounded-full inline-block"></span>
                    รายการอาหารทั้งหมด
                </h2>
                <div id="food-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
                    <!-- Dynamic food items loaded by JS -->
                </div>
                <div id="empty-search" class="hidden text-center py-12">
                    <i class="fa-solid fa-utensils text-5xl text-gray-300 mb-3"></i>
                    <p class="text-gray-500 font-medium">ไม่พบเมนูอาหารที่คุณค้นหา</p>
                </div>
            </div>
        </section>

        <!-- TAB 2: LIVE TRACKING VIEW -->
        <section id="tab-tracking" class="hidden max-w-3xl mx-auto space-y-6">
            <div id="no-active-order" class="bg-white rounded-3xl p-8 text-center shadow-sm border border-orange-100">
                <div class="w-20 h-20 bg-orange-100 text-orange-500 rounded-full flex items-center justify-center mx-auto mb-4 text-3xl">
                    <i class="fa-solid fa-receipt"></i>
                </div>
                <h2 class="text-2xl font-bold text-gray-800 mb-2">ไม่มีออเดอร์ที่กำลังดำเนินอยู่</h2>
                <p class="text-gray-500 text-sm mb-6">คุณยังไม่มีคำสั่งซื้อที่อยู่ระหว่างการจัดส่งในขณะนี้</p>
                <button onclick="switchTab('menu')" class="px-6 py-3 bg-orange-500 hover:bg-orange-600 text-white rounded-full font-medium shadow-md shadow-orange-500/20 transition">
                    สั่งอาหารเลย
                </button>
            </div>

            <div id="active-order-container" class="hidden bg-white rounded-3xl p-6 sm:p-8 shadow-md border border-orange-100 space-y-6">
                <!-- Order Header -->
                <div class="flex flex-wrap items-center justify-between border-b pb-4 gap-2">
                    <div>
                        <span class="text-xs text-gray-400 font-medium uppercase">หมายเลขออเดอร์</span>
                        <h3 id="tracking-order-id" class="text-lg font-bold text-gray-800">#ORD-XXXXXX</h3>
                    </div>
                    <div class="text-right">
                        <span id="tracking-estimated-time" class="inline-block px-3 py-1 bg-orange-100 text-orange-700 text-xs font-bold rounded-full">
                            คาดว่าจะได้รับใน 25-30 นาที
                        </span>
                    </div>
                </div>

                <!-- Progress Steps Bar -->
                <div class="relative py-4">
                    <!-- Progress Line -->
                    <div class="absolute top-1/2 left-0 right-0 h-1.5 bg-gray-200 -translate-y-1/2 rounded-full z-0"></div>
                    <div id="progress-bar-fill" class="absolute top-1/2 left-0 h-1.5 bg-orange-500 -translate-y-1/2 rounded-full z-0 transition-all duration-500" style="width: 25%;"></div>

                    <!-- Steps Icons -->
                    <div class="relative z-10 flex justify-between">
                        <!-- Step 1 -->
                        <div class="step-node flex flex-col items-center" data-step="1">
                            <div class="step-icon w-10 h-10 rounded-full bg-orange-500 text-white flex items-center justify-center font-bold text-sm shadow-md transition-all">
                                <i class="fa-solid fa-check"></i>
                            </div>
                            <span class="text-xs font-semibold text-gray-800 mt-2">รับออเดอร์</span>
                        </div>
                        <!-- Step 2 -->
                        <div class="step-node flex flex-col items-center" data-step="2">
                            <div class="step-icon w-10 h-10 rounded-full bg-gray-200 text-gray-500 flex items-center justify-center font-bold text-sm shadow-md transition-all">
                                <i class="fa-solid fa-kitchen-set"></i>
                            </div>
                            <span class="text-xs font-semibold text-gray-500 mt-2">กำลังปรุง</span>
                        </div>
                        <!-- Step 3 -->
                        <div class="step-node flex flex-col items-center" data-step="3">
                            <div class="step-icon w-10 h-10 rounded-full bg-gray-200 text-gray-500 flex items-center justify-center font-bold text-sm shadow-md transition-all">
                                <i class="fa-solid fa-motorcycle"></i>
                            </div>
                            <span class="text-xs font-semibold text-gray-500 mt-2">กำลังจัดส่ง</span>
                        </div>
                        <!-- Step 4 -->
                        <div class="step-node flex flex-col items-center" data-step="4">
                            <div class="step-icon w-10 h-10 rounded-full bg-gray-200 text-gray-500 flex items-center justify-center font-bold text-sm shadow-md transition-all">
                                <i class="fa-solid fa-house-chimney"></i>
                            </div>
                            <span class="text-xs font-semibold text-gray-500 mt-2">จัดส่งสำเร็จ</span>
                        </div>
                    </div>
                </div>

                <!-- Live Status Message Box -->
                <div class="bg-orange-50 border border-orange-200 rounded-2xl p-4 flex items-center gap-4">
                    <div id="tracking-status-spinner" class="animate-spin text-orange-500 text-2xl">
                        <i class="fa-solid fa-circle-notch"></i>
                    </div>
                    <div>
                        <h4 id="tracking-status-title" class="font-bold text-orange-800">ร้านค้ากำลังยืนยันออเดอร์</h4>
                        <p id="tracking-status-desc" class="text-xs text-orange-600 mt-0.5">ระบบกำลังส่งคำสั่งซื้อของคุณไปยังห้องครัว</p>
                    </div>
                </div>

                <!-- Driver Card Simulation (Shows when Step >= 3) -->
                <div id="driver-card" class="hidden bg-gray-50 rounded-2xl p-4 border border-gray-200 flex items-center justify-between">
                    <div class="flex items-center gap-3">
                        <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&q=80&w=150" alt="Driver" class="w-12 h-12 rounded-full object-cover border-2 border-orange-500">
                        <div>
                            <h5 class="font-bold text-gray-800 text-sm">พี่สมศักดิ์ (ไรเดอร์)</h5>
                            <p class="text-xs text-gray-500">ทะเบียน กข-9999 • Honda Wave</p>
                            <p class="text-xs text-amber-600 font-semibold mt-0.5"><i class="fa-solid fa-star text-amber-400"></i> 4.9 (500+ งาน)</p>
                        </div>
                    </div>
                    <a href="tel:0800000000" class="w-10 h-10 bg-green-500 text-white rounded-full flex items-center justify-center shadow hover:bg-green-600 transition">
                        <i class="fa-solid fa-phone"></i>
                    </a>
                </div>

                <!-- Order Details Summary -->
                <div class="border-t pt-4">
                    <h4 class="font-bold text-gray-700 mb-3 text-sm">รายการอาหารที่สั่ง</h4>
                    <div id="tracking-items-list" class="space-y-2 mb-4 text-sm">
                        <!-- Dynamic item list -->
                    </div>
                    <div class="flex justify-between font-bold text-gray-800 pt-3 border-t text-base">
                        <span>ราคารวมทั้งหมด:</span>
                        <span id="tracking-total-price" class="text-orange-600">฿0</span>
                    </div>
                </div>
            </div>
        </section>

        <!-- TAB 3: ORDER HISTORY VIEW -->
        <section id="tab-history" class="hidden max-w-4xl mx-auto space-y-4">
            <h2 class="text-2xl font-bold text-gray-800 mb-4 flex items-center gap-2">
                <i class="fa-solid fa-clock-rotate-left text-orange-500"></i>
                ประวัติการสั่งซื้อย้อนหลัง
            </h2>
            <div id="history-list" class="space-y-4">
                <!-- Dynamic History Cards loaded by JS -->
            </div>
        </section>

    </main>

    <!-- Mobile Bottom Navigation Bar -->
    <nav class="md:hidden fixed bottom-0 left-0 right-0 bg-white border-t border-gray-200 z-30 flex justify-around py-2 px-2 shadow-lg">
        <button onclick="switchTab('menu')" id="mob-nav-menu" class="flex flex-col items-center py-1 px-3 text-orange-600">
            <i class="fa-solid fa-utensils text-lg"></i>
            <span class="text-[10px] font-medium mt-1">เมนูหลัก</span>
        </button>
        <button onclick="switchTab('tracking')" id="mob-nav-tracking" class="flex flex-col items-center py-1 px-3 text-gray-400">
            <i class="fa-solid fa-motorcycle text-lg"></i>
            <span class="text-[10px] font-medium mt-1">ติดตาม</span>
        </button>
        <button onclick="switchTab('history')" id="mob-nav-history" class="flex flex-col items-center py-1 px-3 text-gray-400">
            <i class="fa-solid fa-clock-rotate-left text-lg"></i>
            <span class="text-[10px] font-medium mt-1">ประวัติ</span>
        </button>
    </nav>

    <!-- FOOD DETAIL MODAL -->
    <div id="food-modal" class="fixed inset-0 bg-black/60 z-50 flex items-center justify-center p-4 hidden backdrop-blur-sm">
        <div class="bg-white rounded-3xl max-w-md w-full overflow-hidden shadow-2xl transform transition-all">
            <div class="relative h-56 bg-gray-200">
                <img id="modal-img" src="" alt="" class="w-full h-full object-cover">
                <button onclick="closeFoodModal()" class="absolute top-3 right-3 w-9 h-9 bg-black/40 hover:bg-black/60 text-white rounded-full flex items-center justify-center backdrop-blur-md transition">
                    <i class="fa-solid fa-xmark"></i>
                </button>
            </div>
            <div class="p-5 space-y-4">
                <div>
                    <div class="flex justify-between items-start">
                        <h3 id="modal-title" class="text-xl font-bold text-gray-800">ชื่ออาหาร</h3>
                        <span id="modal-price" class="text-xl font-extrabold text-orange-600">฿0</span>
                    </div>
                    <p id="modal-desc" class="text-xs text-gray-500 mt-1">รายละเอียดและส่วนผสม</p>
                </div>

                <!-- Customization Options -->
                <div class="space-y-3 border-t border-b py-3 text-sm">
                    <!-- Spicy Level -->
                    <div id="spicy-option-container">
                        <label class="block font-semibold text-gray-700 mb-1">ระดับความเผ็ด</label>
                        <div class="grid grid-cols-3 gap-2 text-xs">
                            <button type="button" onclick="selectSpicy(this, 'เผ็ดน้อย')" class="spicy-btn py-1.5 px-2 border rounded-xl text-center border-orange-500 bg-orange-50 text-orange-700 font-medium">เผ็ดน้อย</button>
                            <button type="button" onclick="selectSpicy(this, 'เผ็ดปานกลาง')" class="spicy-btn py-1.5 px-2 border rounded-xl text-center border-gray-200 text-gray-600">เผ็ดปานกลาง</button>
                            <button type="button" onclick="selectSpicy(this, 'เผ็ดมาก')" class="spicy-btn py-1.5 px-2 border rounded-xl text-center border-gray-200 text-gray-600">เผ็ดมาก</button>
                        </div>
                    </div>

                    <!-- Special Instruction -->
                    <div>
                        <label class="block font-semibold text-gray-700 mb-1">รายละเอียดเพิ่มเติม</label>
                        <input type="text" id="modal-note" placeholder="เช่น ไม่ใส่ผัก, ขอซอสเพิ่ม" class="w-full text-xs p-2.5 border rounded-xl border-gray-200 focus:outline-none focus:border-orange-500">
                    </div>
                </div>

                <!-- Quantity & Add to Cart -->
                <div class="flex items-center justify-between pt-2">
                    <div class="flex items-center gap-3 border border-gray-200 rounded-full px-3 py-1">
                        <button onclick="updateModalQty(-1)" class="w-7 h-7 text-gray-500 hover:text-orange-600 font-bold text-lg flex items-center justify-center">-</button>
                        <span id="modal-qty" class="font-bold text-gray-800 w-4 text-center">1</span>
                        <button onclick="updateModalQty(1)" class="w-7 h-7 text-gray-500 hover:text-orange-600 font-bold text-lg flex items-center justify-center">+</button>
                    </div>

                    <button onclick="confirmAddToCart()" class="flex-grow ml-4 py-3 bg-orange-500 hover:bg-orange-600 text-white rounded-full font-bold text-sm shadow-md shadow-orange-500/30 transition flex items-center justify-center gap-2">
                        <i class="fa-solid fa-basket-shopping"></i>
                        <span>ใส่ตะกร้า • </span>
                        <span id="modal-total-btn-price">฿0</span>
                    </button>
                </div>
            </div>
        </div>
    </div>

    <!-- CART SLIDE OVER DRAWER -->
    <div id="cart-drawer" class="fixed inset-0 z-50 hidden">
        <div onclick="toggleCartDrawer(false)" class="absolute inset-0 bg-black/50 backdrop-blur-sm"></div>
        <div class="absolute inset-y-0 right-0 max-w-full flex pl-10">
            <div class="w-screen max-w-md bg-white shadow-2xl flex flex-col">
                <!-- Header -->
                <div class="p-4 border-b flex items-center justify-between bg-orange-50">
                    <div class="flex items-center gap-2">
                        <i class="fa-solid fa-basket-shopping text-orange-600 text-lg"></i>
                        <h2 class="font-bold text-lg text-gray-800">ตะกร้าของคุณ</h2>
                    </div>
                    <button onclick="toggleCartDrawer(false)" class="p-2 text-gray-400 hover:text-gray-600 text-lg">
                        <i class="fa-solid fa-xmark"></i>
                    </button>
                </div>

                <!-- Cart Items List -->
                <div id="cart-items-container" class="flex-1 overflow-y-auto p-4 space-y-4">
                    <!-- Dynamic Cart Items -->
                </div>

                <!-- Cart Footer Summary & Checkout -->
                <div id="cart-footer" class="p-4 border-t bg-gray-50 space-y-3">
                    <!-- Promo Code Input -->
                    <div class="flex gap-2">
                        <input type="text" id="promo-code-input" placeholder="ใส่โค้ดส่วนลด (เช่น AROY20)" class="flex-grow text-xs border rounded-xl px-3 py-2 border-gray-200 focus:outline-none focus:border-orange-500 uppercase">
                        <button onclick="applyPromoCode()" class="bg-gray-800 hover:bg-black text-white text-xs px-4 py-2 rounded-xl font-medium transition">ใช้โค้ด</button>
                    </div>

                    <div class="space-y-1.5 text-xs text-gray-600 pt-2 border-t">
                        <div class="flex justify-between">
                            <span>รวมค่าอาหาร:</span>
                            <span id="summary-subtotal" class="font-semibold text-gray-800">฿0</span>
                        </div>
                        <div class="flex justify-between">
                            <span>ค่าจัดส่ง:</span>
                            <span id="summary-shipping" class="font-semibold text-gray-800">฿30</span>
                        </div>
                        <div id="discount-row" class="flex justify-between text-green-600 hidden">
                            <span>ส่วนลดโปรโมชัน:</span>
                            <span id="summary-discount" class="font-semibold">-฿0</span>
                        </div>
                        <div class="flex justify-between text-base font-bold text-gray-900 pt-2 border-t">
                            <span>ยอดชำระทั้งหมด:</span>
                            <span id="summary-grandtotal" class="text-orange-600">฿0</span>
                        </div>
                    </div>

                    <button onclick="openCheckoutModal()" class="w-full py-3 bg-orange-500 hover:bg-orange-600 text-white font-bold rounded-xl shadow-lg shadow-orange-500/30 transition text-sm flex items-center justify-center gap-2">
                        <span>ดำเนินการสั่งซื้อ</span>
                        <i class="fa-solid fa-arrow-right"></i>
                    </button>
                </div>
            </div>
        </div>
    </div>

    <!-- CHECKOUT MODAL -->
    <div id="checkout-modal" class="fixed inset-0 bg-black/60 z-50 flex items-center justify-center p-4 hidden backdrop-blur-sm overflow-y-auto">
        <div class="bg-white rounded-3xl max-w-lg w-full p-6 shadow-2xl space-y-5 my-8">
            <div class="flex justify-between items-center border-b pb-3">
                <h3 class="text-xl font-bold text-gray-800 flex items-center gap-2">
                    <i class="fa-solid fa-file-invoice-dollar text-orange-500"></i>
                    ชำระเงินและระบุที่อยู่
                </h3>
                <button onclick="closeCheckoutModal()" class="text-gray-400 hover:text-gray-600">
                    <i class="fa-solid fa-xmark text-xl"></i>
                </button>
            </div>

            <!-- Form Fields -->
            <form id="checkout-form" onsubmit="handlePlaceOrder(event)" class="space-y-4 text-xs">
                <div>
                    <label class="block font-semibold text-gray-700 mb-1">ชื่อ-นามสกุล ผู้รับ *</label>
                    <input type="text" id="cust-name" required placeholder="เช่น สมชาย ใจดี" class="w-full p-2.5 border rounded-xl border-gray-200 focus:outline-none focus:border-orange-500 text-sm">
                </div>
                <div>
                    <label class="block font-semibold text-gray-700 mb-1">เบอร์โทรศัพท์ติดต่อ *</label>
                    <input type="tel" id="cust-phone" required placeholder="เช่น 0812345678" class="w-full p-2.5 border rounded-xl border-gray-200 focus:outline-none focus:border-orange-500 text-sm">
                </div>
                <div>
                    <label class="block font-semibold text-gray-700 mb-1">ที่อยู่จัดส่งอย่างละเอียด *</label>
                    <textarea id="cust-address" required rows="2" placeholder="บ้านเลขที่, ถนน, ซอย, จุดสังเกต" class="w-full p-2.5 border rounded-xl border-gray-200 focus:outline-none focus:border-orange-500 text-sm"></textarea>
                </div>

                <!-- Payment Method Selection -->
                <div>
                    <label class="block font-semibold text-gray-700 mb-2">เลือกวิธีชำระเงิน</label>
                    <div class="grid grid-cols-2 gap-3">
                        <label class="border rounded-2xl p-3 flex items-center gap-2 cursor-pointer hover:border-orange-500 transition has-[:checked]:border-orange-500 has-[:checked]:bg-orange-50">
                            <input type="radio" name="payment_type" value="promptpay" checked onchange="togglePaymentUI()" class="accent-orange-500">
                            <div>
                                <p class="font-bold text-gray-800 text-xs">พร้อมเพย์ / QR Code</p>
                                <p class="text-[10px] text-gray-500">สแกนจ่ายไม่มีค่าธรรมเนียม</p>
                            </div>
                        </label>
                        <label class="border rounded-2xl p-3 flex items-center gap-2 cursor-pointer hover:border-orange-500 transition has-[:checked]:border-orange-500 has-[:checked]:bg-orange-50">
                            <input type="radio" name="payment_type" value="cod" onchange="togglePaymentUI()" class="accent-orange-500">
                            <div>
                                <p class="font-bold text-gray-800 text-xs">เก็บเงินปลายทาง (COD)</p>
                                <p class="text-[10px] text-gray-500">จ่ายเงินสดกับไรเดอร์</p>
                            </div>
                        </label>
                    </div>
                </div>

                <!-- QR PromptPay Display -->
                <div id="qr-pay-box" class="bg-orange-50 rounded-2xl p-4 text-center border border-orange-200 space-y-2">
                    <p class="font-semibold text-orange-800 text-xs">สแกน QR Code เพื่อชำระเงิน</p>
                    <div class="bg-white p-3 inline-block rounded-xl shadow-sm border border-orange-100">
                        <!-- Dynamic PromptPay QR mockup -->
                        <img id="promptpay-qr" src="https://api.qrserver.com/v1/create-qr-code/?size=160x160&data=PROMPTPAY_MOCK_PAYMENT" alt="PromptPay QR" class="w-36 h-36 mx-auto">
                    </div>
                    <p class="text-[11px] text-gray-600 font-medium">ยอดชำระ: <span id="checkout-total-display" class="text-orange-600 font-bold">฿0</span></p>
                    <p class="text-[10px] text-gray-400">ชื่อบัญชี: บจก. อร่อยดี เอ็กซ์เพรส</p>
                </div>

                <button type="submit" class="w-full py-3.5 bg-orange-500 hover:bg-orange-600 text-white font-bold rounded-xl shadow-lg shadow-orange-500/30 transition text-sm flex items-center justify-center gap-2">
                    <i class="fa-solid fa-circle-check"></i>
                    <span>ยืนยันการสั่งซื้ออาหาร</span>
                </button>
            </form>
        </div>
    </div>

    <script>
        // Mock Data for Menu Items
        const foodMenu = [
            {
                id: 1,
                name: "กะเพราหมูกรอบ ไข่ดาว",
                category: "main",
                price: 75,
                rating: 4.9,
                spicy: true,
                image: "https://images.unsplash.com/photo-1589301760014-d929f3979dbc?auto=format&fit=crop&q=80&w=500",
                description: "หมูกรอบผัดกะเพรารสจัดจ้าน เสิร์ฟพร้อมข้าวสวยหอมมะลิและไข่ดาวกรอบนอกไข่แดงเยิ้ม"
            },
            {
                id: 2,
                name: "ข้าวผัดต้มยำกุ้งสด",
                category: "main",
                price: 85,
                rating: 4.8,
                spicy: true,
                image: "https://images.unsplash.com/photo-1559847844-5315695dadae?auto=format&fit=crop&q=80&w=500",
                description: "ข้าวผัดคลุกเครื่องต้มยำเข้มข้น กุ้งตัวโต สดใหม่ รสชาติเปรี้ยวเผ็ดเค็มกลมกล่อม"
            },
            {
                id: 3,
                name: "ส้มตำไทยไข่เค็ม",
                category: "somtum",
                price: 65,
                rating: 4.7,
                spicy: true,
                image: "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&q=80&w=500",
                description: "มะละกอกรอบ ตำพร้อมถั่วลิสง กุ้งแห้งตัวโต และไข่เค็มรสชาติมันนัว"
            },
            {
                id: 4,
                name: "ยำวุ้นเส้นหมูสับกุ้งสด",
                category: "somtum",
                price: 80,
                rating: 4.8,
                spicy: true,
                image: "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&q=80&w=500",
                description: "ยำวุ้นเส้นเหนียวนุ่ม ครบเครื่องหมูสับและกุ้งสด รสจัดจ้านครบรส"
            },
            {
                id: 5,
                name: "ชานมไต้หวันไข่มุก",
                category: "drinks",
                price: 50,
                rating: 4.9,
                spicy: false,
                image: "https://images.unsplash.com/photo-1558857563-b371033873b8?auto=format&fit=crop&q=80&w=500",
                description: "ชานมเข้มข้นกลิ่นหอมชาไต้หวันแท้ เสิร์ฟพร้อมไข่มุกหนึบหนับเคี้ยวเพลิน"
            },
            {
                id: 6,
                name: "ชาไทยเย็นโบราณ",
                category: "drinks",
                price: 45,
                rating: 4.6,
                spicy: false,
                image: "https://images.unsplash.com/photo-1517256064527-09c73fc73e38?auto=format&fit=crop&q=80&w=500",
                description: "ชาไทยรสชาติกลมกล่อม หอมหวานมัน เข้มข้นถึงใจ"
            },
            {
                id: 7,
                name: "นักเก็ตไก่ทอดกรอบ (6 ชิ้น)",
                category: "snack",
                price: 59,
                rating: 4.5,
                spicy: false,
                image: "https://images.unsplash.com/photo-1562967914-608f82629710?auto=format&fit=crop&q=80&w=500",
                description: "นักเก็ตไก่เนื้อแน่น ทอดกรอบสีเหลืองทอง เสิร์ฟคู่กับซอสมะเขือเทศและบาร์บีคิว"
            },
            {
                id: 8,
                name: "เฟรนช์ฟรายส์ซอสชีส",
                category: "snack",
                price: 69,
                rating: 4.7,
                spicy: false,
                image: "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?auto=format&fit=crop&q=80&w=500",
                description: "เฟรนช์ฟรายส์ทอดใหม่ร้อนๆ ราดซอสชีสเข้มข้น หอมมันสะใจ"
            }
        ];

        const categories = [
            { id: "all", name: "ทั้งหมด", icon: "fa-border-all" },
            { id: "main", name: "อาหารจานเดียว", icon: "fa-bowl-rice" },
            { id: "somtum", name: "ส้มตำ-ยำ", icon: "fa-pepper-hot" },
            { id: "drinks", name: "เครื่องดื่ม", icon: "fa-glass-water" },
            { id: "snack", name: "ของทานเล่น", icon: "fa-cookie-bite" }
        ];

        // Global State
        let currentCategory = "all";
        let onlySpicy = false;
        let cart = [];
        let appliedDiscount = 0;
        let selectedFood = null;
        let modalQty = 1;
        let selectedSpicyLevel = "เผ็ดปานกลาง";
        
        // Active Order Simulation State
        let activeOrder = null;
        let trackingTimer = null;
        let orderHistory = [];

        // INITIALIZATION
        window.onload = function() {
            renderCategories();
            renderFoodGrid(foodMenu);
            loadSampleHistory();
        };

        // Render Categories Bar
        function renderCategories() {
            const container = document.getElementById('category-container');
            container.innerHTML = categories.map(cat => `
                <button onclick="selectCategory('${cat.id}')" 
                        class="cat-btn px-4 py-2 rounded-full text-xs font-semibold whitespace-nowrap transition flex items-center gap-2 ${cat.id === currentCategory ? 'bg-orange-500 text-white shadow-md shadow-orange-500/20' : 'bg-white border border-gray-200 text-gray-600 hover:bg-orange-50'}">
                    <i class="fa-solid ${cat.icon}"></i>
                    <span>${cat.name}</span>
                </button>
            `).join('');
        }

        function selectCategory(catId) {
            currentCategory = catId;
            renderCategories();
            filterMenuItems();
        }

        // Render Food Grid with Filters
        function filterMenuItems() {
            const searchTerm = document.getElementById('search-input').value.toLowerCase();
            const sortOption = document.getElementById('sort-select').value;

            let filtered = foodMenu.filter(item => {
                const matchCategory = currentCategory === 'all' || item.category === currentCategory;
                const matchSearch = item.name.toLowerCase().includes(searchTerm) || item.description.toLowerCase().includes(searchTerm);
                const matchSpicy = !onlySpicy || item.spicy;
                return matchCategory && matchSearch && matchSpicy;
            });

            // Sorting
            if (sortOption === 'price-low') filtered.sort((a, b) => a.price - b.price);
            else if (sortOption === 'price-high') filtered.sort((a, b) => b.price - a.price);
            else if (sortOption === 'rating') filtered.sort((a, b) => b.rating - a.rating);

            renderFoodGrid(filtered);
        }

        function toggleSpicyFilter() {
            onlySpicy = !onlySpicy;
            const btn = document.getElementById('btn-spicy-filter');
            if (onlySpicy) {
                btn.classList.add('bg-red-500', 'text-white', 'border-red-500');
                btn.classList.remove('bg-white', 'text-gray-600');
            } else {
                btn.classList.remove('bg-red-500', 'text-white', 'border-red-500');
                btn.classList.add('bg-white', 'text-gray-600');
            }
            filterMenuItems();
        }

        function renderFoodGrid(items) {
            const grid = document.getElementById('food-grid');
            const emptyMsg = document.getElementById('empty-search');

            if (items.length === 0) {
                grid.innerHTML = '';
                emptyMsg.classList.remove('hidden');
                return;
            }

            emptyMsg.classList.add('hidden');
            grid.innerHTML = items.map(item => `
                <div class="bg-white rounded-3xl overflow-hidden border border-gray-100 shadow-sm hover:shadow-xl transition duration-300 flex flex-col justify-between group">
                    <div>
                        <div class="relative h-48 overflow-hidden">
                            <img src="${item.image}" alt="${item.name}" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
                            <div class="absolute top-3 right-3 bg-white/90 backdrop-blur-md px-2.5 py-1 rounded-full text-xs font-bold text-gray-700 flex items-center gap-1 shadow">
                                <i class="fa-solid fa-star text-amber-400"></i> ${item.rating}
                            </div>
                            ${item.spicy ? '<span class="absolute top-3 left-3 bg-red-500 text-white text-[10px] font-bold px-2 py-0.5 rounded-full shadow"><i class="fa-solid fa-pepper-hot"></i> เผ็ด</span>' : ''}
                        </div>
                        <div class="p-4 space-y-2">
                            <h3 class="font-bold text-gray-800 text-base line-clamp-1">${item.name}</h3>
                            <p class="text-xs text-gray-500 line-clamp-2 leading-relaxed">${item.description}</p>
                        </div>
                    </div>
                    <div class="p-4 pt-0 flex items-center justify-between mt-2">
                        <span class="text-lg font-extrabold text-orange-600">฿${item.price}</span>
                        <button onclick="openFoodModal(${item.id})" class="px-4 py-2 bg-orange-50 hover:bg-orange-500 hover:text-white text-orange-600 font-bold text-xs rounded-full transition flex items-center gap-1 shadow-sm">
                            <i class="fa-solid fa-plus"></i> เลือก
                        </button>
                    </div>
                </div>
            `).join('');
        }

        // FOOD MODAL HANDLERS
        function openFoodModal(foodId) {
            selectedFood = foodMenu.find(f => f.id === foodId);
            modalQty = 1;
            selectedSpicyLevel = "เผ็ดปานกลาง";

            document.getElementById('modal-img').src = selectedFood.image;
            document.getElementById('modal-title').innerText = selectedFood.name;
            document.getElementById('modal-desc').innerText = selectedFood.description;
            document.getElementById('modal-price').innerText = `฿${selectedFood.price}`;
            document.getElementById('modal-qty').innerText = modalQty;
            document.getElementById('modal-note').value = '';

            const spicyContainer = document.getElementById('spicy-option-container');
            if (selectedFood.spicy) {
                spicyContainer.classList.remove('hidden');
            } else {
                spicyContainer.classList.add('hidden');
            }

            updateModalPrice();
            document.getElementById('food-modal').classList.remove('hidden');
        }

        function closeFoodModal() {
            document.getElementById('food-modal').classList.add('hidden');
        }

        function updateModalQty(change) {
            modalQty = Math.max(1, modalQty + change);
            document.getElementById('modal-qty').innerText = modalQty;
            updateModalPrice();
        }

        function updateModalPrice() {
            const total = selectedFood.price * modalQty;
            document.getElementById('modal-total-btn-price').innerText = `฿${total}`;
        }

        function selectSpicy(btn, level) {
            selectedSpicyLevel = level;
            document.querySelectorAll('.spicy-btn').forEach(b => {
                b.classList.remove('border-orange-500', 'bg-orange-50', 'text-orange-700', 'font-medium');
                b.classList.add('border-gray-200', 'text-gray-600');
            });
            btn.classList.add('border-orange-500', 'bg-orange-50', 'text-orange-700', 'font-medium');
            btn.classList.remove('border-gray-200', 'text-gray-600');
        }

        function confirmAddToCart() {
            const note = document.getElementById('modal-note').value.trim();
            const cartItem = {
                cartId: Date.now(),
                foodId: selectedFood.id,
                name: selectedFood.name,
                price: selectedFood.price,
                image: selectedFood.image,
                qty: modalQty,
                spicy: selectedFood.spicy ? selectedSpicyLevel : null,
                note: note
            };

            cart.push(cartItem);
            updateCartUI();
            closeFoodModal();
            toggleCartDrawer(true);
        }

        // CART DRAWER LOGIC
        function toggleCartDrawer(show) {
            const drawer = document.getElementById('cart-drawer');
            if (show) drawer.classList.remove('hidden');
            else drawer.classList.add('hidden');
        }

        function updateCartUI() {
            const container = document.getElementById('cart-items-container');
            const badge = document.getElementById('cart-badge');
            
            // Badge total item count
            const totalItemsCount = cart.reduce((sum, item) => sum + item.qty, 0);
            badge.innerText = totalItemsCount;

            if (cart.length === 0) {
                container.innerHTML = `
                    <div class="text-center py-12 text-gray-400">
                        <i class="fa-solid fa-basket-shopping text-5xl mb-3 opacity-40"></i>
                        <p class="text-sm font-medium">ยังไม่มีสินค้าในตะกร้า</p>
                    </div>
                `;
                updateCartTotals();
                return;
            }

            container.innerHTML = cart.map(item => `
                <div class="flex items-center gap-3 p-3 bg-gray-50 rounded-2xl border border-gray-100">
                    <img src="${item.image}" alt="" class="w-16 h-16 rounded-xl object-cover">
                    <div class="flex-1">
                        <h4 class="font-bold text-gray-800 text-xs">${item.name}</h4>
                        <div class="text-[10px] text-gray-500 mt-0.5 space-y-0.5">
                            ${item.spicy ? `<p class="text-orange-600 font-medium"><i class="fa-solid fa-pepper-hot"></i> ${item.spicy}</p>` : ''}
                            ${item.note ? `<p class="italic text-gray-400">"${item.note}"</p>` : ''}
                        </div>
                        <span class="font-bold text-orange-600 text-xs mt-1 block">฿${item.price * item.qty}</span>
                    </div>
                    <div class="flex flex-col items-end gap-2">
                        <button onclick="removeCartItem(${item.cartId})" class="text-gray-400 hover:text-red-500 text-xs">
                            <i class="fa-solid fa-trash-can"></i>
                        </button>
                        <div class="flex items-center gap-2 border border-gray-200 rounded-lg bg-white px-2 py-0.5 text-xs">
                            <button onclick="changeCartQty(${item.cartId}, -1)" class="text-gray-500 hover:text-orange-600 font-bold">-</button>
                            <span class="font-bold text-gray-700 w-3 text-center">${item.qty}</span>
                            <button onclick="changeCartQty(${item.cartId}, 1)" class="text-gray-500 hover:text-orange-600 font-bold">+</button>
                        </div>
                    </div>
                </div>
            `).join('');

            updateCartTotals();
        }

        function changeCartQty(cartId, change) {
            const item = cart.find(i => i.cartId === cartId);
            if (item) {
                item.qty += change;
                if (item.qty <= 0) {
                    cart = cart.filter(i => i.cartId !== cartId);
                }
            }
            updateCartUI();
        }

        function removeCartItem(cartId) {
            cart = cart.filter(i => i.cartId !== cartId);
            updateCartUI();
        }

        function applyPromoCode() {
            const code = document.getElementById('promo-code-input').value.trim().toUpperCase();
            if (code === 'AROY20') {
                appliedDiscount = 20;
                document.getElementById('discount-row').classList.remove('hidden');
                document.getElementById('summary-discount').innerText = `-฿${appliedDiscount}`;
            } else {
                appliedDiscount = 0;
                document.getElementById('discount-row').classList.add('hidden');
            }
            updateCartTotals();
        }

        function updateCartTotals() {
            const subtotal = cart.reduce((sum, item) => sum + (item.price * item.qty), 0);
            const shipping = cart.length > 0 ? (subtotal >= 250 ? 0 : 30) : 0;
            const grandTotal = Math.max(0, subtotal + shipping - appliedDiscount);

            document.getElementById('summary-subtotal').innerText = `฿${subtotal}`;
            document.getElementById('summary-shipping').innerText = shipping === 0 && subtotal > 0 ? 'ฟรี' : `฿${shipping}`;
            document.getElementById('summary-grandtotal').innerText = `฿${grandTotal}`;
            document.getElementById('checkout-total-display').innerText = `฿${grandTotal}`;
        }

        // CHECKOUT & PAYMENT HANDLERS
        function openCheckoutModal() {
            if (cart.length === 0) return;
            toggleCartDrawer(false);
            document.getElementById('checkout-modal').classList.remove('hidden');
        }

        function closeCheckoutModal() {
            document.getElementById('checkout-modal').classList.add('hidden');
        }

        function togglePaymentUI() {
            const paymentType = document.querySelector('input[name="payment_type"]:checked').value;
            const qrBox = document.getElementById('qr-pay-box');
            if (paymentType === 'promptpay') {
                qrBox.classList.remove('hidden');
            } else {
                qrBox.classList.add('hidden');
            }
        }

        function handlePlaceOrder(event) {
            event.preventDefault();

            const name = document.getElementById('cust-name').value;
            const phone = document.getElementById('cust-phone').value;
            const address = document.getElementById('cust-address').value;
            const paymentType = document.querySelector('input[name="payment_type"]:checked').value;

            const subtotal = cart.reduce((sum, item) => sum + (item.price * item.qty), 0);
            const shipping = subtotal >= 250 ? 0 : 30;
            const grandTotal = Math.max(0, subtotal + shipping - appliedDiscount);

            // Create new Order object
            const newOrder = {
                id: 'ORD-' + Math.floor(100000 + Math.random() * 900000),
                customer: { name, phone, address },
                items: [...cart],
                paymentType: paymentType,
                total: grandTotal,
                statusStep: 1, // 1: Received, 2: Cooking, 3: Delivering, 4: Complete
                createdAt: new Date().toLocaleTimeString('th-TH', { hour: '2-digit', minute: '2-digit' })
            };

            activeOrder = newOrder;
            cart = [];
            appliedDiscount = 0;
            updateCartUI();

            closeCheckoutModal();
            switchTab('tracking');
            startOrderSimulation();
        }

        // LIVE TRACKING SIMULATION
        function startOrderSimulation() {
            if (trackingTimer) clearInterval(trackingTimer);

            renderActiveOrderView();

            // Automatic status step progression simulation
            trackingTimer = setInterval(() => {
                if (activeOrder && activeOrder.statusStep < 4) {
                    activeOrder.statusStep += 1;
                    renderActiveOrderView();

                    if (activeOrder.statusStep === 4) {
                        // Order completed, move to history
                        clearInterval(trackingTimer);
                        orderHistory.unshift({ ...activeOrder, completedAt: 'เมื่อสักครู่' });
                        renderHistoryView();
                    }
                }
            }, 8000); // Step updates every 8 seconds
        }

        function renderActiveOrderView() {
            const noOrderBox = document.getElementById('no-active-order');
            const activeBox = document.getElementById('active-order-container');

            if (!activeOrder) {
                noOrderBox.classList.remove('hidden');
                activeBox.classList.add('hidden');
                return;
            }

            noOrderBox.classList.add('hidden');
            activeBox.classList.remove('hidden');

            document.getElementById('tracking-order-id').innerText = `#${activeOrder.id}`;
            document.getElementById('tracking-total-price').innerText = `฿${activeOrder.total}`;

            // Update Progress Bar
            const stepPercent = ((activeOrder.statusStep - 1) / 3) * 100;
            document.getElementById('progress-bar-fill').style.width = `${stepPercent}%`;

            // Update Step Nodes
            document.querySelectorAll('.step-node').forEach(node => {
                const step = parseInt(node.getAttribute('data-step'));
                const iconBox = node.querySelector('.step-icon');
                const label = node.querySelector('span');

                if (step <= activeOrder.statusStep) {
                    iconBox.className = "step-icon w-10 h-10 rounded-full bg-orange-500 text-white flex items-center justify-center font-bold text-sm shadow-md transition-all";
                    label.className = "text-xs font-bold text-orange-600 mt-2";
                } else {
                    iconBox.className = "step-icon w-10 h-10 rounded-full bg-gray-200 text-gray-400 flex items-center justify-center font-bold text-sm transition-all";
                    label.className = "text-xs font-semibold text-gray-400 mt-2";
                }
            });

            // Update Status Messages
            const title = document.getElementById('tracking-status-title');
            const desc = document.getElementById('tracking-status-desc');
            const driverCard = document.getElementById('driver-card');
            const spinner = document.getElementById('tracking-status-spinner');

            if (activeOrder.statusStep === 1) {
                title.innerText = "ร้านค้าได้รับออเดอร์แล้ว";
                desc.innerText = "กำลังรับออเดอร์เข้าสู่ระบบครัว...";
                driverCard.classList.add('hidden');
            } else if (activeOrder.statusStep === 2) {
                title.innerText = "กำลังปรุงอาหารให้คุณ";
                desc.innerText = "เชฟกำลังจัดเตรียมและปรุงอาหารอย่างพิถีพิถัน";
                driverCard.classList.add('hidden');
            } else if (activeOrder.statusStep === 3) {
                title.innerText = "ไรเดอร์กำลังจัดส่งอาหาร";
                desc.innerText = "อาหารของคุณกำลังถูกส่งตรงถึงหน้าบ้าน";
                driverCard.classList.remove('hidden');
            } else if (activeOrder.statusStep === 4) {
                title.innerText = "จัดส่งสำเร็จเรียบร้อย!";
                desc.innerText = "ขอให้คุณอิ่มอร่อยกับมื้อนี้ ขอบคุณที่ใช้บริการ AroyDee";
                driverCard.classList.remove('hidden');
                spinner.innerHTML = '<i class="fa-solid fa-circle-check text-green-500"></i>';
                spinner.classList.remove('animate-spin');
            }

            // Render Items Summary
            document.getElementById('tracking-items-list').innerHTML = activeOrder.items.map(i => `
                <div class="flex justify-between items-center text-xs text-gray-600">
                    <span>${i.name} x ${i.qty} ${i.spicy ? `(${i.spicy})` : ''}</span>
                    <span class="font-semibold text-gray-800">฿${i.price * i.qty}</span>
                </div>
            `).join('');
        }

        // HISTORY VIEW & TAB NAVIGATION
        function loadSampleHistory() {
            orderHistory = [
                {
                    id: 'ORD-892301',
                    total: 215,
                    createdAt: 'เมื่อวานนี้, 12:30 น.',
                    items: [
                        { name: 'กะเพราหมูกรอบ ไข่ดาว', qty: 2, price: 75 },
                        { name: 'ชาไทยเย็นโบราณ', qty: 1, price: 45 }
                    ]
                }
            ];
            renderHistoryView();
        }

        function renderHistoryView() {
            const list = document.getElementById('history-list');
            if (orderHistory.length === 0) {
                list.innerHTML = `<p class="text-center text-gray-400 py-8">ไม่มีประวัติการสั่งซื้อ</p>`;
                return;
            }

            list.innerHTML = orderHistory.map(ord => `
                <div class="bg-white rounded-2xl p-5 border border-gray-100 shadow-sm space-y-3">
                    <div class="flex justify-between items-center border-b pb-2">
                        <div>
                            <span class="font-bold text-gray-800 text-sm">#${ord.id}</span>
                            <span class="text-xs text-gray-400 ml-2">${ord.createdAt}</span>
                        </div>
                        <span class="bg-green-100 text-green-700 text-[10px] font-bold px-2.5 py-0.5 rounded-full">สำเร็จแล้ว</span>
                    </div>
                    <div class="space-y-1">
                        ${ord.items.map(i => `
                            <div class="flex justify-between text-xs text-gray-600">
                                <span>${i.name} x ${i.qty}</span>
                                <span class="font-medium text-gray-800">฿${i.price * i.qty}</span>
                            </div>
                        `).join('')}
                    </div>
                    <div class="flex justify-between items-center pt-2 border-t text-sm font-bold">
                        <span>ราคารวม:</span>
                        <span class="text-orange-600">฿${ord.total}</span>
                    </div>
                </div>
            `).join('');
        }

        function switchTab(tab) {
            document.getElementById('tab-menu').classList.add('hidden');
            document.getElementById('tab-tracking').classList.add('hidden');
            document.getElementById('tab-history').classList.add('hidden');

            // Reset desktop nav buttons style
            document.querySelectorAll('.nav-btn').forEach(btn => {
                btn.classList.remove('text-orange-600', 'bg-orange-50');
                btn.classList.add('text-gray-600');
            });

            // Reset mobile nav buttons style
            ['mob-nav-menu', 'mob-nav-tracking', 'mob-nav-history'].forEach(id => {
                document.getElementById(id).className = "flex flex-col items-center py-1 px-3 text-gray-400";
            });

            if (tab === 'menu') {
                document.getElementById('tab-menu').classList.remove('hidden');
                document.getElementById('nav-menu').classList.add('text-orange-600', 'bg-orange-50');
                document.getElementById('mob-nav-menu').className = "flex flex-col items-center py-1 px-3 text-orange-600";
            } else if (tab === 'tracking') {
                document.getElementById('tab-tracking').classList.remove('hidden');
                document.getElementById('nav-tracking').classList.add('text-orange-600', 'bg-orange-50');
                document.getElementById('mob-nav-tracking').className = "flex flex-col items-center py-1 px-3 text-orange-600";
            } else if (tab === 'history') {
                document.getElementById('tab-history').classList.remove('hidden');
                document.getElementById('nav-history').classList.add('text-orange-600', 'bg-orange-50');
                document.getElementById('mob-nav-history').className = "flex flex-col items-center py-1 px-3 text-orange-600";
            }
        }
    </script>
</body>
</html>
