from flask import Flask, render_template, request
from werkzeug import secure_filename
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/home/gdoxastakis/ServerStorage'
@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		
		
		file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No file')
            return redirect(request.url)
        if file :
			print ('Receiving File')
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		return 'OK'
	else:
		return 'Server Online'
if __name__ == '__main__':
   app.run(app.run(host='83.212.116.82', port=9000, debug=True))