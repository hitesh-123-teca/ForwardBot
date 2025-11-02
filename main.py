# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper

from bot import Bot
import threading, http.server, socketserver, asyncio

# --- Run the bot with correct event loop ---
def run_bot():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    app = Bot()
    app.run()

# --- Dummy web server for Koyeb health check (port 8080) ---
def run_server():
    PORT = 8080
    with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
        httpd.serve_forever()

# --- Run both together ---
threading.Thread(target=run_server, daemon=True).start()
threading.Thread(target=run_bot).start()

# Keep main thread alive
while True:
    pass
