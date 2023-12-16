# Laced picture grabber
Grab the images of a product on laced.com and store them to your own device.

## Setup
install dependencies by running the command `pip install -r requirements.txt` in the directory containing `requirements.txt`

## Usage
Navigate to a product page on laced and copy the product page's url. E.g
https://www.laced.com/products/adidas-campus-00s-grey-gum-gs

call `main.py` passing in the product url as the first positional argument
`python main.py https://www.laced.com/products/adidas-campus-00s-grey-gum-gs`

The images for the specified product should be saved to a new directory `products/<product_name>/`

