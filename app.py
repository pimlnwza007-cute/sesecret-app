# app.py
from dash import Dash, html
import os


app = Dash()
app.layout = [html.Div(children="Hello, Dash!")]
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8050))
    app.run(host="0.0.0.0", port=port)