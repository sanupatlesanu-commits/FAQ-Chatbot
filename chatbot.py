from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

questions = [
    "what is machine learning",
    "what is ml",
    "what is artificial intelligence",
    "what is ai",
    "what is python",
    "what is nlp",
    "what is natural language processing",
    "what is deep learning",
    "what is chatbot",
    "what is computer vision"
]

answers = [
    "Machine Learning is a branch of AI that allows computers to learn from data.",
    "ML stands for Machine Learning. It allows computers to learn from data and make predictions.",
    "Artificial Intelligence is the ability of machines to perform tasks that normally require human intelligence.",
    "AI stands for Artificial Intelligence. It enables machines to perform tasks that normally require human intelligence.",
    "Python is a high-level programming language widely used in AI, machine learning and software development.",
    "NLP stands for Natural Language Processing. It helps computers understand human language.",
    "Natural Language Processing is a field of AI that helps computers understand and process human language.",
    "Deep Learning is a type of machine learning based on artificial neural networks.",
    "A chatbot is a software application that communicates with users using text or voice.",
    "Computer Vision is a field of AI that helps computers understand images and videos."
]

vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)

print("================================")
print("          FAQ CHATBOT")
print("================================")
print("Ask your question.")
print("Type 'exit' to stop.")

while True:

    user_input = input("\nYou: ")
    user_lower = user_input.lower().strip()

    if user_lower == "exit":
        print("Bot: Thank you! Goodbye.")
        break

    # Direct keyword matching
    if "machine learning" in user_lower or user_lower == "ml":
        print("Bot:", answers[0])
        continue

    if "artificial intelligence" in user_lower or user_lower == "ai":
        print("Bot:", answers[2])
        continue

    if "python" in user_lower:
        print("Bot:", answers[4])
        continue

    if "nlp" in user_lower or "natural language processing" in user_lower:
        print("Bot:", answers[5])
        continue

    if "deep learning" in user_lower:
        print("Bot:", answers[7])
        continue

    if "chatbot" in user_lower:
        print("Bot:", answers[8])
        continue

    if "computer vision" in user_lower:
        print("Bot:", answers[9])
        continue

    # TF-IDF similarity for other questions
    user_vector = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vector, question_vectors)

    best_match = similarity.argmax()
    score = similarity[0][best_match]

    if score < 0.20:
        print("Bot: Sorry, I don't understand your question.")
    else:
        print("Bot:", answers[best_match])