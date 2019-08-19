from flask import Flask, request, render_template
import requests
import os
app = Flask(__name__)

# Page Requests
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/portfolio')
def portfolio():
	return render_template('portfolio.html')

@app.route('/portfolio-single')
def portfolio_single():
	return render_template('portfolio-single.html')

@app.route('/services')
def services():
	return render_template('services.html')


# Data Requests
@app.route('/send_contact', methods=['POST'])
def send_contact():
	# Gather Data
	contactInfo = request.json

	# Process Data
	contactServiceUrl = "http://localhost:5001/contact"
	requests.post(contactServiceUrl,json=contactInfo)

	# Return status code
	return "200"


# Run app on 0.0.0.0:5000
if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
