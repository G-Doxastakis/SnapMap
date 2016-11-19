from flask import Flask, render_template, request
from werkzeug import secure_filename
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/home/gdoxastakis/ServerStorage'
@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'OK'
		
if __name__ == '__main__':
   app.run(debug = True)