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
    # 수집된 데이터를 확인하기 위해 각 필드를 출력합니다.
    names = request.form.getlist('name[]')
    departments = request.form.getlist('department[]')
    student_numbers = request.form.getlist('StudentNumber[]')
    parts = request.form.getlist('part[]')
    emails = request.form.getlist('email[]')
    mbtis = request.form.getlist('mbti[]')

    images = [
        student_images.get(student_number, "https://raw.githubusercontent.com/CSID-DGU/2024-2-OSSPrac-azaping-01/main/pic/default.jpg")
        for student_number in student_numbers
    ]


    # 학생 정보를 zip으로 묶어 템플릿에 전달
    students = zip(names, departments, student_numbers, parts, emails, mbtis, images)
    return render_template('app_result.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)
