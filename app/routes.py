from app import app
from flask import render_template
from dataLink import DataLink
from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
    data = DataLink()
    now = datetime.now()
    accounts=[]
    for i in range(1,data.rowCount()+1):
        accounts.append(data.getRow(i))
    return render_template("index.html", accounts=accounts, year=now.year)