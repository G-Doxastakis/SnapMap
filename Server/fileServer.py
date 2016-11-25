#!/usr/bin/python
from flask import Flask, render_template, request, send_from_directory
from werkzeug import secure_filename
import os
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/home/gdoxastakis/ServerStorage'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		file = request.files['file']
		if file :
			filename = secure_filename(file.filename)
			print(filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return 'OK'
		return 'No File'
	else:
		return 'Server Online'

@app.route('/download/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename, as_attachment=True)
		
if __name__ == '__main__':
   app.run(app.run(host='83.212.116.82', port=9000, debug=True))