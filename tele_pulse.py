"""
TelePulse — Automated Telegram Alert Bot
Usage:
    python tele_pulse.py --token YOUR_BOT_TOKEN --chat-id YOUR_CHAT_ID
"""

import sys
import time
import argparse
import requests

def send_telegram_alert(token: str, chat_id: str, message: str):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message, "parse_mode": "Markdown"}
    print(f"[TelePulse] Dispatching alert to Chat ID {chat_id}...")
    try:
        resp = requests.post(url, json=payload, timeout=5)
        if resp.ok:
            print("[SUCCESS] Alert delivered via Telegram API!")
        else:
            print(f"[ERR] Telegram API response: {resp.status_code}")
    except Exception as e:
        print(f"[ERR] Failed to send alert: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TelePulse Alert Bot")
    parser.add_argument("--token", default="MOCK_BOT_TOKEN", help="Telegram Bot Token")
    parser.add_argument("--chat-id", default="MOCK_CHAT_ID", help="Telegram Chat ID")
    parser.add_argument("--msg", default="[Alert] TelePulse engine initialized successfully!", help="Message body")
    args = parser.parse_args()
    send_telegram_alert(args.token, args.chat-id, args.msg)
