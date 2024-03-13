from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/results", methods=["GET", 'POST'])
def results():
   test_string = request.form['test_string']
   regex_pattern = request.form['regex_pattern']
   matches = re.findall(regex_pattern, test_string)
   return render_template('results.html', matches=matches)

@app.route('/validate_email', methods=['GET', 'POST'])
def validate_email():
    if request.method == 'POST':
        email = request.form['email']
        is_valid = validate_email_address(email)
        return render_template('validate_email_result.html', email=email, is_valid=is_valid)
    return render_template('validate_email.html')

def validate_email_address(email):
    # Regular expression for email validation
    regex_pattern = r'^[\w\-]+@[\w\.-]+\.\w+$'
    return re.match(regex_pattern, email) is not None



if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)