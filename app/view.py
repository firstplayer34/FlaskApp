from app import app
from flask import render_template, flash, redirect
from forms import TaskForm

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/task',methods=['GET','POST'])
def task():
    form = TaskForm()
    if form.validate_on_submit():
        flash('Task number:{}'.format(form.taskNumber.data))
        return redirect('/index');
    return render_template("task.html",title = "Выбор задания", form = form)