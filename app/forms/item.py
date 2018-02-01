from flask_wtf import FlaskForm
from sqlalchemy import func
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app.models.category import Category


def all_categories():
    return Category.query.order_by(func.lower(Category.name).asc()).all()


class ItemForm(FlaskForm):
    category = QuerySelectField('Category', query_factory=all_categories, get_label='name')
