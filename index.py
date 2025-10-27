from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from openai import OpenAI
import os

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def index():
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    message = """
    You are on my first production website. Please say hello to the user.
    """
    messages = [{"role": "user", "content": message}]
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    reply = response.choices[0].message.content.replace("\n", "<br>")
    html_content = (
        f"""
        <html>
        <body>
        <h1>Hello, Welcome to my website!</h1>
        <p>{reply}</p>
        </body>
        </html>
        """
    )
    return html_content
