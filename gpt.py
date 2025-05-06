
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_crypto_recommendation(symbol: str, price: float) -> str:
    prompt = f"""
    Ты финансовый советник. Дай краткую рекомендацию по криптовалюте {symbol}.
    Текущая цена: ${price:.2f}.
    Укажи, стоит ли покупать, продавать или удерживать актив и почему.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response['choices'][0]['message']['content'].strip()
