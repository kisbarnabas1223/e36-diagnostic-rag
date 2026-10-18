import ollama

print("Sending the question to the local AI...")

response = ollama.chat(model='qwen2.5:7b', messages=[
  {
    'role': 'user',
    'content': 'What is the meaning of the P0171 OBD error code in two sentences',
  },
])

# A válasz kiíratása
print("\nAI response:")
print(response['message']['content'])