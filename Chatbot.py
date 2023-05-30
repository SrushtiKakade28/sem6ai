pip install tkinter
from tkinter import *
root = Tk()
root.title("Chatbot")
def send():
    send = "You -> "+e.get()
    txt.insert(END, "n"+send)
    user = e.get().lower()
    if(user == "hello"):
        txt.insert(END, "n" + "Bot -> Hi")
    elif(user == "hi" or user == "hii" or user == "hiiii"):
        txt.insert(END, "n" + "Bot -> Hello")
    elif(e.get() == "how are you"):
        txt.insert(END, "n" + "Bot -> fine! and you")
    elif(user == "fine" or user == "i am good" or user == "i am doing good"):
        txt.insert(END, "n" + "Bot -> Great! how can I help you.")
    else:
        txt.insert(END, "n" + "Bot -> Sorry! I dind't got you")
    e.delete(0, END)
txt = Text(root)
txt.grid(row=0, column=0, columnspan=2)
e = Entry(root, width=100)
e.grid(row=1, column=0)
send = Button(root, text="Send", command=send).grid(row=1, column=1)
root.mainloop()





orrr
def greet():
    print("Chatbot: Hello! How can I assist you today?")


def goodbye():
    print("Chatbot: Thank you for chatting with me. Goodbye!")


def process_input(user_input):
    if user_input.lower() == "hello":
        print("Chatbot: Hi there!")
    elif user_input.lower() == "help":
        print("Chatbot: I'm here to help you. How can I assist you?")
    elif user_input.lower() == "bye":
        goodbye()
        return True
    else:
        print("Chatbot: I'm sorry, I didn't understand that. Can you please rephrase or ask a different question?")


def start_chat():
    greet()
    while True:
        user_input = input("User: ")
        should_exit = process_input(user_input)
        if should_exit:
            break


# Start the chatbot
start_chat()
