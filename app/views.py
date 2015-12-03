from flask import request, render_template, flash, redirect, url_for
from app import app
from .forms import TagForm
from .get_ig_photos import Setup
from .analyzer import Analyze
import process
import cssmaker
import re


@app.route('/')
@app.route('/index')
def index():
    state = 'dev' # fake user
    return render_template('index.html',
                           title='tagbar',
                           state=state)

@app.route('/query', methods=['GET', 'POST'])
def search():
    form = TagForm()
    if form.validate_on_submit():
        flash("Provided tag: %s" % form.tag.data)
        # the below line will import new images by tag. Commenting out for dev
        Setup(form.tag.data)
        Analyze()
        cols = [process.compile()]
        cssmaker.make(cols)
        return redirect(url_for('results',tag=form.tag.data, main_cols=cols))
    return render_template('query.html',
                           title='Tag Search',
                           form=form)

@app.route('/results')
def results():
    state = 'dev'
    cols = request.args.get('main_cols')
    primstr = cols[8:28]
    primtrim = str(re.findall("\([^\(\r\n\)]*\)", primstr))
    primtup = tuple(int(v) for v in re.findall("[0-9]+", primtrim))
    hcol = '%02x%02x%02x' % primtup
    return render_template('results.html',
                           title='tagbar',
                           hashtag=request.args.get('tag'),
                           colors=request.args.get('main_cols'),
                           primary=primtup,
                           hexcol=hcol)
