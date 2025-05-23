# seed.py

from app import app, db
from models import Product

def seed():
    with app.app_context():
        # Optional: clear old data
        # db.session.query(Product).delete()
        # db.session.commit()

        products = [
            # CLOTHES
            {"name": "Oversized Hoodie", "price": 1599.00, "description": "Comfy and stylish for chilly days.", "image_file": "hoodie.jpg"},
            {"name": "Vintage Graphic Tee", "price": 599.99, "description": "Soft cotton with retro print.", "image_file": "vintage_tee.jpg"},
            {"name": "Ripped Skinny Jeans", "price": 699.99, "description": "Distressed denim, slim fit.", "image_file": "skinny_jeans.jpg"},
            {"name": "Casual Flannel Shirt", "price": 299.99, "description": "Plaid flannel, ideal for layering.", "image_file": "flannel.jpg"},
            {"name": "Linen Summer Dress", "price": 498.00, "description": "Breezy and lightweight.", "image_file": "summer_dress.jpg"},

            # SHOES
            {"name": "White Sneakers", "price": 599.95, "description": "Crisp, clean and comfy.", "image_file": "white_sneakers.jpg"},
            {"name": "Platform Sandals", "price": 345.99, "description": "Chic summer footwear.", "image_file": "sandals.jpg"},
            {"name": "Combat Boots", "price": 589.90, "description": "Edgy and durable.", "image_file": "combat_boots.jpg"},

            # SNACKS
            {"name": "Caramel Popcorn", "price": 150.50, "description": "Sweet and crunchy movie snack.", "image_file": "popcorn.jpg"},
            {"name": "Almond Butter Protein Bar", "price": 285.99, "description": "Healthy and filling.", "image_file": "protein_bar.jpg"},
            {"name": "Matcha Cookies", "price": 265.75, "description": "Soft baked cookies with green tea flavor.", "image_file": "matcha_cookies.jpg"},
            {"name": "Fruit Gummies", "price": 162.25, "description": "Assorted fruit flavors.", "image_file": "gummies.jpg"},
            {"name": "Hot & Spicy Ramen", "price": 124.99, "description": "Instant noodles with a kick.", "image_file": "ramen.jpg"},

            # ELECTRONICS
            {"name": "Wireless Earbuds", "price": 1159.99, "description": "Crystal clear sound and long battery life.", "image_file": "earbuds.jpg"},
            {"name": "Portable Bluetooth Speaker", "price": 2145.00, "description": "Pump up your playlist anywhere.", "image_file": "speaker.jpg"},
            {"name": "Smartphone Ring Light", "price": 914.99, "description": "For perfect selfies anytime.", "image_file": "ring_light.jpg"},
            {"name": "Mini Power Bank", "price": 1329.00, "description": "Slim, fast charging on the go.", "image_file": "power_bank.jpg"},

            # ACCESSORIES
            {"name": "Beaded Bracelet Set", "price": 212.50, "description": "Stackable wrist candy.", "image_file": "bracelets.jpg"},
            {"name": "Canvas Tote Bag", "price": 418.00, "description": "Eco-friendly and stylish.", "image_file": "tote_bag.jpg"},
            {"name": "Layered Necklaces", "price": 520.00, "description": "Gold-toned trendy layers.", "image_file": "necklaces.jpg"},
            {"name": "Retro Cat Eye Sunglasses", "price": 619.99, "description": "Flirty and fierce.", "image_file": "cat_sunglasses.jpg"},

            # SELF CARE
            {"name": "Aloe Vera Face Mask", "price": 146.50, "description": "Soothing hydration for your skin.", "image_file": "face_mask.jpg"},
            {"name": "Lavender Body Lotion", "price": 349.95, "description": "Smells divine, feels divine.", "image_file": "body_lotion.jpg"},
            {"name": "Scented Soy Candle", "price": 511.00, "description": "Mood setter. Room refresher.", "image_file": "candle.jpg"},
            {"name": "Bubble Bath Bombs", "price": 713.75, "description": "Colorful, fizzy relaxation.", "image_file": "bath_bombs.jpg"},
        ]

        for product in products:
            existing = Product.query.filter_by(name=product["name"]).first()
            if not existing:
                db.session.add(Product(**product))

        db.session.commit()
        print(f"Seeded {len(products)} fire products into your store! 🔥")

if __name__ == "__main__":
    seed()
