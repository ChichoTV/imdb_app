from flask import Blueprint, render_template
from imdb.blueprints.users.models import Top500, Logs
import datetime as dt
from sqlalchemy import or_
from collections import Counter

page=Blueprint('page', __name__, template_folder='templates')

@page.route('/')
def home():
    dates=Logs.query.order_by(Logs.date.desc()).limit(2).all()
    this_week=dates[0].date
    last_week=dates[1].date
    old_entries=Top500.query.filter(Top500.date==last_week).all()
    newest_entries=Top500.query.filter(Top500.date == this_week).order_by(Top500.rank.asc()).all()
    delta=[]
    for new in newest_entries:
        item={
            'title': new.title,
            'change':'New'
        }
        for old in old_entries:
            if old.episode==new.episode and old.title==new.title:
                item['change']= old.rank-new.rank
                delta.append(item)
    def title(obj):
        return obj.title
    mytuple=tuple(map(title, newest_entries))
    counts= Counter(mytuple).most_common(5)
    print(len(delta))
    return render_template('home.html',entries=newest_entries[:50], counts=counts, delta=delta[:50])

# @page.route('/')
# def home():
#     old=Top500.query.filter(Top500.date=="2021-02-02").limit(50).all()
#     entries=Top500.query.order_by(Top500.date.desc(),Top500.rank.asc()).limit(50).all()
#     delta=[]
#     for entry in entries:
#         for o in old:
#             if entry.episode==o.episode:
#                 delta.append(o.rank-entry.rank)
#     for d in delta:
#         print(d)
#     return render_template('home.html',entries=entries,delta=delta)

@page.route('/search/<string:search_query>')
def search(search_query):
    dates=Logs.query.order_by(Logs.date.desc()).limit(2).all()
    this_week=dates[0].date
    # last_week=dates[1].date
    newest_entries=Top500.query.filter(Top500.date == this_week).order_by(Top500.rank.asc()).all()
    def title(obj):
        return obj.title
    mytuple=tuple(map(title, newest_entries))
    counts= Counter(mytuple).most_common(5)
    search_results=Top500.query.filter(or_(Top500.title.like(f"%{search_query}%"),Top500.episode.like(f"%{search_query}%")),Top500.date==this_week).all()
    return render_template('home.html',entries=search_results, counts=counts)