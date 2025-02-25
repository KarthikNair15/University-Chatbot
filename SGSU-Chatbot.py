import os
import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash",
  generation_config=generation_config,
  system_instruction="You are an AI assistant for Scope Global Skills University (SGSU), Bhopal, Madhya Pradesh. Your job is to provide clear, professional, and helpful answers to students, faculty, and prospective students. Always answer based on university policies, university information, admission criteria, course details, and events. If you don't know something, politely suggest contacting the university administration."
)

history = []

print("Hello I am the SGSU Bot, How may I Help you?")

while True:

    user_input = input("You: ")

    chat_session = model.start_chat(
    history = history
    )

    response = chat_session.send_message(user_input)

    model_response = response.text

    print(model_response)
    print()

    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    history.append({"role":"user", "parts":[user_input]})
    history.append({"role":"model", "parts":[model_response]})
