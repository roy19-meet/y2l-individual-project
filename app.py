from flask import Flask
from flask import render_template
from flask import Flask, render_template, request



app = Flask(__name__)

@app.route('/')
def hello_world():
     return render_template("home.html")

@app.route('/Rock_page',methods=['GET'])
def rock_page():     
 if request.method == 'GET':
	    return render_template('rock_page.html')

@app.route('/Blues_page',methods=['GET'])
def blues_page():     
 if request.method == 'GET':
	    return render_template('blues_page.html')

@app.route('/create_artist',methods=['GET','POST'])
def create_artist():
	if request.method == 'GET':
	  return render_template('create_artist.html')
	else:
		Genre=request.form['Genre']
		Name=request.form['Name']
		Info=request.form['Info']
		Hits=request.form['Hits']
		create_artists(Genre,Name,Info,Hits)
		return render_template('home.html')

      

if __name__ == '__main__':
    app.run(debug=True)

