import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def get_crypto_recommendation(symbol: str, pr: float) -> str:
    prompt = f"""
    Ты финансовый советник. Дай краткую рекомендацию по криптовалюте {symbol}.
    Текущая цена: ${price:.2f}.
    Укажи, стоит ли покупать, продавать или удерживать актив и почему.
    """

    response = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content.strip()
