import requests

# === Конфигурация ===
BOT_TOKEN = "8403528772:AAEq_sv71CtKGh5Xp1tHwy8Qb3S7-pnmORc"
CHAT_ID = "-1002580812908"  # ID твоего канала или чата
PARSE_MODE = "Markdown"  # или "HTML"

# === Пример сигнала ===
def send_signal():
    message = """
📈 *СИГНАЛ НА ВХОД: BTC/USDT – длинная позиция*

🕓 *Таймфрейм:* 4H  
📍 *Цена входа:* $113,200  
📊 *Обоснование:*  
- Тренд восходящий (EMA-13 выше EMA-26)  
- MACD Histogram разворачивается вверх  
- Зеленый бар Impulse System  
- Поддержка объёмом

🎯 *Цели:*  
1. $115,600  
2. $117,800  
3. $121,000

🛑 *Стоп-лосс:* $111,700
"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": PARSE_MODE
    }

    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("✅ Сигнал успешно отправлен.")
    else:
        print(f"❌ Ошибка: {response.status_code} — {response.text}")

# === Запуск ===
if __name__ == "__main__":
    send_signal()
