# import google.generativeai as genai
# import os

# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# # def chat_with_ai(user_input):
# #     responce = client.chat.completions.create(
# #         model="gemini-1.5-flash-exp",
# #         messages=[
# #             {"role": "system" , "content": "you are a helpful assistant."},
# #             {"role": "user", "content" : user_input}
# #         ],
# #         temperature=0.7
# #     )
# #     return responce.choices[0].message.content


# # configure the model

# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# model = genai.GenerativeModel(
#     model="gemini-1.5-flash",
#     generation_config={
#         "temperature": 0.7,
#         "max_output_tokens": 200
#     }
# )
# while True:
#     user_input = input("You:")
#     if user_input.lower() == "exit":
#         break

#     try:
#         ai_response = model.generate_content(user_input)
#         print("AI:", ai_response.text)
#     except Exception as e:
#         print("Error:", str(e))

# import os
# from google import genai

# # Create Gemini client
# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# print("🤖 Gemini AI Text Assistant (type 'exit' to quit)")

# while True:
#     user_input = input("\nYou: ")

#     if user_input.lower() in ["exit", "quit"]:
#         print("AI: Goodbye 👋")
#         break

#     response = client.models.generate_content(
#         model="gemini-1.0-pro",
#         contents=user_input,
#         config={
#             "temperature": 0.7,
#             "max_output_tokens": 200
#         }
#     )

#     print("AI:", response.text)

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