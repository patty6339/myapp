from app import app
from flask_restful import Api
from app.resources import CustomerResource, OrderResource

api = Api(app)
api.add_resource(CustomerResource, '/customers')
api.add_resource(OrderResource, '/orders')
