from tkinter import*
from tkinter import messagebox
import sqlite3
color="#ECF2FF"
window= Tk()
window.title("Sales management")
window.geometry("720x750")
window.config(bg=color)

product_name_text= StringVar()
product_id_text= IntVar()
quantity_sold_text= StringVar()
quantity_left_text= StringVar()
prices_text= StringVar()
today_saleq_text= StringVar()
today_saletp_text= StringVar()
week_sales_text= StringVar()
week_salestp_text= StringVar()
month_sales_text= StringVar()
month_salestp_text= StringVar()
delete_entry_text= StringVar()

#labels

product_name_label= Label(text="Product Name",bg=color)
product_id_label= Label(text="Product Id",bg=color)
quantity_sold_label= Label(text="Quantity Sold",bg=color)
quantity_left_label= Label(text="Quantity Left",bg=color)
prices_label= Label(text="Price",bg=color)
today_saleq_label= Label(text="Today's Sale(Quantity)",bg=color)
today_saletp_label= Label(text="Today's Sale(Total Price)",bg=color)
week_sales_label= Label(text="Week Sales(Quantity)",bg=color)
week_salestp_label= Label(text="Week Sales(Total Price)",bg=color)
month_sales_label= Label(text="Month Sales(Quantity)",bg=color)
month_salestp_label= Label(text="Month Sales(Total Price)",bg=color)
product_list_label = Label(text='Product List', font=(30), borderwidth=1, relief="solid", width=50)
product_list_label.grid(row=12, column=0, columnspan=50, pady=20)

pdt_name = Label(text='Product Name', borderwidth=1, relief="solid")
pdt_id = Label(text='Product ID', borderwidth=1, relief="solid")
pdt_price = Label(text='Product Price', borderwidth=1, relief="solid")
pdt_sales_quantity = Label(text="Today's Sales(Quantity)", borderwidth=1, relief="solid")

#entries
product_name_entry= Entry(textvariable=product_name_text)
product_id_entry= Entry(textvariable=product_id_text)
quantity_sold_entry= Entry(textvariable=quantity_sold_text)
quantity_left_entry= Entry(textvariable=quantity_left_text)
prices_entry=Entry(textvariable=prices_text)
today_saleq_entry= Entry(textvariable=today_saleq_text)
today_saletp_entry= Entry(textvariable=today_saletp_text)
week_sales_entry= Entry(textvariable=week_sales_text)
week_salestp_entry= Entry(textvariable=week_salestp_text)
month_sales_entry= Entry(textvariable=month_sales_text)
month_salestp_entry= Entry(textvariable=month_salestp_text)
delete_entry = Entry(textvariable=delete_entry_text, width=20)
delete_entry.grid(row=0, column=3, padx=10, columnspan=20, rowspan=2)
delete_entry.insert(0, 'Enter id to delete')


def Refresh():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS products (name TEXT, id TEXT PRIMARY KEY, quantitySold TEXT, quantityLeft TEXT, price TEXT, todaySalesQuantity TEXT, todaySalesTotalPrice TEXT, weekSalesQuantity TEXT, weekSalesTotalPrice TEXT, monthSalesQuantity TEXT, monthSalesTotalPrice TEXT)")

    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()

    for i in range(len(products)):
        Label(text=products[i][0]).grid(row=i+14, column=0)
        Label(text=products[i][1]).grid(row=i+14, column=1)
        Label(text=products[i][4]).grid(row=i+14, column=2)
        Label(text=products[i][5]).grid(row=i+14, column=3)
    conn.close()

def show_message(title, message):
    messagebox.showerror(title, message)

def add():
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO products (name, id, quantitySold, quantityLeft, price, todaySalesQuantity, todaySalesTotalPrice, weekSalesQuantity, weekSalesTotalPrice, monthSalesQuantity, monthSalesTotalPrice) VALUES (?, ?, ?, ?,?,?,?,?,?,?,?)", (str(product_name_text.get()), str(product_id_text.get()), str(quantity_sold_text.get()), str(quantity_left_text.get()), str(prices_text.get()), str(today_saleq_text.get()), str(today_saletp_text.get()), str(week_sales_text.get()), str(week_salestp_text.get()), str(month_sales_text.get()), str(month_salestp_text.get())))

        conn.commit()
    except sqlite3.Error as e:
        show_message('Sqlite error', e)
    finally:
        Refresh()
        conn.close()

def delete():
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM products')
        cursor.execute("DELETE FROM products WHERE id = ?", (str(delete_entry.get())))
        conn.commit()
        show_message('Success', 'Product deleted')
        conn.close()
        Refresh()
    except sqlite3.Error as e:
        show_message('Sqlite error', e)
    finally:
        conn.close()
        Refresh()

def update():
    price = prices_text.get()
    quantity_sold = quantity_sold_text.get()
    quantity_left = quantity_left_text.get()
    today_sales_quantity = today_saleq_text.get()
    week_sales_quantity = week_salestp_text.get()
    month_sales_quantity = month_sales_text.get()
    if len(price) < 1 or len(quantity_sold) < 1 or len(quantity_left) < 1 or len(today_sales_quantity) < 1 or len(week_sales_quantity) < 1 or len(month_sales_quantity) < 1:
        show_message('Python error!', 'Please enter values for all fields')
        return
    try:
        price = int(price)
        quantity_sold = int(quantity_sold)
        quantity_left = int(quantity_left)
        today_sales_quantity = int(today_sales_quantity)
        week_sales_quantity = int(week_sales_quantity)
        month_sales_quantity = int(month_sales_quantity)
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("UPDATE products SET name=?, id=?, quantitySold=?, quantityLeft=?, price=?, todaySalesQuantity=?, todaySalesTotalPrice=?, weekSalesQuantity=?, weekSalesTotalPrice=?, monthSalesQuantity=?, monthSalesTotalPrice=?  WHERE id=?", (str(product_name_text.get()), str(product_id_text.get()), str(quantity_sold_text.get()), str(quantity_left_text.get()), str(prices_text.get()), str(today_saleq_text.get()), str(today_saletp_text.get()), str(week_sales_text.get()), str(week_salestp_text.get()), str(month_sales_text.get()), str(month_salestp_text.get()), str(product_id_text.get())))
        conn.commit()
        Refresh()
        show_message('Success', 'Product updated')
        conn.close()
    except sqlite3.Error as e:
        show_message('Sqlite error', e)
    finally:
        Refresh()
        conn.close()

def calculate():
    price = prices_text.get()
    quantity_sold = quantity_sold_text.get()
    quantity_left = quantity_left_text.get()
    today_sales_quantity = today_saleq_text.get()
    week_sales_quantity = week_sales_text.get()
    month_sales_quantity = month_sales_text.get()
    if len(price) < 1 or len(quantity_sold) < 1 or len(quantity_left) < 1 or len(today_sales_quantity) < 1 or len(week_sales_quantity) < 1 or len(month_sales_quantity) < 1:
        show_message('Python error!', 'Please enter values for all fields')
        return
    try:
        price = int(price)
        quantity_sold = int(quantity_sold)
        quantity_left = int(quantity_left)
        today_sales_quantity = int(today_sales_quantity)
        week_sales_quantity = int(week_sales_quantity)
        month_sales_quantity = int(month_sales_quantity)
    except:
        show_message('Python error!', 'Please enter integer values in these fields-> Price, Today Sales(Quantity), Week Sales(Quantity), Month Sales(Quantity)')
        return
    today_sales_total_price = price * today_sales_quantity
    week_sales_total_price = price * week_sales_quantity
    month_sales_total_price = price * month_sales_quantity

    today_saletp_text.set(today_sales_total_price)
    week_salestp_text.set(week_sales_total_price)
    month_salestp_text.set(month_sales_total_price)
    add_button.config(state='normal')

Refresh()

update_button= Button(text="UPDATE",width=20,height=2,command=update)
delete_button= Button(text="DELETE",width=20,height=2,command=delete)
add_button= Button(text="ADD",width=20,height=2,command=add)
add_button.config(state='disabled')
calculate_button = Button(text='Verify And Calculate Prices', width=20, height=2, command=calculate)
refresh_button = Button(text='Refresh Table', width=20, height=2, command=Refresh)

#label grids bullshit
product_name_label.grid(column=0,row=0,padx=10,pady=10,sticky="w")
product_id_label.grid(column=0,row=1,padx=10,pady=10,sticky="w")
quantity_sold_label.grid(column=0,row=2,padx=10,pady=10,sticky="w")
quantity_left_label.grid(column=0,row=3,padx=10,pady=10,sticky="w")
prices_label.grid(column=0,row=4,padx=10,pady=10,sticky="w")
today_saleq_label.grid(column=0,row=5,padx=10,pady=10,sticky="w")
today_saletp_label.grid(column=0,row=6,padx=10,pady=10,sticky="w")
week_sales_label.grid(column=0,row=7,padx=10,pady=10,sticky="w")
week_salestp_label.grid(column=0,row=8,padx=10,pady=10,sticky="w")
month_sales_label.grid(column=0,row=9,padx=10,pady=10,sticky="w")
month_salestp_label.grid(column=0,row=10,padx=10,pady=10,sticky="w")


#entries label bullshit
product_name_entry.grid(column=1,row=0,padx=10,pady=10,sticky="w")
product_id_entry.grid(column=1,row=1,padx=10,pady=10,sticky="w")
quantity_sold_entry.grid(column=1,row=2,padx=10,pady=10,sticky="w")
quantity_left_entry.grid(column=1,row=3,padx=10,pady=10,sticky="w")
prices_entry.grid(column=1,row=4,padx=10,pady=10,sticky="w")
today_saleq_entry.grid(column=1,row=5,padx=10,pady=10,sticky="w")
today_saletp_entry.grid(column=1,row=6,padx=10,pady=10,sticky="w")
week_sales_entry.grid(column=1,row=7,padx=10,pady=10,sticky="w")
week_salestp_entry.grid(column=1,row=8,padx=10,pady=10,sticky="w")
month_sales_entry.grid(column=1,row=9,padx=10,pady=10,sticky="w")
month_salestp_entry.grid(column=1,row=10,padx=10,pady=10,sticky="w")
today_saletp_entry.config(state='disabled')
week_salestp_entry.config(state='disabled')
month_salestp_entry.config(state='disabled')
update_button.grid(row=2, column=3,pady=50, rowspan=2, padx=15)
delete_button.grid(row=1, column=3, rowspan=2, padx=15)
calculate_button.grid(row=11, column=1)
add_button.grid(row=4, column=3)
refresh_button.grid(row=5, column=3,pady=30)

pdt_name.grid(row=13, column=0)
pdt_id.grid(row=13, column=1)
pdt_price.grid(row=13, column=2)
pdt_sales_quantity.grid(row=13, column=3)

window.mainloop()