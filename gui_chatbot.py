import tkinter as tk
from tkinter import scrolledtext

faqs = {
    "ai": "AI stands for Artificial Intelligence. It enables machines to perform tasks that normally require human intelligence.",
    "ml": "ML stands for Machine Learning. It allows computers to learn from data and make predictions.",
    "python": "Python is a high-level programming language widely used in AI and machine learning.",
    "nlp": "NLP stands for Natural Language Processing. It helps computers understand human language.",
    "deep learning": "Deep Learning is a type of machine learning based on artificial neural networks.",
    "chatbot": "A chatbot is a software application that communicates with users.",
    "computer vision": "Computer Vision helps computers understand images and videos."
}

def get_answer():
    question = entry.get().lower().strip()

    if not question:
        return

    chat_box.insert(tk.END, "You: " + question + "\n")

    answer = "Sorry, I don't understand your question."

    for keyword in faqs:
        if keyword in question:
            answer = faqs[keyword]
            break

    chat_box.insert(tk.END, "Bot: " + answer + "\n\n")
    entry.delete(0, tk.END)

window = tk.Tk()
window.title("FAQ Chatbot")
window.geometry("600x500")

title = tk.Label(
    window,
    text="FAQ CHATBOT",
    font=("Arial", 20, "bold")
)
title.pack(pady=10)

chat_box = scrolledtext.ScrolledText(
    window,
    width=65,
    height=20,
    font=("Arial", 11)
)
chat_box.pack(padx=10, pady=10)

entry = tk.Entry(
    window,
    width=45,
    font=("Arial", 12)
)
entry.pack(side=tk.LEFT, padx=10, pady=10)

send_button = tk.Button(
    window,
    text="Send",
    command=get_answer
)
send_button.pack(side=tk.LEFT)

window.mainloop()