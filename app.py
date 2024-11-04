from flask import Flask, render_template, request
import db

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():

    name = ''
    if request.method == 'GET':
        name = request.args.get('name','')

    if request.method == 'POST':
        db.add_comment(request.form['comment'])

    search_query = request.args.get('q')

    comments = db.get_comments(search_query)

    return render_template('index.html',
                           name=name,
                           comments=comments,
                           search_query=search_query)
