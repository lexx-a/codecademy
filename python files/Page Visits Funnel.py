import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
					   
# print(visits.head())
# print(cart.head())
# print(checkout.head())
# print(purchase.head())

### Funnel for Cool T-Shirts Inc.
## visits_cart
visits_cart = pd.merge(visits, cart, how='left')
print(len(visits_cart.user_id))
print(len(visits_cart[visits_cart.cart_time.isnull()]))
first_step = float(len(visits_cart[visits_cart.cart_time.isnull()])) / len(visits_cart.user_id)
print('First step (visit_cart) = {0:.0%}'.format(first_step))
print

## cart_checkout
cart_checkout = pd.merge(cart, checkout, how='left')
print(len(cart_checkout.user_id))
print(len(cart_checkout[cart_checkout.checkout_time.isnull()]))
second_step = float(len(cart_checkout[cart_checkout.checkout_time.isnull()])) / len(cart_checkout.user_id)
print('Second step (cart_checkout) = {0:.0%}'.format(second_step))
print

## all steps of the funnel
all_data = visits.merge(cart, how='left')\
                .merge(checkout, how='left')\
                .merge(purchase, how='left')

# print(all_data.head())
checkouted = len(all_data[all_data.checkout_time.notnull()])
not_purchased = len(all_data[ (all_data.purchase_time.isnull()) & (all_data.checkout_time.notnull())])
print(checkouted)
print(not_purchased)

third_step = float(not_purchased) / checkouted
print('Third step (checkout_purchase) = {0:.0%}'.format(third_step))


### Average Time to Purchase
all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time

print(all_data.time_to_purchase)
print(all_data.time_to_purchase.mean())