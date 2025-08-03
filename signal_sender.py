import requests

print("🔧 Бот запускается...")


# === Конфигурация ===
import os
import requests

# === Конфигурация ===
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
PARSE_MODE = "Markdown"

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
        
if __name__ == "__main__":
    send_signal()