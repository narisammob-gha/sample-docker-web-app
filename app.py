```python
from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import socket
from datetime import datetime

HOST = "0.0.0.0"

# Read PORT from the environment; no hardcoded default.
port_value = os.environ.get("PORT")

if not port_value:
    raise RuntimeError("PORT environment variable is not set")

try:
    PORT = int(port_value)
except ValueError:
    raise RuntimeError("PORT must be a valid integer")

if not 1 <= PORT <= 65535:
    raise RuntimeError("PORT must be between 1 and 65535")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            body = b'{"status":"ok"}'
            self.send_response(200)
            self.send_header(
                "Content-Type",
                "application/json; charset=utf-8"
            )
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        hostname = socket.gethostname()
        server_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Docker Sample App</title>
  <style>
    body {{
      font-family: system-ui, sans-serif;
      max-width: 760px;
      margin: 4rem auto;
      padding: 0 1rem;
      line-height: 1.5;
    }}
    .card {{
      border: 1px solid #ddd;
      border-radius: 14px;
      padding: 1.5rem;
    }}
    code {{
      background: #f3f4f6;
      padding: .2rem .4rem;
      border-radius: 5px;
    }}
    .ok {{
      color: #137333;
      font-weight: 700;
    }}
  </style>
</head>
<body>
  <div class="card">
    <h1>It works! 🚀</h1>
    <p class="ok">The app is running inside a Docker container.</p>
    <p><strong>Container hostname:</strong>
       <code>{hostname}</code></p>
    <p><strong>Server time:</strong>
       <code>{server_time}</code></p>
    <p><strong>Application port:</strong>
       <code>{PORT}</code></p>
    <p>Try the health endpoint:
       <a href="/health"><code>/health</code></a></p>
  </div>
</body>
</html>"""

        body = html.encode("utf-8")
        self.send_response(200)
        self.send_header(
            "Content-Type",
            "text/html; charset=utf-8"
        )
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        print(
            f"{self.address_string()} - {format % args}",
            flush=True
        )


if __name__ == "__main__":
    print(f"Starting web app on {HOST}:{PORT}", flush=True)
    HTTPServer((HOST, PORT), Handler).serve_forever()
```
