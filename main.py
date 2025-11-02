# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper

from bot import Bot
import threading, http.server, socketserver

# --- Dummy web server for Koyeb health check (port 8080) ---
def run_server():
    PORT = 8080
    with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
        httpd.serve_forever()

# Start web server in background
threading.Thread(target=run_server, daemon=True).start()

# --- Run the bot normally in main thread ---
app = Bot()
app.run()
