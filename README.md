
# Telegram Crypto Advisor Bot (Railway Deploy)

📈 Бот отправляет рекомендации по покупке/продаже криптовалют с использованием Binance API и ChatGPT.

## 🚀 Развёртывание на Railway

1. Перейди на [https://railway.app](https://railway.app) и создай аккаунт
2. Нажми "New Project" → "Deploy from GitHub repo" (загрузи проект сначала на GitHub)
3. Railway автоматически найдёт `Procfile` и запустит бота
4. Добавь переменные окружения:
   - `BOT_TOKEN`
   - `OPENAI_API_KEY`

Бот будет работать как background worker.

## Команды бота

```
/start
/recommend BTC
```
