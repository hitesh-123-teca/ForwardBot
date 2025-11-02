# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper

from bot import Bot
import threading, http.server, socketserver

# --- Run the bot normally ---
app = Bot()

def run_bot():
    app.run()

# --- Dummy web server for Koyeb health check (port 8080) ---
def run_server():
    PORT = 8080
    with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
        httpd.serve_forever()

# --- Run both threads together ---
threading.Thread(target=run_server, daemon=True).start()
threading.Thread(target=run_bot).start()

# Keep main thread alive
while True:
    pass
