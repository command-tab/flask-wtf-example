from flask import Flask, render_template
from sqlalchemy import func


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
app.config['SECRET_KEY'] = 'hunter2'

# Configure Flask-SQLAlchemy
from app.models import db
db.init_app(app)

# Import models
from app.models.category import Category

# Import forms
from app.forms.item import ItemForm


@app.route('/')
def index():
    # Build in-memory schema
    db.drop_all()
    db.create_all()
    db.session.commit()

    # Populate some data
    names = ['Movies', 'TV Shows', 'Games']
    for name in names:
        category = Category(name)
        db.session.add(category)
    db.session.commit()

    # Query categories
    categories = Category.query.order_by(func.lower(Category.name).asc()).all()

    # Setup an Item form, which allows you to select a category for the item.
    # (There's no item saving logic)
    form = ItemForm()

    return render_template('index.html', categories=categories, form=form)
