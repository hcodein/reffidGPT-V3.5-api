
import tkinter as tk
from tkinter import scrolledtext
from gradio_client import Client

# Initialize the Gradio client

client = Client("yyasso/reffidGPT-V3.5-speed")
# Function to handle user input and get chatbot response

def send_message():
    user_message = input_box.get("1.0", tk.END).strip()
    if not user_message:

        return
    input_box.delete("1.0", tk.END)
    chat_display.insert(tk.END, f"You: {user_message}\n")
    # Get the response from the chatbot
    try:
        result = client.predict(

            message=user_message,
            system_message="Your name is reffidGPT,Developed by H.coding Company,You are a friendly Chatbot.",
            max_tokens=2048,
            temperature=0.9,
            top_p=0.95,
            api_name="/chat"
        )

        chat_display.insert(tk.END, f"reffidGPT: {result}\n")
    except Exception as e:
        chat_display.insert(tk.END, f"Error: {e}\n")

# Create the main application window
app = tk.Tk()
app.title("reffidGPT Chatbot")
app.geometry("500x500")

# Create a scrollable text area for chat display
chat_display = scrolledtext.ScrolledText(app, wrap=tk.WORD, height=20, width=60, state="normal")
chat_display.pack(pady=10)

# Create a text input box for user messages
input_box = tk.Text(app, height=3, width=50)
input_box.pack(pady=10)

# Create a "Send" button
send_button = tk.Button(app, text="Send", command=send_message)
send_button.pack()
# Run the Tkinter event loop
app.mainloop()

