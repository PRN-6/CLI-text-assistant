
import os
from google import genai

# Create client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

conversation = [] # conversation history like a memory

print("🤖 Gemini AI Text Assistant (type 'exit' to quit)")

while True:
    user_input = input("\nYou: ")

    if user_input.lower() in ["exit", "quit"]:
        print("AI: Goodbye 👋")
        break
    
    # add user input to conversation
    conversation.append({
        "role" : "user",
        "parts" : [{"text": user_input}]
    })

    #generate response
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=conversation,
        config={
            "temperature": 0.7,
            "max_output_tokens": 1000 # based on the output toeken limit the responce will be cut off
        }
    )

    print("AI:", response.text)

    # add model response to conversation
    conversation.append({
        "role": "model",
        "parts" : [{"text": response.text}]
    })

    print(conversation)