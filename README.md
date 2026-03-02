# saucedemo-QA

- install command: `pip install -r requirements.txt`
- run command: `python -m pytest -v`

## Test Case 1: Successful Login & Add to Cart
- Login with valid credentials
- Add 2-3 products to cart
- Verify cart shows correct item count
- Verify cart shows correct products
## Test Case 2: Remove Item from Cart
- Add multiple items to cart
- Remove one item
- Verify item count updates
- Verify removed item is no longer in cart
## Test Case 3: Checkout Flow
- Complete checkout with valid information
- Verify order confirmation appears
- Verify success message
## Test Case 4: Negative Testing
- Try login with invalid credentials
- Verify appropriate error message

- Try checkout without adding items
- Any edge case you can think of
