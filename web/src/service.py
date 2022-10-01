from flask import Flask, render_template, request, redirect, url_for, session

from engine import *
from werkzeug.utils import secure_filename
from pathlib import Path

# Initialize flask app and session key
app = Flask(__name__)
app.secret_key = "1234" # Have to give any random key to be able to use session to store variables and pass them between routes


# Define upload folder and allowed ext
UPLOAD_FOLDER = './Uploaded/'


# request file upload
@app.route('/')
def upload_file():
   return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def processFile():
   if request.method == 'POST':
       # A <form> tag is marked with enctype=multipart/form-data and an <input type=file> is placed in that form.
       f = request.files['file'] # The application accesses the file from the files dictionary on the request object.
       
       # Check if the user didn't input any file
       if f.filename == '':
           # if the user didn't upload anyfile redirect to the /
           return redirect(url_for('upload_file'))

       # Give secure name to file
       sec_fname= secure_filename(f.filename)

       # Use the save() method of the file to save the file permanently somewhere on the filesystem. 
       f.save(UPLOAD_FOLDER + sec_fname)

       # Save file name in session
       session['sec_fname'] = sec_fname

       # check file type
       fileExt= Path(sec_fname).suffix 

       # Initialize fileType varable used for url-routing
       fileType=''

       if fileExt =='.txt':
           #print('textfile')
           fileType = 'do_process_text'

       else:
           return "file format must be .txt"

   return redirect(url_for(fileType))
      


@app.route('/text', methods=['GET', 'POST']) # changed methods to include get and post 
def do_process_text(): 
    # Retrieve filename variable from session
    filename= session.get('sec_fname', None)

    # Recreate file path
    filePath= UPLOAD_FOLDER + filename

    # Call process text
    ner_results= process_text(filePath)
    return 'type: text file, ' + "Filename:{}, ".format(str(filename)) + 'Result: ' + ner_results


'''
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug= True) # change port number
'''
