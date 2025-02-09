import openai
import os

openai.api_key = "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"

def generate_response(intent, entities, user_text):
    prompt = (
        f"User query: '{user_text}'.\n"
        f"Intent: {intent}.\n"
        f"Entities: {entities}.\n"
        "Provide a friendly, helpful response."
    )
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7,
        )

        answer = response.choices[0].message['content'].strip()
        return answer
    except Exception as e:
        print("Error generating response:", e)
        return "I'm sorry, I couldn't process your request at this time."
