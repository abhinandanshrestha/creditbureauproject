from flask import Flask,request,redirect,url_for,jsonify
from flask import render_template
import csv,requests 

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    csv_file = 'data.csv'
    json_data = []

    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            json_data.append({
                'user_id': row['user_id'],
                'credit_score': row['credit_score'],
                'report_date': row['report_date'],
                'open_accounts': row['open_accounts'],
                'closed_accounts': row['closed_accounts'],
                'total_accounts': row['total_accounts'],
                'oldest_account_type': row['oldest_account_type'],
                'oldest_account_date': row['oldest_account_date'],
                'recent_account_type': row['recent_account_type'],
                'recent_account_date': row['recent_account_date'],
                'active_accounts': row['active_accounts'],
                'closed_accounts': row['closed_accounts'],
                'credit_utilization': row['credit_utilization'],
                'payment_history': row['payment_history'],
                'name':row['name'],
                'date_of_birth':row['date_of_birth'],
                'address':row['address'],
                'ssn':row['ssn'],
                'credit_card_number':row['credit_card_number']
            })

    return jsonify(json_data)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def form():
    userid = request.form['userid']
    name = request.form['name']
    dob = request.form['dob']
    address = request.form['address']
    ssn = request.form['ssn']
    credit_card_number = request.form['credit_card_number']
    # print(userid,name,dob,address,ssn,credit_card_number,ssn)

    return redirect(url_for('check_condition', userid=userid, name=name,dob=dob, address=address, ssn=ssn,credit_card_number=credit_card_number))

@app.route('/check_condition')
def check_condition():
    # Retrieve the form data from the URL parameters
    userid = request.args.get('userid')
    name = request.args.get('name')
    dob = request.args.get('dob')
    address = request.args.get('address')
    ssn = request.args.get('ssn')
    credit_card_number = request.args.get('credit_card_number')

    # Send a GET request to the /api endpoint
    response = requests.get('http://localhost:5000/api')
    
    if response.status_code == 200:
        json_data = response.json()
        user_data = None
        for data in json_data:
            if data['user_id'] == userid and data['name'] == name and data['date_of_birth'] == dob and data['address'] ==address and data['ssn']==ssn and data['credit_card_number']==credit_card_number:
                user_data = data
                break

        if user_data:
            # Pass the user data and additional details to the success.html template
            return render_template('success.html', user_data=user_data)
        else:
            message="User data error Please check again"

            # User not found
            return render_template('error.html',message=message)
    else:
        message="API request failed"

        # API request failed
        return render_template('error.html',message=message)

# @app.route('/<u>/<n>/<d>/<a>/<s>/<c>')
# def creditData(u, n,d,a,s,c):
#     print(u,n,d,a,s,c)
#     return render_template('error.html',u=userid, n=name,d=dob, a=address, s=ssn,c=credit_card_number)
    # Send a GET request to the /api endpoint
    # response = requests.get('http://localhost:5000/api')
    
    # if response.status_code == 200:
    #     json_data = response.json()
    #     user_data = None
    #     for data in json_data:
    #         if data['user_id'] == userid:
    #             user_data = data
    #             break

    #     if user_data:
    #         # Pass the user data and additional details to the success.html template
    #         return render_template('success.html', user_data=user_data)
    #     else:
    #         # User not found
    #         return render_template('error.html',userid=userid,name=name,address=address,ssn=ssn,credit_card_number=credit_card_number)
    # else:
    #     # API request failed
    #     return render_template('error.html',userid=userid,name=name,address=address,ssn=ssn,credit_card_number=credit_card_number)




if __name__ == '__main__':
    app.run(debug=True)

