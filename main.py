# pip install Flask

# Install "Docker Desktop" - https://docs.docker.com/desktop/windows/install/

# URL - http://localhost:105/product/

from flask import Flask, jsonify, request
app = Flask(__name__)

lstProducts = [{'soap':'nirma','biscuit':'nutrichoice'}]

@app.route('/product/')
def product():
    return jsonify(lstProducts)

@app.route('/product/', methods=['POST'])
def add_product():
    lstProducts.append(request.get_json())
    return '',204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)

# In Fiddler add
# POST - http://localhost:105/product/
# JSON - {"biscuit": "milk","soap": "aol"}
# Check URL - http://localhost:105/product/