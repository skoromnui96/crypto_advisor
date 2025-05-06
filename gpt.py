import os
import requests

API_KEY = os.getenv("OPENROUTER_API_KEY")
API_URL = "https://openrouter.ai/api/v1/chat/completions"

def get_crypto_recommendation(symbol: str, price: float) -> str:
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openchat/openchat-7b",
        "messages": [
            {"role": "user", "content": f"""
            Ты финансовый советник. Дай краткую рекомендацию по криптовалюте {symbol}.
            Текущая цена: ${price:.2f}.
            Укажи, стоит ли покупать, продавать или удерживать актив и почему.
            """}
        ]
    }

    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"].strip()
    else:
        return f"Ошибка OpenRouter: {response.status_code} — {response.text}"
