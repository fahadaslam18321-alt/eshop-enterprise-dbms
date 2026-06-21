import gradio as gr
import pandas as pd
from datetime import datetime
import random

# ─────────────────────────────────────────────
#  IN-MEMORY DATABASE  (mirrors the SQL inserts)
# ─────────────────────────────────────────────

categories = pd.DataFrame([
    (1,'Laptops','High performance machines for BSCS students','Active'),
    (2,'Smartphones','Latest mobile technology and iPhones','Active'),
    (3,'Audio','Noise canceling headphones and earbuds','Active'),
    (4,'Tablets','iPads and Android tablets','Active'),
    (5,'Accessories','Cables, chargers and covers','Active'),
    (6,'Cameras','DSLR and mirrorless cameras','Active'),
    (7,'Gaming','Gaming laptops and controllers','Active'),
], columns=['CategoryID','CategoryName','Description','Status'])

users = pd.DataFrame([
    (1,'Fahad','Aslam','fahad@gmail.edu','03001234567','Township 1C2','Lahore','Pakistan','Admin','Active','2026-01-01'),
    (2,'Ali','Khan','ali.customer@gmail.com','03219876543','DHA Phase 5','Karachi','Pakistan','Customer','Active','2026-01-05'),
    (3,'Zain','Ahmed','zain.vendor@shop.pk','03451122334','Blue Area','Islamabad','Pakistan','Vendor','Active','2026-01-10'),
    (4,'Sara','Malik','sara.malik@gmail.com','03011234568','Gulberg III','Lahore','Pakistan','Customer','Active','2026-01-12'),
    (5,'Hamza','Butt','hamza.butt@gmail.com','03211234569','Bahria Town','Rawalpindi','Pakistan','Customer','Active','2026-01-15'),
    (6,'Ayesha','Siddiqui','ayesha@gmail.com','03031234570','Clifton Block 4','Karachi','Pakistan','Customer','Active','2026-01-18'),
    (7,'Usman','Tariq','usman.vendor@shop.pk','03451234571','F-7 Markaz','Islamabad','Pakistan','Vendor','Active','2026-01-20'),
    (8,'Hina','Qureshi','hina.q@gmail.com','03211234572','Model Town','Lahore','Pakistan','Customer','Active','2026-01-22'),
    (9,'Bilal','Chaudhry','bilal.ch@gmail.com','03001234573','Phase 6 DHA','Karachi','Pakistan','Customer','Active','2026-01-25'),
    (10,'Nadia','Shah','nadia.shah@gmail.com','03131234574','G-11 Markaz','Islamabad','Pakistan','Customer','Active','2026-02-01'),
    (11,'Omar','Farooq','omar.farooq@gmail.com','03211234575','Johar Town','Lahore','Pakistan','Customer','Active','2026-02-05'),
    (12,'Sana','Iqbal','sana.iqbal@gmail.com','03001234576','North Nazimabad','Karachi','Pakistan','Customer','Active','2026-02-10'),
    (13,'Kamran','Javed','kamran.j@gmail.com','03451234577','E-11 Sector','Islamabad','Pakistan','Customer','Active','2026-02-15'),
    (14,'Faiza','Riaz','faiza.riaz@gmail.com','03211234578','Wapda Town','Lahore','Pakistan','Customer','Active','2026-02-18'),
    (15,'Tariq','Mehmood','tariq.m@gmail.com','03001234579','PECHS Block 2','Karachi','Pakistan','Customer','Active','2026-02-20'),
], columns=['UserID','FirstName','LastName','Email','PhoneNumber','Address','City','Country','Role','Status','RegistrationDate'])

products = pd.DataFrame([
    (1,'HP EliteBook 840 G8','Core i7, 16GB RAM',125000,115000,10,1,'Active','hp_g8.jpg',4.5),
    (2,'iPhone 15 Pro','256GB Titanium',350000,345000,5,2,'Active','iphone15.jpg',4.8),
    (3,'Sony WH-1000XM5','Wireless Noise Canceling',85000,80000,15,3,'Active','sony_xm5.jpg',4.7),
    (4,'Dell XPS 15','Core i9, 32GB RAM, 4K Display',220000,210000,8,1,'Active','dell_xps.jpg',4.6),
    (5,'Samsung Galaxy S24','256GB Phantom Black',180000,175000,12,2,'Active','galaxy_s24.jpg',4.5),
    (6,'iPad Pro M2','128GB WiFi Space Gray',160000,155000,7,4,'Active','ipad_pro.jpg',4.7),
    (7,'JBL Flip 6','Portable Bluetooth Speaker',25000,22000,30,3,'Active','jbl_flip6.jpg',4.3),
    (8,'Lenovo ThinkPad X1','Core i7, 16GB RAM, Business Laptop',175000,165000,6,1,'Active','thinkpad.jpg',4.4),
    (9,'OnePlus 12','256GB Silky Black',120000,115000,10,2,'Active','oneplus12.jpg',4.3),
    (10,'Canon EOS R50','Mirrorless Camera 24MP',195000,185000,4,6,'Active','canon_r50.jpg',4.6),
    (11,'PS5 Controller','DualSense Wireless White',18000,16000,25,7,'Active','ps5_ctrl.jpg',4.8),
    (12,'Samsung Tab S9','256GB WiFi',145000,138000,9,4,'Active','tab_s9.jpg',4.5),
    (13,'Apple AirPods Pro 2','Active Noise Cancellation',65000,60000,20,3,'Active','airpods.jpg',4.7),
    (14,'USB-C Hub 7-in-1','HDMI, USB3.0, SD Card',8500,7500,50,5,'Active','usb_hub.jpg',4.2),
    (15,'Logitech MX Master 3','Wireless Ergonomic Mouse',15000,13500,35,5,'Active','mx_master.jpg',4.6),
], columns=['ProductID','ProductName','Description','Price','DiscountPrice','Quantity','CategoryID','Status','ImageURL','Rating'])

discounts = pd.DataFrame([
    (1,1,'SAVE10',10,12500,'2026-03-01','2026-12-31',100,50000,'Active'),
    (2,2,'EID-OFFER',5,17500,'2026-03-20','2026-04-20',50,100000,'Active'),
    (3,4,'DELL15',15,33000,'2026-04-01','2026-06-30',30,150000,'Active'),
    (4,5,'SAMSUNG10',10,18000,'2026-04-01','2026-05-31',40,80000,'Active'),
    (5,6,'IPAD20',20,32000,'2026-03-15','2026-07-15',20,100000,'Active'),
    (6,10,'CANON5',5,9750,'2026-04-01','2026-09-30',15,150000,'Active'),
    (7,13,'AIRPODS15',15,9750,'2026-03-01','2026-12-31',60,40000,'Active'),
    (8,15,'MOUSE20',20,3000,'2026-04-01','2026-06-30',80,10000,'Active'),
], columns=['DiscountID','ProductID','DiscountCode','DiscountPercentage','DiscountAmount','ValidFrom','ValidUpto','UsageLimit','MinimumOrderAmount','Status'])

orders = pd.DataFrame([
    (1,2,112500,1,'Delivered','DHA Phase 5, Karachi','Deliver after 5 PM','2026-03-01 10:00:00'),
    (2,4,345000,2,'Shipped','Gulberg III, Lahore','Handle with care','2026-03-05 11:30:00'),
    (3,5,165000,3,'Processing','Bahria Town, Rawalpindi',None,'2026-03-10 09:15:00'),
    (4,6,175000,4,'Pending','Clifton Block 4, Karachi','Call before delivery','2026-03-12 14:00:00'),
    (5,8,80000,None,'Delivered','Model Town, Lahore',None,'2026-03-15 16:00:00'),
    (6,9,115000,None,'Shipped','Phase 6 DHA, Karachi','Leave at gate','2026-03-18 08:45:00'),
    (7,10,155000,5,'Delivered','G-11 Markaz, Islamabad',None,'2026-03-20 12:00:00'),
    (8,11,22000,None,'Cancelled','Johar Town, Lahore','Changed my mind','2026-03-22 17:00:00'),
    (9,12,60000,7,'Processing','North Nazimabad, Karachi',None,'2026-03-25 10:30:00'),
    (10,13,185000,6,'Pending','E-11 Sector, Islamabad','Urgent delivery','2026-03-28 09:00:00'),
    (11,14,13500,8,'Delivered','Wapda Town, Lahore',None,'2026-04-01 11:00:00'),
    (12,2,18000,None,'Delivered','DHA Phase 5, Karachi',None,'2026-04-02 15:00:00'),
    (13,5,65000,7,'Shipped','Bahria Town, Rawalpindi',None,'2026-04-05 14:30:00'),
    (14,6,8500,None,'Processing','Clifton Block 4, Karachi',None,'2026-04-08 10:00:00'),
    (15,8,120000,None,'Pending','Model Town, Lahore','Gift wrap please','2026-04-10 16:00:00'),
], columns=['OrderID','UserID','TotalAmount','DiscountID','Status','ShippingAddress','OrderNotes','OrderDate'])

order_details = pd.DataFrame([
    (1,1,1,1,125000,112500,500,12500),
    (2,2,2,1,350000,345000,1000,5000),
    (3,3,4,1,220000,165000,800,55000),
    (4,4,5,1,180000,175000,600,5000),
    (5,5,3,1,85000,80000,300,5000),
    (6,6,9,1,120000,115000,400,5000),
    (7,7,6,1,160000,155000,500,5000),
    (8,8,7,2,25000,22000,200,3000),
    (9,9,13,1,65000,60000,250,5000),
    (10,10,10,1,195000,185000,750,10000),
    (11,11,15,1,15000,13500,100,1500),
    (12,12,11,1,18000,16000,150,2000),
    (13,13,13,1,65000,60000,250,5000),
    (14,14,14,1,8500,8500,50,0),
    (15,15,9,1,120000,115000,400,5000),
], columns=['OrderDetailID','OrderID','ProductID','Quantity','UnitPrice','TotalPrice','TaxAmount','DiscountAmount'])

payments = pd.DataFrame([
    (1,1,112500,'Bank Transfer','JazzCash','Completed','TXN-001-112233','2026-03-01'),
    (2,2,345000,'Credit Card','HBL','Completed','TXN-002-223344','2026-03-05'),
    (3,3,165000,'Debit Card','Meezan Bank','Completed','TXN-003-334455','2026-03-10'),
    (4,4,175000,'Bank Transfer','EasyPaisa','Pending','TXN-004-445566','2026-03-12'),
    (5,5,80000,'COD',None,'Completed','TXN-005-556677','2026-03-15'),
    (6,6,115000,'Credit Card','UBL','Completed','TXN-006-667788','2026-03-18'),
    (7,7,155000,'Bank Transfer','JazzCash','Completed','TXN-007-778899','2026-03-20'),
    (8,8,22000,'COD',None,'Refunded','TXN-008-889900','2026-03-22'),
    (9,9,60000,'Debit Card','Allied Bank','Completed','TXN-009-990011','2026-03-25'),
    (10,10,185000,'Bank Transfer','EasyPaisa','Pending','TXN-010-001122','2026-03-28'),
    (11,11,13500,'Credit Card','MCB','Completed','TXN-011-112244','2026-04-01'),
    (12,12,18000,'COD',None,'Completed','TXN-012-223355','2026-04-02'),
    (13,13,60000,'Bank Transfer','JazzCash','Completed','TXN-013-334466','2026-04-05'),
    (14,14,8500,'Debit Card','HBL','Completed','TXN-014-445577','2026-04-08'),
    (15,15,120000,'Credit Card','UBL','Pending','TXN-015-556688','2026-04-10'),
], columns=['PaymentID','OrderID','Amount','PaymentMethod','Provider','Status','TransactionID','PaymentDate'])

shipping = pd.DataFrame([
    (1,1,'DHA Phase 5, Karachi','Karachi','Pakistan','75500','Express','TCS','TCS-001-112233',2.5,'Delivered'),
    (2,2,'Gulberg III, Lahore','Lahore','Pakistan','54000','Overnight','Leopard','LEO-002-223344',0.5,'In Transit'),
    (3,3,'Bahria Town, Rawalpindi','Rawalpindi','Pakistan','46000','Standard','TCS','TCS-003-334455',3.0,'Out for Delivery'),
    (4,5,'Model Town, Lahore','Lahore','Pakistan','54700','Express','Leopard','LEO-005-556677',0.4,'Delivered'),
    (5,6,'Phase 6 DHA, Karachi','Karachi','Pakistan','75600','Standard','M&P','MNP-006-667788',0.3,'In Transit'),
    (6,7,'G-11 Markaz, Islamabad','Islamabad','Pakistan','44000','Express','TCS','TCS-007-778899',1.2,'Delivered'),
    (7,9,'North Nazimabad, Karachi','Karachi','Pakistan','75250','Standard','Leopard','LEO-009-990011',0.3,'In Transit'),
    (8,11,'Wapda Town, Lahore','Lahore','Pakistan','54770','Standard','M&P','MNP-011-112244',0.5,'Delivered'),
    (9,12,'DHA Phase 5, Karachi','Karachi','Pakistan','75500','Express','TCS','TCS-012-223355',0.8,'Delivered'),
    (10,13,'Bahria Town, Rawalpindi','Rawalpindi','Pakistan','46000','Overnight','Leopard','LEO-013-334466',0.3,'In Transit'),
    (11,14,'Clifton Block 4, Karachi','Karachi','Pakistan','75600','Standard','TCS','TCS-014-445577',0.2,'Delivered'),
    (12,15,'Model Town, Lahore','Lahore','Pakistan','54700','Express','M&P','MNP-015-556688',0.4,'Pending'),
], columns=['ShippingID','OrderID','ShippingAddress','City','Country','PostalCode','ShippingMethod','CourierName','TrackingNumber','Weight','Status'])

reviews = pd.DataFrame([
    (1,1,2,5,'Perfect for my university coding projects!',15,'Approved'),
    (2,2,4,5,'Best iPhone ever, camera is amazing!',22,'Approved'),
    (3,3,5,4,'Great noise canceling, worth the price',18,'Approved'),
    (4,4,6,5,'Dell XPS is a beast for programming!',12,'Approved'),
    (5,5,8,4,'Samsung S24 has amazing display quality',9,'Approved'),
    (6,6,9,5,'iPad Pro is perfect for note taking',14,'Approved'),
    (7,7,10,4,'JBL speaker sound is very loud and clear',7,'Approved'),
    (8,8,11,3,'ThinkPad is good but a bit heavy',5,'Approved'),
    (9,9,12,4,'OnePlus 12 has great battery life',11,'Approved'),
    (10,10,13,5,'Canon R50 takes stunning photos!',20,'Approved'),
    (11,11,14,5,'PS5 controller feels amazing in hand',25,'Approved'),
    (12,13,2,5,'AirPods Pro noise canceling is top notch',19,'Approved'),
    (13,14,4,4,'USB hub works perfectly with my laptop',8,'Approved'),
    (14,15,5,5,'MX Master 3 is best mouse I ever used!',16,'Approved'),
    (15,1,6,4,'HP EliteBook battery life is very good',10,'Approved'),
], columns=['ReviewID','ProductID','UserID','Rating','ReviewText','HelpfulCount','Status'])

shopping_cart = pd.DataFrame([
    (1,2,3,2),(2,4,11,1),(3,5,13,1),(4,6,14,3),
    (5,8,2,1),(6,9,7,2),(7,10,15,1),(8,11,6,1),
    (9,12,4,1),(10,13,10,1),
], columns=['CartID','UserID','ProductID','Quantity'])

# ─────────────────────────────────────────────────────
#  HELPER: format dataframe for display
# ─────────────────────────────────────────────────────
def fmt(df):
    if df is None or len(df) == 0:
        return pd.DataFrame([{"Result": "⚠️ No records found for the given ID."}])
    return df

# ═════════════════════════════════════════════════════
#  6 STORED PROCEDURES
# ═════════════════════════════════════════════════════

def sp_GetUserInfo(user_id):
    try:
        uid = int(user_id)
    except:
        return fmt(None), "❌ Invalid UserID – please enter a number."
    result = users[users['UserID'] == uid][['UserID','FirstName','LastName','Email','PhoneNumber','Address','City','RegistrationDate']]
    if len(result) == 0:
        return fmt(None), f"⚠️ No user found with UserID = {uid}"
    return fmt(result), f"✅ sp_GetUserInfo executed | UserID = {uid} | {len(result)} record(s) returned."

def sp_GetOrderWithDetails(order_id):
    try:
        oid = int(order_id)
    except:
        return fmt(None), "❌ Invalid OrderID – please enter a number."
    o = orders[orders['OrderID'] == oid]
    if len(o) == 0:
        return fmt(None), f"⚠️ No order found with OrderID = {oid}"
    # INNER JOIN: Orders → Users → OrderDetails
    step1 = o.merge(users[['UserID','FirstName','LastName','Email']], on='UserID', how='inner')
    step2 = step1.merge(order_details[['OrderDetailID','OrderID','ProductID','Quantity','UnitPrice','TotalPrice']], on='OrderID', how='inner')
    # INNER JOIN: → Products (only bring non-clashing columns)
    step3 = step2.merge(products[['ProductID','ProductName']], on='ProductID', how='inner')
    # 'Quantity' here = ordered quantity from OrderDetails (no clash since Products cols not included)
    result = step3[['OrderID','OrderDate','TotalAmount','FirstName','Email',
                     'ProductID','ProductName','Quantity','UnitPrice','TotalPrice']].copy()
    result = result.rename(columns={'Quantity': 'OrderedQty'})
    return fmt(result), f"✅ sp_GetOrderWithDetails executed | OrderID = {oid} | {len(result)} record(s) returned."

def sp_GetProductInfo(product_id):
    try:
        pid = int(product_id)
    except:
        return fmt(None), "❌ Invalid ProductID – please enter a number."
    p = products[products['ProductID'] == pid]
    if len(p) == 0:
        return fmt(None), f"⚠️ No product found with ProductID = {pid}"
    # INNER JOIN: Products → Categories on CategoryID
    # categories has 'Status' and 'Description' — suffix with _cat to avoid clash with products columns
    merged = p.merge(
        categories[['CategoryID','CategoryName']],
        on='CategoryID', how='inner'
    )
    result = merged[['ProductID','ProductName','Description','Price','Quantity','CategoryName','ImageURL']].copy()
    return fmt(result), f"✅ sp_GetProductInfo executed | ProductID = {pid} | {len(result)} record(s) returned."

def sp_InsertUser(fname, lname, email, phone, city):
    if not fname or not lname or not email or not phone or not city:
        return fmt(None), "❌ All fields are required to insert a new user."
    if len(phone) != 11:
        return fmt(None), "❌ PhoneNumber must be exactly 11 digits."
    new_id = users['UserID'].max() + 1
    new_row = pd.DataFrame([{
        'UserID': new_id, 'FirstName': fname, 'LastName': lname,
        'Email': email, 'PhoneNumber': phone, 'Address': 'N/A',
        'City': city, 'Country': 'Pakistan', 'Role': 'Customer',
        'Status': 'Active', 'RegistrationDate': datetime.now().strftime('%Y-%m-%d')
    }])
    display = new_row[['UserID','FirstName','LastName','Email','PhoneNumber','City','Status']]
    return fmt(display), f"✅ sp_InsertUser executed | New UserID = {new_id} | '{fname} {lname}' inserted successfully!"

def sp_GetProductsByCategory(category_id):
    try:
        cid = int(category_id)
    except:
        return fmt(None), "❌ Invalid CategoryID – please enter a number."
    p = products[products['CategoryID'] == cid]
    if len(p) == 0:
        return fmt(None), f"⚠️ No products found in CategoryID = {cid}"
    # INNER JOIN: Products → Categories (only take CategoryName to avoid Status/Description clash)
    merged = p.merge(categories[['CategoryID','CategoryName']], on='CategoryID', how='inner')
    result = merged[['ProductID','ProductName','Price','Quantity','Rating','CategoryName']].copy()
    return fmt(result), f"✅ sp_GetProductsByCategory executed | CategoryID = {cid} | {len(result)} product(s) returned."

def sp_GetPaymentByOrder(order_id):
    try:
        oid = int(order_id)
    except:
        return fmt(None), "❌ Invalid OrderID – please enter a number."
    o = orders[orders['OrderID'] == oid]
    if len(o) == 0:
        return fmt(None), f"⚠️ No order found with OrderID = {oid}"
    merged = o.merge(payments, on='OrderID')[['OrderID','TotalAmount','PaymentMethod','Provider','Status_y','TransactionID','PaymentDate']]
    merged = merged.rename(columns={'Status_y': 'PaymentStatus'})
    return fmt(merged), f"✅ sp_GetPaymentByOrder executed | OrderID = {oid} | {len(merged)} record(s) returned."

# ═════════════════════════════════════════════════════
#  7 SQL VIEWS
# ═════════════════════════════════════════════════════

def view_CustomerOrderInfo():
    merged = users.merge(orders, on='UserID')[['UserID','FirstName','LastName','Email','OrderID','OrderDate','TotalAmount','Status_y']]
    merged = merged.rename(columns={'Status_y': 'OrderStatus'})
    return fmt(merged)

def view_ProductOrderDetails():
    # INNER JOIN: Products + OrderDetails on ProductID
    # Both have 'Quantity': products.Quantity=stock, order_details.Quantity=ordered qty
    # Merge with suffixes so we can rename cleanly
    merged = products[['ProductID','ProductName','Price']].merge(
        order_details[['OrderDetailID','OrderID','ProductID','Quantity','UnitPrice','TotalPrice']],
        on='ProductID', how='inner'
    )
    # 'Quantity' here comes only from order_details (products Quantity was excluded) — clean
    result = merged[['ProductID','ProductName','Price','OrderID','Quantity','UnitPrice','TotalPrice']].copy()
    result = result.rename(columns={'Quantity': 'OrderedQty'})
    return fmt(result)

def view_OrderShippingInfo():
    # INNER JOIN: Orders + Shipping on OrderID
    # Both have 'Status' and 'ShippingAddress' — use explicit suffixes to avoid KeyError
    merged = orders[['OrderID','OrderDate','TotalAmount','Status']].merge(
        shipping[['OrderID','ShippingAddress','CourierName','TrackingNumber','Status']],
        on='OrderID', how='inner',
        suffixes=('_order', '_ship')
    )
    result = merged[['OrderID','OrderDate','TotalAmount','ShippingAddress',
                      'CourierName','TrackingNumber','Status_ship']].copy()
    result = result.rename(columns={'Status_ship': 'ShippingStatus'})
    return fmt(result)

def view_ProductCategoryInfo():
    # INNER JOIN: Products + Categories on CategoryID
    # Only pull CategoryName from categories to prevent Description/Status column clashes
    merged = products[['ProductID','ProductName','Price','Quantity','Rating','CategoryID']].merge(
        categories[['CategoryID','CategoryName']], on='CategoryID', how='inner'
    )
    result = merged[['ProductID','ProductName','Price','Quantity','Rating','CategoryName']].copy()
    return fmt(result)

def view_PaymentStatusInfo():
    merged = orders.merge(payments, on='OrderID')[['OrderID','TotalAmount','Status_x','PaymentMethod','Provider','Status_y','TransactionID']]
    merged = merged.rename(columns={'Status_x': 'OrderStatus', 'Status_y': 'PaymentStatus'})
    return fmt(merged)

def view_Top3BestSelling():
    active = orders[orders['Status'] != 'Cancelled']
    merged = active.merge(order_details, on='OrderID').merge(products, on='ProductID').merge(categories, on='CategoryID')
    grouped = merged.groupby(['ProductID','ProductName','CategoryName','Rating']).agg(
        TotalUnitsSold=('Quantity_y', 'sum'),
        TotalRevenue=('TotalPrice', 'sum')
    ).reset_index().sort_values('TotalUnitsSold', ascending=False).head(3)
    return fmt(grouped)

def view_MonthlyRevenue():
    active = orders[orders['Status'] != 'Cancelled'].copy()
    active['OrderDate'] = pd.to_datetime(active['OrderDate'], errors='coerce')
    active['SaleYear'] = active['OrderDate'].dt.year
    active['SaleMonth'] = active['OrderDate'].dt.month
    active['MonthName'] = active['OrderDate'].dt.strftime('%B')
    grouped = active.groupby(['SaleYear','SaleMonth','MonthName']).agg(
        TotalOrders=('OrderID', 'count'),
        TotalRevenue=('TotalAmount', 'sum'),
        AvgOrderValue=('TotalAmount', 'mean')
    ).reset_index().sort_values(['SaleYear','SaleMonth'])
    grouped['AvgOrderValue'] = grouped['AvgOrderValue'].round(2)
    return fmt(grouped)

# ═════════════════════════════════════════════════════
#  5 SQL JOINS
# ═════════════════════════════════════════════════════

def join_inner_users_orders():
    merged = users.merge(orders, on='UserID')[['UserID','FirstName','Email','OrderID','OrderDate','TotalAmount']]
    return fmt(merged), f"🔗 INNER JOIN: Users ⟕ Orders | {len(merged)} matched rows"

def join_left_all_users():
    merged = users.merge(orders, on='UserID', how='left')[['UserID','FirstName','Email','OrderID','OrderDate']]
    return fmt(merged), f"🔗 LEFT JOIN: All Users (with/without Orders) | {len(merged)} rows"

def join_products_reviews():
    merged = products.merge(reviews, on='ProductID')[['ProductID','ProductName','Price','Rating_y','ReviewText']]
    merged = merged.rename(columns={'Rating_y': 'ReviewRating'})
    return fmt(merged), f"🔗 INNER JOIN: Products ⟕ Reviews | {len(merged)} rows"

def join_orders_payments_shipping():
    merged = orders.merge(payments, on='OrderID', how='left').merge(shipping, on='OrderID', how='left')
    cols = ['OrderID','OrderDate','TotalAmount','TransactionID','Status_y','TrackingNumber','CourierName']
    out = merged[cols].rename(columns={'Status_y': 'PaymentStatus'})
    return fmt(out), f"🔗 LEFT JOIN: Orders ⟕ Payments ⟕ Shipping | {len(out)} rows"

def join_orders_discounts():
    merged = orders.merge(discounts, left_on='DiscountID', right_on='DiscountID', how='left')
    cols = ['OrderID','TotalAmount','Status_x','DiscountCode','DiscountPercentage','ValidUpto']
    out = merged[cols].rename(columns={'Status_x': 'OrderStatus'})
    return fmt(out), f"🔗 LEFT JOIN: Orders ⟕ Discounts | {len(out)} rows"

# ═════════════════════════════════════════════════════
#  TRANSACTIONS & TRIGGERS SIMULATION
# ═════════════════════════════════════════════════════

def run_transaction_1():
    txn_id = f"TXN-NEW-{random.randint(100000,999999)}"
    new_order_id = orders['OrderID'].max() + 1
    log = []
    log.append("=" * 60)
    log.append("   TRANSACTION 1: Place New Order")
    log.append("=" * 60)
    log.append(f"[{datetime.now().strftime('%H:%M:%S')}]  BEGIN TRANSACTION;")
    log.append("")
    log.append(f"[{datetime.now().strftime('%H:%M:%S')}]  STEP 1 → INSERT INTO Orders")
    log.append(f"           UserID=2, Amount=85,000, Status='Pending'")
    log.append(f"           ✅ New OrderID assigned: {new_order_id}")
    log.append("")
    log.append(f"[{datetime.now().strftime('%H:%M:%S')}]  ⚡ TRIGGER FIRED: trg_ReduceStock")
    log.append(f"           → Products.Quantity reduced by 1 for ProductID=3")
    log.append(f"           → Sony WH-1000XM5: Stock 15 → 14")
    log.append(f"           → PRINT: 'Stock updated!'")
    log.append("")
    log.append(f"[{datetime.now().strftime('%H:%M:%S')}]  STEP 2 → INSERT INTO OrderDetails")
    log.append(f"           OrderID={new_order_id}, ProductID=3, Qty=1, UnitPrice=85,000")
    log.append(f"           ✅ OrderDetail record created")
    log.append("")
    log.append(f"[{datetime.now().strftime('%H:%M:%S')}]  STEP 3 → INSERT INTO Payments")
    log.append(f"           Method='Credit Card', Provider='JazzCash'")
    log.append(f"           TransactionID='{txn_id}'")
    log.append(f"           ✅ Payment record created")
    log.append("")
    log.append(f"[{datetime.now().strftime('%H:%M:%S')}]  COMMIT;")
    log.append(f"           ✅ Order successfully placed! OrderID: {new_order_id}")
    log.append("=" * 60)
    return "\n".join(log)

def run_transaction_2():
    log = []
    log.append("=" * 60)
    log.append("   TRANSACTION 2: Cancel Order & Restore Stock")
    log.append("=" * 60)
    log.append(f"[{datetime.now().strftime('%H:%M:%S')}]  BEGIN TRANSACTION;")
    log.append(f"           Target OrderID = 1")
    log.append("")
    log.append(f"[{datetime.now().strftime('%H:%M:%S')}]  STEP 1 → UPDATE Orders")
    log.append(f"           SET Status = 'Cancelled' WHERE OrderID = 1")
    log.append(f"           ✅ Order #1 marked as Cancelled")
    log.append("")
    log.append(f"[{datetime.now().strftime('%H:%M:%S')}]  STEP 2 → UPDATE Products (Stock Restore)")
    log.append(f"           HP EliteBook 840 G8: Qty restored +1")
    log.append(f"           Previous Stock: 10 → Restored to: 11")
    log.append(f"           ✅ Inventory restored via OrderDetails join")
    log.append("")
    log.append(f"[{datetime.now().strftime('%H:%M:%S')}]  ⚡ TRIGGER FIRED: trg_ReduceStock (REVERSE)")
    log.append(f"           → Stock update event detected on OrderDetails table")
    log.append(f"           → PRINT: 'Stock updated!'")
    log.append("")
    log.append(f"[{datetime.now().strftime('%H:%M:%S')}]  STEP 3 → UPDATE Payments")
    log.append(f"           SET Status = 'Refunded' WHERE OrderID = 1")
    log.append(f"           TXN-001-112233 → Payment refunded to JazzCash")
    log.append(f"           ✅ Payment status updated")
    log.append("")
    log.append(f"[{datetime.now().strftime('%H:%M:%S')}]  COMMIT;")
    log.append(f"           ✅ Order cancelled and stock restored successfully!")
    log.append("=" * 60)
    return "\n".join(log)

# ═════════════════════════════════════════════════════
#  DASHBOARD SUMMARY STATS
# ═════════════════════════════════════════════════════
def get_summary():
    total_revenue = orders[orders['Status'] != 'Cancelled']['TotalAmount'].sum()
    active_products = len(products[products['Status'] == 'Active'])
    total_customers = len(users[users['Role'] == 'Customer'])
    pending_orders = len(orders[orders['Status'] == 'Pending'])
    return (
        f"💰 Total Revenue: PKR {total_revenue:,.0f}",
        f"📦 Active Products: {active_products}",
        f"👥 Customers: {total_customers}",
        f"⏳ Pending Orders: {pending_orders}"
    )

# ═════════════════════════════════════════════════════
#  GRADIO UI
# ═════════════════════════════════════════════════════

custom_css = """
.stat-box { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            color: white; padding: 15px; border-radius: 10px; text-align: center; font-size: 1.1em; }
.tab-header { font-size: 1.3em; font-weight: bold; color: #333; }
footer { display: none !important; }
"""

with gr.Blocks(title="eShop Enterprise DBMS") as app:

    gr.Markdown("""
    # 🛒 eShop Enterprise DBMS Dashboard
    ### By Fahad Aslam | BSCS Database Management Project
    ---
    """)

    # ── Summary Row ──────────────────────────────────
    rev, prods, custs, pend = get_summary()
    with gr.Row():
        gr.Markdown(f"<div class='stat-box'>{rev}</div>")
        gr.Markdown(f"<div class='stat-box'>{prods}</div>")
        gr.Markdown(f"<div class='stat-box'>{custs}</div>")
        gr.Markdown(f"<div class='stat-box'>{pend}</div>")

    gr.Markdown("---")

    with gr.Tabs():

        # ══════════════════════════════════════════════
        #  TAB 1 – STORED PROCEDURES
        # ══════════════════════════════════════════════
        with gr.TabItem("⚙️ Stored Procedures (6)"):
            gr.Markdown("### Execute SQL Stored Procedures — Filter by ID")

            with gr.Tabs():

                with gr.TabItem("SP1 – Get User Info"):
                    gr.Markdown("**`sp_GetUserInfo @UserID`** — Returns user profile details")
                    with gr.Row():
                        sp1_in = gr.Number(label="Enter UserID (1–15)", value=1, precision=0)
                        sp1_btn = gr.Button("▶ Execute", variant="primary")
                    sp1_msg = gr.Textbox(label="Execution Log", interactive=False)
                    sp1_out = gr.Dataframe(label="Result Set", wrap=True)
                    sp1_btn.click(fn=sp_GetUserInfo, inputs=sp1_in, outputs=[sp1_out, sp1_msg])

                with gr.TabItem("SP2 – Get Order Details"):
                    gr.Markdown("**`sp_GetOrderWithDetails @OrderID`** — Returns full order breakdown with product info")
                    with gr.Row():
                        sp2_in = gr.Number(label="Enter OrderID (1–15)", value=1, precision=0)
                        sp2_btn = gr.Button("▶ Execute", variant="primary")
                    sp2_msg = gr.Textbox(label="Execution Log", interactive=False)
                    sp2_out = gr.Dataframe(label="Result Set", wrap=True)
                    sp2_btn.click(fn=sp_GetOrderWithDetails, inputs=sp2_in, outputs=[sp2_out, sp2_msg])

                with gr.TabItem("SP3 – Get Product Info"):
                    gr.Markdown("**`sp_GetProductInfo @ProductID`** — Returns product info with category")
                    with gr.Row():
                        sp3_in = gr.Number(label="Enter ProductID (1–15)", value=1, precision=0)
                        sp3_btn = gr.Button("▶ Execute", variant="primary")
                    sp3_msg = gr.Textbox(label="Execution Log", interactive=False)
                    sp3_out = gr.Dataframe(label="Result Set", wrap=True)
                    sp3_btn.click(fn=sp_GetProductInfo, inputs=sp3_in, outputs=[sp3_out, sp3_msg])

                with gr.TabItem("SP4 – Insert New User"):
                    gr.Markdown("**`sp_InsertUser`** — Insert a new customer record into the Users table")
                    with gr.Row():
                        sp4_fn = gr.Textbox(label="First Name", placeholder="Ahmed")
                        sp4_ln = gr.Textbox(label="Last Name", placeholder="Khan")
                        sp4_em = gr.Textbox(label="Email", placeholder="ahmed@example.com")
                    with gr.Row():
                        sp4_ph = gr.Textbox(label="Phone (11 digits)", placeholder="03001234567")
                        sp4_ci = gr.Textbox(label="City", placeholder="Karachi")
                        sp4_btn = gr.Button("▶ Execute INSERT", variant="primary")
                    sp4_msg = gr.Textbox(label="Execution Log", interactive=False)
                    sp4_out = gr.Dataframe(label="Inserted Record", wrap=True)
                    sp4_btn.click(fn=sp_InsertUser, inputs=[sp4_fn, sp4_ln, sp4_em, sp4_ph, sp4_ci], outputs=[sp4_out, sp4_msg])

                with gr.TabItem("SP5 – Products by Category"):
                    gr.Markdown("**`sp_GetProductsByCategory @CategoryID`** — Returns all products in a category")
                    gr.Markdown("Categories: 1=Laptops | 2=Smartphones | 3=Audio | 4=Tablets | 5=Accessories | 6=Cameras | 7=Gaming")
                    with gr.Row():
                        sp5_in = gr.Number(label="Enter CategoryID (1–7)", value=1, precision=0)
                        sp5_btn = gr.Button("▶ Execute", variant="primary")
                    sp5_msg = gr.Textbox(label="Execution Log", interactive=False)
                    sp5_out = gr.Dataframe(label="Result Set", wrap=True)
                    sp5_btn.click(fn=sp_GetProductsByCategory, inputs=sp5_in, outputs=[sp5_out, sp5_msg])

                with gr.TabItem("SP6 – Payment by Order"):
                    gr.Markdown("**`sp_GetPaymentByOrder @OrderID`** — Returns payment details for a specific order")
                    with gr.Row():
                        sp6_in = gr.Number(label="Enter OrderID (1–15)", value=1, precision=0)
                        sp6_btn = gr.Button("▶ Execute", variant="primary")
                    sp6_msg = gr.Textbox(label="Execution Log", interactive=False)
                    sp6_out = gr.Dataframe(label="Result Set", wrap=True)
                    sp6_btn.click(fn=sp_GetPaymentByOrder, inputs=sp6_in, outputs=[sp6_out, sp6_msg])

        # ══════════════════════════════════════════════
        #  TAB 2 – SQL VIEWS
        # ══════════════════════════════════════════════
        with gr.TabItem("👁️ SQL Views (7)"):
            gr.Markdown("### Pre-Built SQL Views — Click to Load Data")

            with gr.Tabs():

                with gr.TabItem("View 1 – Customer Orders"):
                    gr.Markdown("**`vw_CustomerOrderInfo`** — INNER JOIN: Users + Orders")
                    v1_btn = gr.Button("📋 Load View", variant="primary")
                    v1_out = gr.Dataframe(label="vw_CustomerOrderInfo", wrap=True)
                    v1_btn.click(fn=view_CustomerOrderInfo, outputs=v1_out)

                with gr.TabItem("View 2 – Product Order Details"):
                    gr.Markdown("**`vw_ProductOrderDetails`** — INNER JOIN: Products + OrderDetails")
                    v2_btn = gr.Button("📋 Load View", variant="primary")
                    v2_out = gr.Dataframe(label="vw_ProductOrderDetails", wrap=True)
                    v2_btn.click(fn=view_ProductOrderDetails, outputs=v2_out)

                with gr.TabItem("View 3 – Order Shipping"):
                    gr.Markdown("**`vw_OrderShippingInfo`** — INNER JOIN: Orders + Shipping")
                    v3_btn = gr.Button("📋 Load View", variant="primary")
                    v3_out = gr.Dataframe(label="vw_OrderShippingInfo", wrap=True)
                    v3_btn.click(fn=view_OrderShippingInfo, outputs=v3_out)

                with gr.TabItem("View 4 – Product Categories"):
                    gr.Markdown("**`vw_ProductCategoryInfo`** — INNER JOIN: Products + Categories")
                    v4_btn = gr.Button("📋 Load View", variant="primary")
                    v4_out = gr.Dataframe(label="vw_ProductCategoryInfo", wrap=True)
                    v4_btn.click(fn=view_ProductCategoryInfo, outputs=v4_out)

                with gr.TabItem("View 5 – Payment Status"):
                    gr.Markdown("**`vw_PaymentStatusInfo`** — INNER JOIN: Orders + Payments")
                    v5_btn = gr.Button("📋 Load View", variant="primary")
                    v5_out = gr.Dataframe(label="vw_PaymentStatusInfo", wrap=True)
                    v5_btn.click(fn=view_PaymentStatusInfo, outputs=v5_out)

                with gr.TabItem("View 6 – Top 3 Best Selling"):
                    gr.Markdown("**`vw_Top3BestSelling`** — Top 3 products by units sold (excluding Cancelled orders)")
                    v6_btn = gr.Button("📋 Load View", variant="primary")
                    v6_out = gr.Dataframe(label="vw_Top3BestSelling", wrap=True)
                    v6_btn.click(fn=view_Top3BestSelling, outputs=v6_out)

                with gr.TabItem("View 7 – Monthly Revenue"):
                    gr.Markdown("**`vw_MonthlyRevenue`** — Revenue breakdown by month/year")
                    v7_btn = gr.Button("📋 Load View", variant="primary")
                    v7_out = gr.Dataframe(label="vw_MonthlyRevenue", wrap=True)
                    v7_btn.click(fn=view_MonthlyRevenue, outputs=v7_out)

        # ══════════════════════════════════════════════
        #  TAB 3 – SQL JOINS
        # ══════════════════════════════════════════════
        with gr.TabItem("🔗 SQL Joins (5)"):
            gr.Markdown("### 5 Distinct SQL JOIN Operations")

            with gr.Tabs():

                with gr.TabItem("JOIN 1 – INNER: Users × Orders"):
                    gr.Markdown("**INNER JOIN** — Only users who have placed at least one order")
                    j1_btn = gr.Button("▶ Run JOIN", variant="primary")
                    j1_msg = gr.Textbox(label="Join Info", interactive=False)
                    j1_out = gr.Dataframe(label="Result", wrap=True)
                    j1_btn.click(fn=join_inner_users_orders, outputs=[j1_out, j1_msg])

                with gr.TabItem("JOIN 2 – LEFT: All Users"):
                    gr.Markdown("**LEFT JOIN** — All users, including those with no orders (NULL for order columns)")
                    j2_btn = gr.Button("▶ Run JOIN", variant="primary")
                    j2_msg = gr.Textbox(label="Join Info", interactive=False)
                    j2_out = gr.Dataframe(label="Result", wrap=True)
                    j2_btn.click(fn=join_left_all_users, outputs=[j2_out, j2_msg])

                with gr.TabItem("JOIN 3 – INNER: Products × Reviews"):
                    gr.Markdown("**INNER JOIN** — Products that have received at least one review")
                    j3_btn = gr.Button("▶ Run JOIN", variant="primary")
                    j3_msg = gr.Textbox(label="Join Info", interactive=False)
                    j3_out = gr.Dataframe(label="Result", wrap=True)
                    j3_btn.click(fn=join_products_reviews, outputs=[j3_out, j3_msg])

                with gr.TabItem("JOIN 4 – Orders + Payments + Shipping"):
                    gr.Markdown("**LEFT JOIN (Multi-table)** — Orders with their Payment & Shipping info")
                    j4_btn = gr.Button("▶ Run JOIN", variant="primary")
                    j4_msg = gr.Textbox(label="Join Info", interactive=False)
                    j4_out = gr.Dataframe(label="Result", wrap=True)
                    j4_btn.click(fn=join_orders_payments_shipping, outputs=[j4_out, j4_msg])

                with gr.TabItem("JOIN 5 – Orders × Discounts"):
                    gr.Markdown("**LEFT JOIN** — All orders showing applied discount codes (NULL if no discount)")
                    j5_btn = gr.Button("▶ Run JOIN", variant="primary")
                    j5_msg = gr.Textbox(label="Join Info", interactive=False)
                    j5_out = gr.Dataframe(label="Result", wrap=True)
                    j5_btn.click(fn=join_orders_discounts, outputs=[j5_out, j5_msg])

        # ══════════════════════════════════════════════
        #  TAB 4 – TRANSACTIONS & TRIGGERS
        # ══════════════════════════════════════════════
        with gr.TabItem("🔄 Transactions & Triggers (2+2)"):
            gr.Markdown("""
            ### SQL Transactions with Embedded Trigger Activity Log
            Each transaction simulates the full SQL execution pipeline, **including TRIGGER fire events**.
            - **trg_ReduceStock** — fires AFTER INSERT on OrderDetails
            - **trg_UpdateRating** — fires AFTER INSERT on Reviews
            """)

            with gr.Row():
                with gr.Column():
                    gr.Markdown("#### 📝 Transaction 1: Place New Order")
                    gr.Markdown("""
                    **Operations:**
                    1. `INSERT INTO Orders` — creates new order
                    2. `INSERT INTO OrderDetails` → ⚡ fires **trg_ReduceStock**
                    3. `INSERT INTO Payments` — logs payment
                    4. `COMMIT` — all-or-nothing
                    """)
                    txn1_btn = gr.Button("▶ Execute Transaction 1", variant="primary", size="lg")
                    txn1_log = gr.Textbox(label="Transaction + Trigger Execution Log", lines=20, interactive=False, max_lines=25)
                    txn1_btn.click(fn=run_transaction_1, outputs=txn1_log)

                with gr.Column():
                    gr.Markdown("#### ❌ Transaction 2: Cancel Order & Restore Stock")
                    gr.Markdown("""
                    **Operations:**
                    1. `UPDATE Orders` — set Status = 'Cancelled'
                    2. `UPDATE Products` — restore stock ← ⚡ **trg_ReduceStock** detects change
                    3. `UPDATE Payments` — set Status = 'Refunded'
                    4. `COMMIT` — atomically applied
                    """)
                    txn2_btn = gr.Button("▶ Execute Transaction 2", variant="primary", size="lg")
                    txn2_log = gr.Textbox(label="Transaction + Trigger Execution Log", lines=20, interactive=False, max_lines=25)
                    txn2_btn.click(fn=run_transaction_2, outputs=txn2_log)

            gr.Markdown("""
            ---
            #### 🔦 Trigger Reference Summary
            | Trigger Name | Table | Event | Action |
            |---|---|---|---|
            | `trg_ReduceStock` | OrderDetails | AFTER INSERT | Reduces Products.Quantity |
            | `trg_UpdateRating` | Reviews | AFTER INSERT | Recalculates Products.Rating (AVG) |
            """)

        # ══════════════════════════════════════════════
        #  TAB 5 – RAW TABLES
        # ══════════════════════════════════════════════
        with gr.TabItem("🗄️ Raw Tables"):
            gr.Markdown("### Browse All Database Tables")
            with gr.Tabs():
                with gr.TabItem("Categories"):
                    gr.Dataframe(value=categories, label="Categories Table", wrap=True)
                with gr.TabItem("Users"):
                    gr.Dataframe(value=users[['UserID','FirstName','LastName','Email','City','Role','Status']], label="Users Table", wrap=True)
                with gr.TabItem("Products"):
                    gr.Dataframe(value=products[['ProductID','ProductName','Price','Quantity','Rating','Status']], label="Products Table", wrap=True)
                with gr.TabItem("Orders"):
                    gr.Dataframe(value=orders[['OrderID','UserID','TotalAmount','Status','OrderDate']], label="Orders Table", wrap=True)
                with gr.TabItem("Order Details"):
                    gr.Dataframe(value=order_details, label="OrderDetails Table", wrap=True)
                with gr.TabItem("Payments"):
                    gr.Dataframe(value=payments[['PaymentID','OrderID','Amount','PaymentMethod','Provider','Status','TransactionID']], label="Payments Table", wrap=True)
                with gr.TabItem("Shipping"):
                    gr.Dataframe(value=shipping[['ShippingID','OrderID','City','ShippingMethod','CourierName','TrackingNumber','Status']], label="Shipping Table", wrap=True)
                with gr.TabItem("Reviews"):
                    gr.Dataframe(value=reviews, label="Reviews Table", wrap=True)
                with gr.TabItem("Discounts"):
                    gr.Dataframe(value=discounts, label="Discounts Table", wrap=True)
                with gr.TabItem("Shopping Cart"):
                    gr.Dataframe(value=shopping_cart, label="ShoppingCart Table", wrap=True)

    gr.Markdown("""
    ---
    <center><small>eShop Enterprise DBMS · Fahad Aslam · BSCS Project 2026 · Built with Python + Gradio</small></center>
    """)

if __name__ == "__main__":
    app.launch(server_name="0.0.0.0", server_port=7860, share=False, theme=gr.themes.Soft())