def chatbot_response(user_input):
    if "hi" in user_input or "hi" in user_input:
        return "Hey there! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm doing fantastic, thanks for asking! How about you?"
    elif "your name" in user_input:
        return "I'm Malya! hazellenuts' little brother gave me this awesome name. What's yours?"
    elif "my name" in user_input:
        return "that's a beautiful name!"
    elif "thank you" in user_input or "thanks" in user_input:
        return "anytime!"
    else:
        return "Hmm, I'm not sure I understand. Could you rephrase that or ask something else?"

print("Simple Chatbot: Malya")
print("Malya: Hi! how can I help you today? Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()
    print("")
    if user_input == "bye":
        print("Malya: Goodbye, Have a great day!")
        break
    else:
        response = chatbot_response(user_input)
        print(f"Malya: {response}")

print("—hazellenuts")