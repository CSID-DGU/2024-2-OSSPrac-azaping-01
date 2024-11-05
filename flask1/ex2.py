# 파이썬 파일이 직접 스크립트로 실행될 때만 flask 애플리케이션을 실행
from flask import Flask

app = Flask(__name__)

@app.route('/') # default URL
def hello_world():
    return ('Hello World!')

@app.route('/page') # page URL
def print_page():
    return ('This is page')

if __name__ == '__main__':
   app.run()

# 만약?
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8000)

# 만약?
if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=8000)
