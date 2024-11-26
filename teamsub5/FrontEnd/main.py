from flask import Flask, request, render_template

app = Flask(__name__)

student_images = {
    "2020110401": "https://raw.githubusercontent.com/CSID-DGU/2024-2-OSSPrac-azaping-01/main/pic/2020110401.jpg",
    "2021113455": "https://raw.githubusercontent.com/CSID-DGU/2024-2-OSSPrac-azaping-01/main/pic/2021113455.jpg",
    "2022111520": "https://raw.githubusercontent.com/CSID-DGU/2024-2-OSSPrac-azaping-01/main/pic/2022111520.jpg",
    "2020111670": "https://raw.githubusercontent.com/CSID-DGU/2024-2-OSSPrac-azaping-01/main/pic/2020111670.jpg",
    # 다른 학번에 따른 URL 추가 가능
}

@app.route('/')
def index():
    return render_template('app_index.html')

@app.route('/input')
def input():
    return render_template('app_input.html')

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        results = []

        student_numbers = request.form.getlist('StudentNumber[]')
        names = request.form.getlist('name[]')
        genders = [request.form.get(f'gender{i}') for i in range(len(student_numbers))]
        departments = request.form.getlist('department[]')
        parts = request.form.getlist('part[]')
        email_ids = request.form.getlist('email_id[]')
        email_domains = request.form.getlist('email_domain')
        mbtis = request.form.getlist('mbti[]')
        languages = [request.form.getlist(f'languages{i}') for i in range(len(student_numbers))]

        for i in range(len(student_numbers)):
            result = {
                '이름': names[i],
                '성별': genders[i],
                '학과': departments[i],
                '학번': student_numbers[i],
                '역할': parts[i],
                'Email': f"{email_ids[i]}@{email_domains[i]}",
                'MBTI': mbtis[i],
                'Programming Languages': ', '.join(languages[i]) if languages[i] else 'None',
                'images': student_images.get(student_numbers[i], "https://raw.githubusercontent.com/CSID-DGU/2024-2-OSSPrac-azaping-01/main/pic/default.jpg")
            }
            results.append(result)

        return render_template('app_result.html', results=results)

@app.route('/contact')
def contact_info():
    return render_template('app_contact.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)