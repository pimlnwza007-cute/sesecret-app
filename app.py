# app.py
from dash import Dash, dcc, html, Input, Output, State
import os
from dotenv import load_dotenv

load_dotenv()
APP_PASSWORD = os.getenv("APP_PASSWORD")
SECRET_MESSAGE = os.getenv("SECRET_MESSAGE")

app = Dash()
app.layout = [
    dcc.Input(id="password", type="password"),
    html.Button("Submit", id="btn-submit"),
    html.Div(id="output"),
]


@app.callback(
    Output("output", "children"),
    Input("btn-submit", "n_clicks"),
    State("password", "value"),
)
def check_password(n_clicks, pw):
    if not n_clicks:
        return ""
    if pw == APP_PASSWORD:
        return SECRET_MESSAGE
    if pw == None:
        return "Password not set"
    return "Wrong password"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8050))
    app.run(host="0.0.0.0", port=port)