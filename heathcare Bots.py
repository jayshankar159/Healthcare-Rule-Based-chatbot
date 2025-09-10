import random
import spacy

nlp = spacy.load("en_core_web_sm")


intents = {
    "intents": [
        {
            "tag": "greeting",
            "patterns": ["hello", "hi", "hey", "good morning", "good evening"],
            "responses": ["Hello! Welcome to Jay Hospital. How can I assist you today?"]
        },
        {
            "tag": "hours",
            "patterns": ["what are visiting hours", "when can I visit", "hospital timings"],
            "responses": ["Visiting hours are from 9 AM to 7 PM every day."]
        },
        {
            "tag": "appointment",
            "patterns": ["book appointment", "schedule doctor visit", "appointment with doctor"],
            "responses": ["Sure, please provide the department (Cardiology, Orthopedics, Pediatrics) and your preferred time."]
        },
        {
            "tag": "emergency",
            "patterns": ["emergency", "ambulance", "urgent help"],
            "responses": ["For emergencies, please call our helpline at 102 immediately or rush to the Emergency Ward."]
        },
        {
            "tag": "departments",
            "patterns": ["what departments are there", "specialists available", "doctors in hospital"],
            "responses": ["We have departments like Cardiology, Orthopedics, Pediatrics, Neurology, and General Medicine."]
        },
        {
            "tag": "insurance",
            "patterns": ["do you accept insurance", "cashless treatment", "medical insurance"],
            "responses": ["Yes, we accept major health insurance providers for cashless treatment."]
        },
        {
            "tag": "goodbye",
            "patterns": ["bye", "goodbye", "exit", "quit"],
            "responses": ["Goodbye! Take care of your health."]
        }
    ]
}

def chatbot_response(user_input):
    doc = nlp(user_input.lower())
    user_tokens = [token.lemma_ for token in doc]

    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            pattern_doc = nlp(pattern.lower())
            pattern_tokens = [token.lemma_ for token in pattern_doc]
            if any(word in user_tokens for word in pattern_tokens):
                return random.choice(intent["responses"])

    return "I'm sorry, I didn’t understand that. Can you please rephrase?"


print("🏥 Healthcare Chatbot: Hello! Welcome to Jay Hospital. Type 'quit' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit", "bye"]:
        print("🏥 Chatbot:", chatbot_response(user_input))
        break
    print("🏥 Chatbot:", chatbot_response(user_input))