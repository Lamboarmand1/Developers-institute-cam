from flask import Flask, render_template, redirect
#import database_manager
import random
import json

app = Flask(__name__)

with open('products_db.json', 'r') as file_obj:
	data = json.load(file_obj)

'''data = [
	{
		'id' : 1,
		'name': 'iphone 9',
		'price': 799,
		'remains': True
	},

	{
		'id' : 2,
		'name': 'Macbook Pro',
		'price': 4799,
		'remains': False
	},

	{
		'id': 3,
		'name': 'Apple Watch',
		'price': 10799,
		'remains': True
	},

	{
		'id': 4,
		'name': 'Apple stand pro',
		'price': 99999,
		'remains': True
	},
]
'''
#data = database_manager.load_database()


@app.route('/')
def home():
	return redirect('product')

@app.route('/roll/<number>')
def roll(number):
	random_number = random.randint(1,101)
	if random_number == int(number) :
		return f'Bravo tu as trouvé le bon nombre: {random_number}'
	else :
		return f'LOST, the good number was {random_number}'

@app.route('/product')
def show_product():
	css = open('style.css', 'r').read()
	return render_template('produits.html', products=data, additional_css=css)


@app.route('/product/<id>')
def product_details(id):
	dic_to_find={}
	for elements in data:
		if elements['ProductId'] == id:
			print(elements)
			dic_to_find=elements
	return render_template('details.html', product= dic_to_find)


@app.route('/search/by-category/<category>')
def search_by_category(category):
	liste_dic=[]
	css = open('style.css', 'r').read()
	for product in data:
		if product['Category'] == category:
			liste_dic.append(product)
	return render_template('produits.html', products=liste_dic, additional_css=css)

#Daily challenge 2
@app.route('/colors')
def list_color():
	return render_template('color.html')


@app.route('/color/<color>')
def show(color):
	return render_template('colors.html', color=color)


if __name__== '__main__' :
	app.run(debug=True)

