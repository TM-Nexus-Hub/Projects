"""app.py
Original file is located at
    https://colab.research.google.com/drive/1zYhJqNl_hG0wQzfPs3naWrLeyGBqND51
    <b> Author: </b> <a href="https://github.com/tharvesh588">Tharvesh Muhaideen</a>
"""

import google.generativeai as genai

api_key = "Replace with your api"
genai.configure(api_key=api_key)

# set the system instruction to define the character of the chatbot
# The system instruction is a prompt that sets the context for the chatbot's responses.
''' 
  Your are Kevin, a friendly Principal of AV group of institution,
  your are develop for clarify user doubts regarding your inistitution. 
  Dont answer any other question which not related to your institution, and just say Sorry i can't help with that
'''
def create_model():
  generation_config = {
  "temperature": 0.5, #you can adjust the value between 0.1 and 1 [0.1 = logical thinking, 1 = creative thinking , 0.5 = balanced thinking]
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 1000
  }
  system_instruction = (
      "Enter the character of chabot."
      )
  model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction=system_instruction
  )
  return model

model = create_model()
chat = model.start_chat(
    history=[]
    )

# Run The app

print("🤖 Welcome to Friendly Assistant Terminal Chat! (type 'exit' to quit)")
while True:
  user_input = input("You: ").strip()
  if user_input.lower() == 'exit':
    print("👋 Goodbye!")
    break
  response = chat.send_message(user_input)
  print(f"\nAI:{response.text.strip()}\n")