import os
from openai import OpenAI

client = OpenAI()  # API-ключ берется автоматически из переменной окружения

def get_crypto_recommendation(symbol: str, price: float) -> str:
    prompt = f"""
    Ты финансовый советник. Дай краткую рекомендацию по криптовалюте {symbol}.
    Текущая цена: ${price:.2f}.
    Укажи, стоит ли покупать, продавать или удерживать актив и почему.
    """

    response = client.chat.completions.create(
        model="gpt-4",  # или "gpt-3.5-turbo"
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content.strip()
