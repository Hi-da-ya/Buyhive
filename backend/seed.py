from random import choice as rc
from faker import Faker

from app import app
from models import db, Product, User,Review,Order,OrderItem,Category


fake = Faker()
with app.app_context():
    # Delete existing products (optional)
    Product.query.delete()
    Category.query.delete()
    User.query.delete()

    category = []

    # Create category instances
    catone = Category(name='women')
    cattwo = Category(name='men')
    catthree = Category(name='kids')
    catfour = Category(name='sports-wear')


    # Append category instances to the list
    category.append(catone)
    category.append(cattwo)
    category.append(catthree)
    category.append(catfour)
    

    # Add categories to the session and commit
    db.session.add_all(category)
    db.session.commit()
    print("Categories seeded successfully!")

    category_women = Category.query.filter_by(name='women').first()
    category_men = Category.query.filter_by(name='men').first()
    category_kids = Category.query.filter_by(name='kids').first()
    category_sports_wear= Category.query.filter_by(name='sports-wear').first()
    

    # Define products
    products = [
        Product(
            name='Summer dress',
            price=500.00,
            image_url='https://img.freepik.com/free-photo/graphic-woman-dress-trendy-design-white-background_460848-13623.jpg?t=st=1720702522~exp=1720706122~hmac=827df0a41317a41faffc3243fcb5a22a3c1978c9f670b9ec75b71579e749843d&w=740',
            description="Breezy elegance meets summer's charm in our vibrant, floral-patterned dress for effortless style under the sun.",
            category=category_women
            ),
        Product(
            name='Off-shoulder ankara dress',
            price=1500.00,
            image_url='https://img.freepik.com/free-photo/cute-small-height-african-american-girl-with-dreadlocks-wear-coloured-yellow-dress-posed-shop-showcase-trade-center_627829-13025.jpg?t=st=1720702951~exp=1720706551~hmac=855d4fce6a1aa7b260998d9113550a352d0c57a3516fc4d3b552e1d127df05b1&w=740',
            description="Radiate elegance in our Ankara dress, adorned with vibrant patterns and tailored for timeless sophistication and charm.",
            category=category_women
        ),
        Product(
            name='Light cream chiffon blouse',
            price=200.00,
            image_url='https://img.freepik.com/free-photo/graphic-tshirt-trendy-design-mockup-presented-wooden-hanger_460848-13975.jpg?t=st=1720703168~exp=1720706768~hmac=00c08eed564605e7d74cd104ab5e694bc9c2891a107ca773a5c25d93142677ed&w=826',
            description='"Effortlessly chic chiffon top: lightweight, airy, and perfect for any occasion, enhancing your elegance with every wear.',
            category=category_women
        ),
        Product(
            name='Party dress',
            price=2800.00,
            image_url='https://img.freepik.com/free-photo/dress-ballet-shoes_155003-641.jpg?t=st=1720703584~exp=1720707184~hmac=907f58b2c44c0dca1146bd6c3bacc3ea0a75574ae308c0570407d5a7ec062888&w=740',
            description="Stunning party dress: vibrant, glamorous, and designed to turn heads at every celebration.",
            category=category_women
        ),
        Product(
            name='Ruby Red Mini Delight',
            price=1200.00,
            image_url='https://img.freepik.com/premium-photo/studio-portrait-attractive-woman-with-long-wavy-hair-tail-wearing-mini-red-dress-black-high-heels-white-background-isolate_132075-9301.jpg?w=740',
            description=' "Captivate in this vibrant red mini dress, blending daring allure with playful sophistication."',
            category=category_women
        ),
        Product(
            name='Purple denim jacket',
            price=1800.00,
            image_url='https://img.freepik.com/free-psd/purple-jacket-made-basic-denim-isolated-transparent-background_191095-22715.jpg',
            description='Elevate your style with this chic purple denim jacket, a versatile staple for effortless cool',
            category=category_women
        ),
        Product(
            name="Palazzo pants",
            price=150.00,
            image_url='https://www.travelandleisure.com/thmb/2j403kjQ2C50Yx1U-ZXTlyDWbNw=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/anrabess-linen-palazzo-pants-tout-61f8d6eb5a2640dfadd1aa898055d943.jpg',
            description='Flowy and stylish, these palazzo pants offer comfort and sophistication for any occasion.',
            category=category_women
        ),
        Product(
            name='Urban Chic Casual Pants',
            price=200.00,
            image_url='https://img.kwcdn.com/product/Fancyalgo/VirtualModelMatting/2328d5b2feada10f7d24849e53e1d9a4.jpg',
            description="Effortlessly blend comfort and style with these versatile urban chic casual pants, ideal for everyday wear.",
            category=category_women
        ),
        Product(
            name='Midi Waist Bottoms Straight Wide Legs Cargo Pants Four Pockets Trousers',
            price=120.00,
            image_url='https://i.ebayimg.com/images/g/gA8AAOSw1AtkdA4k/s-l1200.webp',
            description='Discover comfort and style in these midi waist, wide-leg cargo pants with four pockets, perfect for effortless urban fashion.',
            category=category_women
        ),
        Product(
            name='Denim pants',
            price=120.00,
            image_url='https://img.freepik.com/free-photo/denims_1303-4490.jpg?t=st=1720713159~exp=1720716759~hmac=e71df394f664db72317524eb7039b292f3cf50dfc60670b43be9498277de5a35&w=740',
            description='Description for Product 5',
            category=category_women
        ),
        Product(
            name='Elegant denim',
            price=150.00,
            image_url='https://img.freepik.com/premium-photo/happy-asia-woman-bright-blue-skinny-crop-jeans-sky-blue-jeans_38810-8029.jpg',
            description='Description for Product 2',
            category=category_women
        ),
        Product(
            name='Blue hoodie',
            price=800.00,
            image_url='https://img.freepik.com/free-photo/portrait-cool-teenage-boy-wearing-hoodie_23-2149085833.jpg',
            description='Description for Product 4',
            category=category_kids
        ),
        
        Product(
            name='Dreads',
            price=1500.00,
            image_url='https://img.freepik.com/free-photo/photorealistic-portrait-young-person-with-braids_23-2151570193.jpg',
            description='Description for Product 2',
            category=category_kids
        ),
        Product(
            name='skate girl',
            price=2000.00,
            image_url='https://img.freepik.com/free-photo/portrait-young-girl-with-roller-blades_23-2149185131.jpg',
            description='Description for Product 3',
            category=category_kids
        ),
        Product(
            name='Boys sweater and blank pants',
            price=800.00,
            image_url='https://img.freepik.com/premium-photo/man-woman-kid-person-character-portrait-young-boy-white-sweater-black-pants-jumping_761066-119172.jpg',
            description='Description for Product 4',
            category=category_kids
        ),
        Product(
            name='White girl sweat pants and sweater',
            price=1200.00,
            image_url='https://img.freepik.com/premium-psd/cute-kig-girl-running-white-background_652930-350.jpg',
            description='Description for Product 5',
            category=category_kids
        ),
        Product(
            name='generic white tshirt for kids',
            price=800.00,
            image_url='https://img.freepik.com/free-photo/full-length-portrait-excited-little-african-girl-jumping_171337-5480.jpg',
            description='Description for Product 4',
            category=category_kids
        ),
        
        Product(
            name='Casual boy outfit',
            price=1500.00,
            image_url='https://img.freepik.com/free-photo/portrait-cool-teenage-boy-with-headphones_23-2149085797.jpg',
            description='Description for Product 2',
            category=category_kids
        ),
        Product(
            name='Ankara attire',
            price=2000.00,
            image_url='https://img.freepik.com/free-photo/photorealistic-portrait-young-person-with-braids_23-2151570201.jpg',
            description='Description for Product 3',
            category=category_kids
        ),
        Product(
            name='Denim pants for teens girls',
            price=800.00,
            image_url='https://img.freepik.com/free-photo/happy-smiling-lady-walking-looking-aside-isolated_171337-6663.jpg',
            description='Description for Product 4',
            category=category_kids
        ),
        Product(
            name='Cute todler dress',
            price=1200.00,
            image_url='https://img.freepik.com/premium-photo/child-girl-flowery-dress-with-red-hat-studio-photo-with-white-background-clipping_496782-1167.jpg?size=626&ext=jpg',
            description='Description for Product 5',
            category=category_kids
        ),
        Product(
            name='Red checked dress for kids',
            price=800.00,
            image_url='https://img.freepik.com/free-vector/girl-s-dress-vintage-illustration-vector-remixed-from-artwork-by-virginia-berge_53876-116268.jpg?size=626&ext=jpg',
            description='Description for Product 4',
            category=category_kids
        ),
        
        Product(
            name='Cute beige dress',
            price=150.00,
            image_url='https://img.freepik.com/free-photo/full-shot-kid-holding-flowers_23-2149067165.jpg?size=626&ext=jpg',
            description='Description for Product 2',
            category=category_kids
        ),
        Product(
            name='Yellow sleeveless dress',
            price=2000.00,
            image_url='https://img.freepik.com/premium-photo/portrait-smiley-young-girl-with-skateboard_23-2149185194.jpg?size=626&ext=jpg',
            description='Description for Product 3',
            category=category_kids
        ),
        Product(
            name='Pink vest jacket',
            price=800.00,
            image_url='https://img.freepik.com/premium-photo/jacket_87394-39085.jpg?semt=ais_user',
            description='Description for Product 4',
            category=category_kids
        ),
        Product(
            name='Todler vest',
            price=1200.00,
            image_url='https://img.freepik.com/free-photo/girl-s-white-tank-top-studio_53876-97724.jpg?semt=ais_user',
            description='Description for Product 5',
            category=category_kids
        ),
        #Men product
        Product(
            name='White crew-neck t-shirt',
            price=2000.00,
            image_url='https://images.unsplash.com/photo-1581655353564-df123a1eb820?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8c2hpcnR8ZW58MHx8MHx8fDA%3D',
            description='Description for Product 3',
            category=category_men
        ),
        Product(
            name='Yello splash',
            price=800.00,
            image_url='https://plus.unsplash.com/premium_photo-1683140435505-afb6f1738d11?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8c2hpcnR8ZW58MHx8MHx8fDA%3D',
            description='Description for Product 4',
            category=category_men
        ),
        
        Product(
            name='Black crew neck t-shirt',
            price=1500.00,
            image_url='https://images.unsplash.com/photo-1583743814966-8936f5b7be1a?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8c2hpcnR8ZW58MHx8MHx8fDA%3D',
            description='Description for Product 2',
            category=category_men
        ),
        Product(
            name='Black and yellow plaid button up shirt',
            price=2000.00,
            image_url='https://images.unsplash.com/photo-1607345366928-199ea26cfe3e?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fHNoaXJ0fGVufDB8fDB8fHww',
            description='Description for Product 3',
            category=category_men
        ),
        Product(
            name='Formal white shirt',
            price=2000.00,
            image_url='https://images.unsplash.com/photo-1598033129183-c4f50c736f10?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTR8fHNoaXJ0fGVufDB8fDB8fHww',
            description='Description for Product 3',
            category=category_men
        ),
        Product(
            name='Black leather jacket',
            price=800.00,
            image_url='https://images.unsplash.com/photo-1521223890158-f9f7c3d5d504?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8amFja2V0fGVufDB8fDB8fHww',
            description='Description for Product 4',
            category=category_men
        ),
        
        Product(
            name='Men brown coat',
            price=1500.00,
            image_url='https://images.unsplash.com/photo-1525457136159-8878648a7ad0?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjB8fGphY2tldHxlbnwwfHwwfHx8MA%3D%3D',
            description='Description for Product 2',
            category=category_men
        ),
        Product(
            name='Brown pull neck',
            price=2000.00,
            image_url='https://img.freepik.com/free-photo/young-handsome-man-posing-with-hat_23-2148884326.jpg?semt=ais_user',
            description='Description for Product 3',
            category=category_men
        ),
        Product(
            name='Checked coat',
            price=2000.00,
            image_url='https://img.freepik.com/free-photo/portrait-stylish-young-man-with-modern-hat_23-2148466063.jpg?semt=ais_user',
            description='Description for Product 3',
            category=category_men
        ),
        Product(
            name='Peach pants',
            price=800.00,
            image_url='https://img.freepik.com/free-photo/full-length-portrait-confident-young-african-man_171337-8186.jpg?semt=ais_user',
            description='Description for Product 4',
            category=category_men
        ),
        
        Product(
            name='White pants',
            price=1500.00,
            image_url='https://img.freepik.com/premium-photo/young-handsome-bearded-man-with-short-hair_251136-10756.jpg?semt=ais_user',
            description='Description for Product 2',
            category=category_men
        ),
        Product(
            name='Denim pants for men',
            price=2000.00,
            image_url='https://img.freepik.com/free-photo/african-american-man_1303-9961.jpg?semt=ais_user',
            description='Description for Product 3',
            category=category_men
        ),
        Product(
            name='Casual dennim pants',
            price=2000.00,
            image_url='https://img.freepik.com/free-photo/portrait-smiling-young-man-holding-books-hand-standing-against-red-wall_23-2148093332.jpg?semt=ais_user',
            description='Description for Product 3',
            category=category_men
        ),
        Product(
            name='Maroon men suit',
            price=800.00,
            image_url='https://images.unsplash.com/photo-1558222218-b7b54eede3f3?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTJ8fGphY2tldCUyMG1lbnxlbnwwfHwwfHx8MA%3D%3D',
            description='Description for Product 4',
            category=category_men
        ),
        
        Product(
            name='Suspenders',
            price=1500.00,
            image_url='https://img.freepik.com/premium-photo/image-attractive-young-man-wearing-hat-standing-studio-isolated-grey-background_171337-86341.jpg?semt=ais_user',
            description='Description for Product 2',
            category=category_men
        ),
        
    ]

    
    db.session.add_all(products)
    db.session.commit()

    print("Data seeded successfully!")
 




