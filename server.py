from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/") 
def index(): 
    return render_template('index.html') 

@app.route("/<string:page_name>")  
def html(page_name):  
    return render_template(page_name) 

def write_to_file(data): 
    with open('database.txt',mode='a') as database: 
        email = data["email"] 
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}') 

def write_to_csv(data): 
    with open('database.csv',mode='a',newline='') as database2: #append with new line everytime 
        email = data["email"] 
        subject = data["subject"]
        message = data["message"]
        #csv writer object -> writing data to our csv object. yes we can just copy and read it from doc if needed
        csv_write = csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow([email,subject,message]) # write in to our database2


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST': 
        try:
            data = request.form.to_dict() 
            write_to_csv(data) # call the function to write to database.csv
            return redirect('/thankyou.html') 
        except:
            return 'did not save to database'
    else:
        return 'something wrong try again'


