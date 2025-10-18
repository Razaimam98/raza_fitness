from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Homepage
@app.route('/')
def home():
    return render_template('index.html', title="Home")

# Sitemap
@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'sitemap.xml')

# Robots.txt
@app.route('/robots.txt')
def robots():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'robots.txt')

# Fitness Blog Pages
@app.route('/nutrition')
def nutrition():
    return render_template('nutrition.html', title="Nutrition")

@app.route('/supplements')
def supplements():
    return render_template('supplements.html', title="Supplements")

@app.route('/workouts')
def workouts():
    return render_template('workouts.html', title="Workouts")

@app.route('/motivation')
def motivation():
    return render_template('motivation.html', title="Motivation")

# General Website Pages
@app.route('/blog')
def blog():
    return render_template('blog.html', title="Blog")

@app.route('/about')
def about():
    return render_template('about.html', title="About")

@app.route('/privacy')
def privacy():
    return render_template('privacy.html', title="Privacy Policy")

if __name__ == "__main__":
    app.run(debug=True)
