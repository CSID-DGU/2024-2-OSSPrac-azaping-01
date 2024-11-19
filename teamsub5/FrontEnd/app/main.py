from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def input():
    return render_template('input.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = dict()
        result['Name'] = request.form.get('name')
        result['StudentNumber'] = request.form.get('StudentNumber')
        result['Major'] = request.form.get('Major')
        result['gender'] = request.form.get('gender')
        result['languages'] = request.form.getlist('languages')
        result['languages'] = ', '.join(result['languages'])
        
        # Combine email ID and domain
        email_id = request.form.get('email_id')
        email_domain = request.form.get('email_domain')
        result['Email'] = f"{email_id}@{email_domain}" if email_id and email_domain else None
        
        return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9000)