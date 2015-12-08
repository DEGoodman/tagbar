from ast import literal_eval as make_tuple
from flask import request, render_template, flash, redirect, url_for
from app import app
from .forms import TagForm
from .get_ig_photos import Setup
from .analyzer import Analyze
from .palletizer import Palletize
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
        pcols = [cssmaker.make(cols)]
        print("cols:")
        print(cols)
        print("pcols:")
        print(pcols)
        return redirect(url_for('results',tag=form.tag.data, main_cols=cols, p_cols=pcols[:]))
    return render_template('query.html',
                           title='Tag Search',
                           form=form)

@app.route('/results')
def results():
    state = 'dev'
    cols = request.args.get('main_cols')
    tups = make_tuple(cols)
    tlist = []
    hlist = []
    for t in tups:
        tlist.append(t[1])
        hlist.append('%02x%02x%02x' % t[1])
    primcol = tlist[0]
    hcol = '%02x%02x%02x' % primcol

    pallete = request.args.get('p_cols')
    print("results pallete: %s" % pallete)
    # pcol = pallete
    # print('pcol: %s' % pcol)
    return render_template('results.html',
                           title='tagbar',
                           hashtag=request.args.get('tag'),
                           colors=request.args.get('main_cols'),
                           primary=primcol,
                           hexcol=hcol,
                           hcs = hlist,
                           pcl=pallete)
