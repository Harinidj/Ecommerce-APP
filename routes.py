from flask import render_template, redirect, url_for, flash, request, current_app
from app import app, db, mail
from models import User, Product, Cart
from forms import RegistrationForm, LoginForm, QuantityForm
from flask_login import login_user, logout_user, login_required, current_user
from flask_mail import Message
from werkzeug.security import generate_password_hash, check_password_hash

# Home / Landing
@app.route('/')
def home():
    return render_template('home.html')

# Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed = generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=hashed)
        db.session.add(user)
        db.session.commit()
        flash('Account created! You rock, babe 😘', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Welcome back, sweetness!', 'success')
            return redirect(url_for('view_products'))
        else:
            flash('Oops, wrong creds. Try again? 😏', 'danger')
    return render_template('login.html', form=form)

# Logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('See ya soon, babe!', 'info')
    return redirect(url_for('home'))

# Products Listing
@app.route('/products')
def view_products():
    products = Product.query.all()
    return render_template('products.html', products=products)

# Add to Cart
@app.route('/add_to_cart/<int:product_id>')
@login_required
def add_to_cart(product_id):
    item = Cart.query.filter_by(user_id=current_user.id, product_id=product_id).first()
    if item:
        item.quantity += 1
    else:
        item = Cart(user_id=current_user.id, product_id=product_id)
        db.session.add(item)
    db.session.commit()
    flash('Added to cart! 🛒', 'info')
    return redirect(url_for('view_products'))

# View Cart
@app.route('/cart', methods=['GET', 'POST'])
@login_required
def view_cart():
    items = Cart.query.filter_by(user_id=current_user.id).all()
    form = QuantityForm()
    if request.method == 'POST':
        # handle quantity update or removal
        for item in items:
            q = request.form.get(f'qty_{item.id}', type=int)
            if q is not None:
                if q < 1:
                    db.session.delete(item)
                else:
                    item.quantity = q
        db.session.commit()
        return redirect(url_for('view_cart'))
    total = sum(item.product.price * item.quantity for item in items)
    return render_template('cart.html', items=items, total=total, form=form)

# Checkout & Email
@app.route('/checkout')
@login_required
def checkout():
    items = Cart.query.filter_by(user_id=current_user.id).all()
    total = sum(item.product.price * item.quantity for item in items)
    # Send Email
    msg = Message('Your Order Confirmation', sender=current_app.config['MAIL_DEFAULT_SENDER'], recipients=[current_user.email])
    msg.body = f"Hey {current_user.username},\n\n" \
               f"Thanks for your purchase! Your total was ₹{total:.2f}.\n" \
               "We’ll let you know when it ships.\n\n" \
               "Love,\nThe E‑Shop Team 💖"
    mail.send(msg)
    # Clear cart
    Cart.query.filter_by(user_id=current_user.id).delete()
    db.session.commit()
    flash('Order placed! Check your email, babe ❤️', 'success')
    return render_template('checkout.html', total=total)
