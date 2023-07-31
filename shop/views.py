
from itertools import product
from django.shortcuts import get_object_or_404, redirect, render
from .models import CartItem, product 

# add_to_cart
def add_to_cart(request, product_id):
    selected_product = get_object_or_404(product, id=product_id)
    
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if quantity < 1:
            quantity = 1
    
        # Get the cart from the session or create an empty cart if it doesn't exist
        cart = request.session.get('cart', {})
        
        # Update the quantity if the product is already in the cart, otherwise add it
        cart[product_id] = cart.get(product_id, 0) + quantity
        
        # Save the cart back to the session
        request.session['cart'] = cart
        # Calculate the total quantity of items in the cart
        total_items = sum(cart.values())
        print(f"Total quantity of items in the cart: {total_items}")

    # Redirect to the product details page after adding to cart
    return redirect('shopping_cart')




def product_detail(request, product_id):
    product_obj = get_object_or_404(product, id=product_id)
    

    return render(request, 'shop/products_details.html', {'product': product_obj})


# Remove item from cart view
def remove_from_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        cart = request.session.get('cart', {})
        if product_id in cart:
            del cart[product_id]
            request.session['cart'] = cart

    return redirect('shopping_cart')


def shopping_cart(request):
    cart = request.session.get('cart', {})
    products_in_cart = []

    total_price = 0

    for product_id, quantity in cart.items():
        product_obj = get_object_or_404(product, id=product_id)
        total_price += product_obj.price * quantity
        products_in_cart.append({
            'product': product_obj,
            'quantity': quantity,
            'total_price': product_obj.price * quantity,
        })

    context = {
        'products_in_cart': products_in_cart,
        'total_price': total_price,
    }

    return render(request, 'shop/shopping_cart.html', context)


def process_order(request):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        # Process the order and handle the payment option here
        payment_option = request.POST.get('payment_option')
        # Implement logic for different payment options here

        # Clear the cart after successful checkout
        request.session['cart'] = {}

        # Show a success message (You can customize this message as needed)
        message = 'Order placed successfully!'

        return render(request, 'shop/order_confirmation.html', {'message': message})
    else:
        return redirect('shopping_cart')


def billing_address(request):
    # Process the form submission and save the billing address if needed
    if request.method == 'POST':
        # Handle form data and save the billing address
        # (You can use Django forms for this)

        # Redirect to the final checkout page
        return redirect('final_checkout')

    return render(request, 'shop/billing_address.html')

def final_checkout(request):
    # Perform final checkout process (e.g., order confirmation)
    # You can access the cart items and billing address from the session here

    # Clear the cart after final checkout
    request.session['cart'] = {}

    return render(request, 'shop/final_checkout.html')


def index(request):
    products_by_category = {}  # Dictionary to hold products grouped by category
    categories = [choice[0] for choice in product._meta.get_field('category').choices]

    for category in categories:
        products = product.objects.filter(category=category)[:4]  # Assuming you want to display only 4 products per category
        products_by_category[category] = products

        # Calculate total items in the cart
        cart = request.session.get('cart', {})
        total_items = sum(cart.values())
        

    context = {
        'products_by_category': products_by_category,
        'total_items': total_items,
    }

    return render(request, 'shop/index.html', context)


def aboutus(request):
  return render(request, 'shop/about.html')

def contactus(request):
      return render(request, 'shop/contact.html')

def tracker(request):
    return render( request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def productview(request):
    products = product.objects.all()
    return render(request, 'shop/products.html', {'products': products})

# views.py

# ... (previous views and imports)

def checkout(request):
    cart = request.session.get('cart', {})
    products_in_cart = []

    total_price = 0

    for product_id, quantity in cart.items():
        product_obj = get_object_or_404(product, id=product_id)
        total_price += product_obj.price * quantity
        products_in_cart.append({
            'product': product_obj,
            'quantity': quantity,
            'total_price': product_obj.price * quantity,
        })

    context = {
        'products_in_cart': products_in_cart,
        'total_price': total_price,
    }

    return render(request, 'shop/checkout.html', context)

# views.py
def calculate_total_items_in_cart(cart):
    return sum(cart.values())

def some_view(request):
    # Calculate or fetch the total_items value
    cart = request.session.get('cart', {})

    # Calculate the total number of items in the cart
    total_items = calculate_total_items_in_cart(cart)


    # Your other view logic

    context = {
        # Your other context variables
        'total_items': total_items,
    }

    return render(request, 'shop/basic.html', context)
