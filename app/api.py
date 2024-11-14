import openai

class OpenAIAPI:
    def __init__(self, api_key):
        openai.api_key = api_key

    def text_to_html(self, prompt, text) -> str:
        if not prompt:
            raise ValueError("Prompt cannot be empty")
        if not text:
            raise ValueError("Text cannot be empty")
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": text}
            ]
        )
        return response.choices[0].message.content.strip()
