import africastalking
from flask_restful import Resource, reqparse
from app.models import Customer, Order
from app import db

# Customer Resource
class CustomerResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help="Customer name cannot be blank!")
    parser.add_argument('code', type=str, required=True, help="Customer code cannot be blank!")

    def post(self):
        data = CustomerResource.parser.parse_args()
        customer = Customer(name=data['name'], code=data['code'])
        db.session.add(customer)
        db.session.commit()
        return {'message': 'Customer created successfully'}, 201

# Order Resource
class OrderResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('item', type=str, required=True, help="Item cannot be blank!")
    parser.add_argument('amount', type=float, required=True, help="Amount cannot be blank!")
    parser.add_argument('time', type=str, required=True, help="Time cannot be blank!")
    parser.add_argument('customer_id', type=int, required=True, help="Customer ID cannot be blank!")

    def post(self):
        data = OrderResource.parser.parse_args()
        order = Order(item=data['item'], amount=data['amount'], time=data['time'], customer_id=data['customer_id'])
        db.session.add(order)
        db.session.commit()
        # Add SMS sending here
        return {'message': 'Order created successfully'}, 201

# Initialize Africa's Talking
africastalking.initialize('username', 'atsk_e14469112397365499081b85dea387f1486c273b468cd79fe6f6d0caad9bb7525991c6a0')
sms = africastalking.SMS

def send_sms(message, recipient):
    response = sms.send(message, [recipient])
    print(response)

# Modify Order Resource post method
def post(self):
    data = OrderResource.parser.parse_args()
    order = Order(item=data['item'], amount=data['amount'], time=data['time'], customer_id=data['customer_id'])
    db.session.add(order)
    db.session.commit()
    
    # Fetch customer and send SMS
    customer = Customer.query.get(data['customer_id'])
    send_sms(f'Order added: {order.item} for {order.amount}', customer.code)
    
    return {'message': 'Order created successfully and SMS sent'}, 201
