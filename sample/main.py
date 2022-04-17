from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from starlette.middleware.cors import CORSMiddleware  # 追加
import pandas as pd


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,   # 追記により追加
    allow_methods=["*"],      # 追記により追加
    allow_headers=["*"]       # 追記により追加
)

csv_data_1 = pd.read_csv("data1.csv")
csv_data_2 = pd.read_csv("data2.csv")

print(csv_data_1)


@app.get("/items/", response_class=HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """


@app.get("/users")
def read_users():
    return {"id": 1, "name": "Revenue&Profit"}


@app.get("/data_1")
async def store_data():
    s_data = [
        {"store": "A", "month": 202010, "members": 300, "male": 150, "female": 150},
        {"store": "A", "month": 202011, "members": 400, "male": 200, "female": 200},
        {"store": "A", "month": 202012, "members": 500, "male": 250, "female": 250},
        {"store": "B", "month": 202010, "members": 800, "male": 500, "female": 300},
        {"store": "B", "month": 202011, "members": 500, "male": 300, "female": 200},
        {"store": "B", "month": 202012, "members": 700, "male": 200, "female": 500},
        {"store": "C", "month": 202010, "members": 650, "male": 350, "female": 300},
        {"store": "C", "month": 202011, "members": 1000, "male": 450, "female": 550},
        {"store": "C", "month": 202012, "members": 1200, "male": 550, "female": 650}
    ]
    return s_data


@app.get("/data_2")
async def store_data():
    s_data = [
        {"store": "A", "month": 202010, "members": 300, "male": 50, "female": 150},
        {"store": "A", "month": 202011, "members": 400, "male": 0, "female": 200},
        {"store": "A", "month": 202012, "members": 500, "male": 50, "female": 250},
        {"store": "B", "month": 202010, "members": 300, "male": 00, "female": 300},
        {"store": "B", "month": 202011, "members": 200, "male": 0, "female": 200},
        {"store": "B", "month": 202012, "members": 900, "male": 0, "female": 500},
        {"store": "C", "month": 202010, "members": 100, "male": 50, "female": 0},
        {"store": "C", "month": 202011, "members": 300, "male": 50, "female": 0},
        {"store": "C", "month": 202012, "members": 1000, "male": 50, "female": 0}
    ]
    return s_data
