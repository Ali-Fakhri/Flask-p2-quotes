import os
from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


base_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = 'SomeStringforSecurityPurposes'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
Migrate(app, db)


#######################################
##### Building SQL Tables Section #####
#######################################


class Post(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.Text(50), nullable=False)
    auther = db.Column(db.Text(50), nullable=False)
    subject = db.Column(db.Text(300), nullable=False)

    def __init__(self, address, auther, subject):
        self.address = address
        self.auther = auther
        self.subject = subject


#######################################
##### Building SQL Tables Section #####
#######################################

#######################################
######## Building Forms Section #######
#######################################


class AddPost(FlaskForm):
    address = StringField("What's The Address of The Quote You'll Add Now?.")
    auther = StringField("What's You're Name or The Quote Maker's Name?.")
    subject = TextAreaField("You Can Write You're Favorite Quote Here..")
    submit_add = SubmitField("Save")


#######################################
######## Building Forms Section #######
#######################################


@app.route('/', methods=['GET', 'POST'])
def index():
    form = AddPost()
    posts = Post.query.order_by(Post.id).all()
    if form.validate_on_submit():
        address = form.address.data
        auther = form.auther.data
        subject = form.subject.data
        new_post = Post(address, auther, subject)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('index.html', posts=posts, form=form)

if __name__ == '__main__':
    app.run(debug=True)
