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
        genders = [request.form.get(f'gender{i}') for i in range(len(student_numbers))]  # 수정된 부분
        departments = request.form.getlist('department[]')
        parts = request.form.getlist('part[]')
        email_id = request.form.get('email_id')
        email_domain = request.form.get('email_domain')
        mbtis = request.form.getlist('mbti[]')
        languages = [request.form.getlist(f'languages{i}') for i in range(len(student_numbers))]

        for i in range(len(student_numbers)):
            result = {
                '이름': names[i],
                '성별': genders[i],
                '학과': departments[i],
                '학번': student_numbers[i],
                '역할': parts[i],
                'Email': f"{email_id}@{email_domain}" if email_id and email_domain else None,
                'MBTI': mbtis[i],
                '프로그래밍 언어': ', '.join(languages[i]) if languages[i] else 'None',
                'images': student_images.get(student_numbers[i], "https://raw.githubusercontent.com/CSID-DGU/2024-2-OSSPrac-azaping-01/main/pic/default.jpg")
            }
            results.append(result)

        return render_template('app_result.html', results=results)

@app.route('/contact')
def contact_info():
    return render_template('app_contact.html')


if __name__ == '__main__':
    app.run(debug=True)
