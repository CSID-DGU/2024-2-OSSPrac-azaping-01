from flask import Flask, request, render_template

app = Flask(__name__)

# 최초 메인 페이지를 보여주는 루트 경로
@app.route('/')
def index():
    return render_template('app_index.html')  # 위 HTML 코드를 form.html 파일로 저장해야 합니다

# 학생 정보를 입력하는 경로

@app.route('/input')
def input():
    return render_template('app_input.html')

# 제출된 데이터를 처리하여 출력하는 경로
@app.route('/result', methods=['POST'])
def result():
    # form 데이터 가져오기
    names = request.form.getlist('name[]')
    student_numbers = request.form.getlist('StudentNumber[]')
    parts = request.form.getlist('part[]')
    genders = request.form.getlist('gender[]')
    emails = request.form.getlist('email[]')
    mbtis = request.form.getlist('mbti[]')

    # 컴퓨터 언어는 체크박스 배열로 수집
    languages_all = request.form.getlist('languages[]')
    languages_per_person = [languages_all[i:i+5] for i in range(0, len(languages_all), 5)]

    # 데이터 템플릿으로 전달
    students = zip(names, student_numbers, parts, genders, languages_per_person, emails, mbtis)
    return render_template('app_result.html', students=students)

@app.route('/contact')
def contact_info():
    return render_template('app_contact.html')

if __name__ == '__main__':
    app.run(debug=True)