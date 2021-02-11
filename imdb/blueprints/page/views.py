from flask import Blueprint, render_template
from imdb.blueprints.users.models import Top500
import datetime as dt

page=Blueprint('page', __name__, template_folder='templates')
@page.route('/')
def home():
    old=Top500.query.filter(Top500.date=="2021-02-02").limit(50).all()
    entries=Top500.query.order_by(Top500.date.desc(),Top500.rank.asc()).limit(50).all()
    delta=[]
    for entry in entries:
        for o in old:
            if entry.episode==o.episode:
                delta.append(o.rank-entry.rank)
    for d in delta:
        print(d)
    return render_template('home.html',entries=entries,delta=delta)

@page.route('/search/<string:search_query>')
def search(search_query):
    entries=Top500.query.filter(Top500.title.like(f"%{search_query}%")).all()
    return render_template('home.html',entries=entries)