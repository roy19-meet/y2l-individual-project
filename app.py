from flask import Flask, send_from_directory, session as login_session
from flask import render_template
from werkzeug import secure_filename
from database import *
from flask import Flask, render_template, request, redirect, url_for
import os
UPLOAD_FOLDER='static/'
ALLOWED_EXTENSIONS=set(['mp3','wav'])

session = login_session

 
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key ="pokemon"

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
		art=query_genre('Blues')
		return render_template('blues_page.html',art=art, genree='Blues')

@app.route('/Pop_page',methods=['GET'])
def pop_page():     
	if request.method == 'GET':
		art=query_genre('Pop')
		return render_template('pop.html',art=art, genree='Pop')

@app.route('/Hiphop_page',methods=['GET'])
def hiphop_page():     
	if request.method == 'GET':
		art=query_genre('Hipop')
		return render_template('hiphop.html',art=art, genree='Hiphop')



@app.route('/create_artist',methods=['GET','POST'])
def create_artist():
	if 'logged_in' in session:
		if session['logged_in']==True:
			if request.method == 'GET':
				return render_template('create_artist.html')
			if request.method=="POST":
				print('s')	
				genree=request.form['genree']
				print('w')
				name=request.form['name']
				neforma=request.form['neforma']
				hits=request.files['hits']
				# like=0
				if hits and allowed_file(hits.filename):
			  	    filename = secure_filename(hits.filename)
			  	    hits.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			  	    create_artists(genree,name,neforma,url_for('uploaded_file', filename = filename))
			  	    return render_template('home.html')





		else:
			return redirect(url_for('login_route'))            
	else:
		return redirect(url_for('login_route'))



# @app.route('/add_like',methods=['GET','POST'])
# def add_like_route():
# 	if (request.method=='GET'):
# 		return render_template('artist.html')
# 	else:
# 		the_id = request.form("id")
# 		add_like(the_id)
# 		art = query_id(the_id)
# 		return render_template('artist.html',d=id,c=art.name,r=art.neforma, p=art.hits,l=art.like)




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

    g=query_by_username(username)

    if g!=None:
      print ('we already have a user with that name')
    else:   
      create_users(username,password)
      session['display_login'] = True
      return redirect(url_for('home'))






    return render_template('singup_response.html')



@app.route('/login', methods=['GET', 'POST'])
def login_route():
  if 'logged_in' in session:
   if session['logged_in']==True:
    return redirect (url_for('hello_world'))
  if request.method == 'POST':
    print('hey')
    User=query_by_username(request.form['username'])
    if User==None:
      return redirect (url_for('signup_route'))

    else:
      if request.form['password']==User.password:
        session['logged_in'] = True
        session['user_id']=User.id
        session['display_login'] = True
        print (session)
        return redirect(url_for('hello_world'))
      return render_template('login.html')

  else:
    return render_template('login.html') 


@app.route('/logout', methods=['GET'])
def logout():
  print('qqqqqq')
  if 'user_id' in session:
    print('super')
    del session['user_id']
    session['logged_in']=False
    print('logged out')
  return redirect(url_for('hello_world'))







if __name__ == '__main__':
  app.run(debug=True)

