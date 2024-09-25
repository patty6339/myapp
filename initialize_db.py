from app import app, db
from app.models import Customer, Order

with app.app_context():
    db.create_all()
