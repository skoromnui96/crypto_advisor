import os
import requests

API_KEY = os.getenv("HF_API_KEY")
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def get_crypto_recommendation(symbol: str, price: float) -> str:
    prompt = f"""Ты финансовый советник. Дай краткую рекомендацию по криптовалюте {symbol}.
Текущая цена: ${price:.2f}. Укажи, стоит ли покупать, продавать или удерживать актив и почему."""

    data = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 200, "temperature": 0.7}
    }

    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"].strip()
        elif isinstance(result, dict) and "generated_text" in result:
            return result["generated_text"].strip()
        else:
            return str(result)
    else:
        return f"Ошибка Hugging Face: {response.status_code} — {response.text}"
