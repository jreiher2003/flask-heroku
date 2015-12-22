#################
#### imports ####
#################

from project import db
from project.models import BlogPost, User
from forms import MessageForm
from flask import render_template, Blueprint, request, flash, redirect, url_for
from flask.ext.login import login_required, current_user


################
#### config ####
################

home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)


################
#### routes ####
################

# use decorators to link the function to a url
@home_blueprint.route('/', methods=['GET', 'POST'])
@login_required
def home():
    error = None
    form = MessageForm(request.form)
    if form.validate_on_submit():
        new_message = BlogPost(
            form.title.data,
            form.description.data,
            current_user.id
        )

        db.session.add(new_message)
        db.session.commit()
        flash('New entry was successfully posted. Thanks.', 'bg-success')
        return redirect(url_for('home.home'))
    else:
        # current_u = current_user()
        posts = db.session.query(BlogPost).all()
        u_posts = db.session.query(User,BlogPost).filter(current_user.id==BlogPost.author_id)
        return render_template(
            'index.html', posts=posts, form=form, u_posts=u_posts, error=error)


@home_blueprint.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template