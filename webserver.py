"""
webserver.py

File that is the central location of code for your webserver.
"""
import requests
import os

from flask import Flask, request, render_template

# Create application, and point static path (where static resources like images, css, and js files are stored) to the
# "static folder"
app = Flask(__name__,static_url_path="/static")

@app.route('/')
def home():
    """
    If someone goes to the root of your website (i.e. http://localhost:5000/), run this function. The string that this
    returns will be sent to the browser
    """
    return render_template("index.html") # Render the template located in "templates/index.html"

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/contact')
def contact():
	return render_template("contact.html")

@app.route('/blog/8-experiments-in-motivation ')
def m1():
	return render_template("m1.html")


@app.route('/blog/a-mindful-shift-of-focus')
def m2():
	return render_template("m2.html")

@app.route('/blog/how-to-develop-an-awesome-sense-of-direction')
def m3():
	return render_template("m3.html")

@app.route('/blog/training-to-be-a-good-writer')
def m4():
	return render_template("m4.html")

@app.route('/blog/what-productivity-systems-wont-solve ')
def m5():
	return render_template("m5.html")

@app.route('/contact', methods=['POST'])
def send_email():
	notifications = []
	name = request.form.get("name")
	subject = request.form.get("subject")
	message = request.form.get("message")

	if (name == ""):
		notifications.append("Please fill out the name box below")
	elif(subject == ""):
		notifications.append("Please fill out the subejct box below")
	elif(message == ""):
		notifications.append("Please fill out the message box below")
	else:
		data = {
	    'from': os.environ["INFO253_MAILGUN_FROM_EMAIL"],
		'to': os.environ["INFO253_MAILGUN_TO_EMAIL"],
		'subject': subject,
		'text': message,
		}
		auth = (os.environ["INFO253_MAILGUN_USER"], os.environ["INFO253_MAILGUN_PASSWORD"])
		r = requests.post(
			'https://api.mailgun.net/v3/{}/messages'.format(os.environ["INFO253_MAILGUN_DOMAIN"]),
			auth=auth,
			data=data)

		if (r.status_code == requests.codes.ok):
			notifications.append("Hi " + name + ", your message was sent")
		else:
			notifications.append("You email was not sent. Please try again later")

	return render_template("contact.html", notifications=notifications)
