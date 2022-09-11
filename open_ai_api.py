# Get your API : https://beta.openai.com/

import openai as ai


ai.api_key = "Your API key"
text =  "Hey I hope you are doing great?"

resp = ai.Completion.create(
  model="text-davinci-002",
  prompt=f"Translate this into 1. French:\n\n{text}\n\n1.",
  temperature=0.3,
  max_tokens=100,
  top_p=1.0,
)
