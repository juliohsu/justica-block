from ollama import chat
from pydantic import BaseModel

class Answer(BaseModel):
  answer: int

reasoning_trace = """
Problem: Solve for x in the equation 2x + 5 = 13

Let me work through this step by step:

First, I need to isolate the term with x. I'll subtract 5 from both sides:
2x + 5 - 5 = 13 - 5
2x = 8

Next, I'll divide both sides by 2 to solve for x:
2x ÷ 2 = 8 ÷ 2
x = 4

Let me verify this answer by substituting back into the original equation:
2(4) + 5 = 8 + 5 = 13 ✓

Ok, which means I got the correct answer, and I'm confident about my answer.
"""

response = chat(
  messages=[
    {
        "role": "system",
        "content": f"You are a helpful assistant that understands and translates text to JSON format according to the following schema. {Answer.model_json_schema()}"
    },
    {
      'role': 'user',
      'content': reasoning_trace,
    }
  ],
  model='Osmosis/Osmosis-Structure-0.6B',
  format=Answer.model_json_schema(),
)

answer = Answer.model_validate_json(response.message.content)
print(answer)