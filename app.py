
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

#Set up  flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
#mars_app <-name of database
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#Define the route for our HTML page
@app.route("/")
def index():
    #Find the 'mars' collection in our mars_app database
   mars = mongo.db.mars.find_one()
   #Render an HTML template using index.html file
   #Create "mars" collection in MongoDB
   return render_template("index.html", mars=mars)

#Set up scraping route
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   #Update the data ({} means all data) 
   mars.update({}, mars_data, upsert=True)
   return redirect('/', code=302)

if __name__ == "__main__":
   app.run()