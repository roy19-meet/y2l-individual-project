from flask import Flask, send_from_directory
from flask import render_template
from werkzeug import secure_filename
from database import create_artists, query_genre, get_all_artists,create_users
from flask import Flask, render_template, request, redirect, url_for
import os
UPLOAD_FOLDER='static/'
ALLOWED_EXTENSIONS=set(['mp3','wav'])




 
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
	return '.' in filename and \
	  filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def hello_world():
  return render_template("home.html")

@app.route('/Rock_page',methods=['GET'])
def rock_page():     
 if request.method == 'GET':
   art=query_genre('Rock')
   return render_template('rock_page.html',art=art, genree="Rock")

@app.route('/Blues_page',methods=['GET'])
def blues_page():     
 if request.method == 'GET':
	    return render_template('blues_page.html')

@app.route('/create_artist',methods=['GET','POST'])
def create_artist():
	if request.method == 'GET':
	  return render_template('create_artist.html')
	else:
	  print('s')	
	  genree=request.form['genree']
	  print('w')
	  name=request.form['name']
	  neforma=request.form['neforma']
	  hits=request.files['hits']
	  if file and allowed_file(file.filename):
	  	
	  	filename = secure_filename(file.filename)
	  	file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

	  	create_artists(genree,name,neforma,url_for('uploaded_file', filename = filename))
	  return render_template('home.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
	return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
      
@app.route('/artists/<int:id>',methods=['GET'])
def go_artist(id):
  artists=get_all_artists()	
  for art in artists:
    if art.id==id:
      return render_template('artist.html',d=id,c=art.name,r=art.neforma, p=art.hits)

@app.route('/signup',methods=['GET','POST'])
def signup():
  if request.method == 'GET':
    return render_template('signup.html')
  else:
    password=request.form['password']
    username=request.form['username']
    create_users(password,username)
    return render_template('singup_response.html')


# @app.route('/signin',methods=['GET','POST'])
# def signin():
#   if request.method == 'GET':
#     return render_template('signin.html')
#   else:
    




if __name__ == '__main__':
  app.run(debug=True)

