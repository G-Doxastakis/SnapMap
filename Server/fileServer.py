from flask import Flask, render_template, request
from werkzeug import secure_filename
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/home/gdoxastakis/ServerStorage'
@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		print ('Receiving File   ')
		f = request.files['file']
		print (f.filename)
		f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
		return 'OK'
	else:
		return 'Server Online'
if __name__ == '__main__':
   app.run(app.run(host='83.212.116.82', port=9000, debug=True))