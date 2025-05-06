
# Telegram Crypto Advisor Bot

📈 Бот отправляет рекомендации по покупке/продаже криптовалют с использованием Binance API и ChatGPT.

## 🚀 Развертывание на Render

1. Создайте репозиторий на GitHub и загрузите туда файлы.
2. Перейдите на [https://dashboard.render.com/](https://dashboard.render.com/)
3. Нажмите **"New" → "Web Service"** → выберите GitHub репозиторий.
4. Выберите:
   - Type: `Background Worker`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python bot.py`
5. В разделе "Environment" добавьте переменные:
   - `BOT_TOKEN` — токен Telegram-бота
   - `OPENAI_API_KEY` — ключ OpenAI

## 🧪 Тестирование

Напиши в Telegram:

```
/recommend BTC
```

И получи текстовую рекомендацию от ChatGPT на основе текущей цены BTC с Binance.
