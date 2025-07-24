import tkinter as tk

# ---------------- Chatbot Logic ---------------- #
def chatbot_response(user_input):
    user_input = user_input.lower() 

    if "add" in user_input and ("product" in user_input or "item" in user_input):
        return "🛒 To add a new product, click on the 'Products' tab from the dashboard and fill in the required fields like name, supplier, price, etc."
    
    elif "delete" in user_input or "remove" in user_input:
        return "🗑️ Use the same section where you added items (like Products, Employees, etc.) and click the 'Delete' button after selecting the record."

    elif "low stock" in user_input or "stock alert" in user_input:
        return "⚠️ You can see low-stock alerts in the Products section. Products below threshold quantities are marked for restocking."

    elif "employee" in user_input:
        return "👥 Go to the 'Employee' tab to add, edit, or search employee details using name, email, or contact number."

    elif "supplier" in user_input:
        return "📦 Click the 'Supplier' tab. You can manage suppliers, add new ones, or search them by invoice number."

    elif "category" in user_input:
        return "🗂️ 'Category' helps group similar products. Click the tab and add or delete categories as needed."

    elif "billing" in user_input or "bill" in user_input:
        return "🧾 Use the 'Billing' section to generate bills. Select products, quantities, and discounts. Bills are auto-saved in the 'bill' folder."

    elif "sales" in user_input:
        return "💰 Click on the 'Sales' tab to see past invoices and sales records. Search by invoice number to view details."

    elif "how are you" in user_input:
        return "I'm just a bunch of Python code, but I’m here to help you run your store like a pro! 💼"

    elif "hello" in user_input or "hi" in user_input:
        return "Hello 👋 I'm your Inventory Assistant! You can ask me about adding items, checking stock, or where to find billing."

    elif "help" in user_input or "what can you do" in user_input:
        return ("🤖 I can assist you with:\n"
                "- How to add/delete products\n"
                "- Viewing low stock items\n"
                "- Where to manage employees/suppliers\n"
                "- How billing and sales work")

    else:
        return "❓ I didn’t understand that. Try asking things like:\n- How to add product?\n- Show low stock\n- How to generate bill?"

# ---------------- UI Setup ---------------- #
def open_chatbot():
    chat = tk.Toplevel()
    chat.title("Inventory Chatbot Assistant")
    chat.geometry("550x550")
    chat.configure(bg="#f2f2f2")

    # Title
    title_label = tk.Label(chat, text="💬 Inventory Chatbot Assistant", font=("Helvetica", 16, "bold"), bg="#283747", fg="white", pady=10)
    title_label.pack(fill=tk.X)

    # Chat history area with scrollbar
    frame_chat = tk.Frame(chat)
    frame_chat.pack(pady=10)

    scrollbar = tk.Scrollbar(frame_chat)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    chatbox = tk.Text(frame_chat, height=20, width=65, yscrollcommand=scrollbar.set, wrap=tk.WORD, bg="white", font=("Helvetica", 11))
    chatbox.pack()
    scrollbar.config(command=chatbox.yview)

    # Entry area
    entry_frame = tk.Frame(chat)
    entry_frame.pack(pady=10)

    entry = tk.Entry(entry_frame, width=50, font=("Helvetica", 12))
    entry.pack(side=tk.LEFT, padx=(10, 5))

    def send_message():
        user_msg = entry.get().strip()
        if user_msg == "":
            return
        reply = chatbot_response(user_msg)

        chatbox.insert(tk.END, f"\nYou: {user_msg}")
        chatbox.insert(tk.END, f"\nBot: {reply}\n")
        chatbox.see(tk.END)
        entry.delete(0, tk.END)

    send_button = tk.Button(entry_frame, text="Send", font=("Helvetica", 12), bg="#3498db", fg="white", command=send_message)
    send_button.pack(side=tk.LEFT)

    # Intro message
    chatbox.insert(tk.END, "Bot: Hello 👋! I'm your assistant.\nAsk me anything related to inventory, like:\n- How to add item\n- Show low stock\n- Where is billing\n\n")

    entry.bind("<Return>", lambda event: send_message())  # Pressing Enter also sends message
