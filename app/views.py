from flask import request, render_template, flash, redirect, url_for
from app import app
from .forms import TagForm

@app.route('/')
@app.route('/index')
def index():
    state = 'dev' # fake user
    return render_template('index.html',
                           title='tagbar',
                           state=state)

@app.route('/query', methods=['GET', 'POST'])
def login():
    form = TagForm()
    if form.validate_on_submit():
        flash("Provided tag: %s, remember_me=%s'" %
            (form.tag.data, str(form.remember_me.data)))
        return redirect(url_for('results',tag=form.tag.data))
    return render_template('query.html',
                           title='Tag Search',
                           form=form)

@app.route('/results')
def results():
    state = 'dev'
    return render_template('results.html',
                           title='tagbar',
                           hashtag=request.args.get('tag'))
