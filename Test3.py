from flask import Flask, request, render_template_string

# 1. Flask 앱을 생성합니다.
app = Flask(__name__)

# 2. 웹페이지의 HTML 템플릿을 만듭니다.
# <h1>은 제목, <form>은 입력을 받는 양식입니다.
# {{ greeting_message }} 부분에 인사말이 표시됩니다.
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>이름 입력기</title>
</head>
<body>
    <h2>이름을 입력하면 인사해 드려요!</h2>
    
    <form method="POST" action="/">
        <label for="name">이름:</label>
        <input type="text" id="name" name="user_name">
        <input type="submit" value="제출">
    </form>
    
    <hr>
    
    {% if greeting_message %}
        <h3>{{ greeting_message }}</h3>
    {% endif %}

</body>
</html>
"""

# 3. 브라우저가 "/" 주소로 접속할 때 처리할 함수를 정의합니다.
# GET (그냥 접속)과 POST (폼 제출) 방식을 모두 허용합니다.
@app.route("/", methods=["GET", "POST"])
def index():
    greeting = ""  # 기본 인사말은 비워둡니다.

    # 4. 만약 사용자가 폼을 '제출(POST)'했다면,
    if request.method == "POST":
        # 폼에서 'user_name'으로 보낸 값을 가져옵니다.
        name = request.form["user_name"]
        
        # 인사말을 만듭니다.
        if name:
            greeting = f"안녕하세요, {name}님!"
        else:
            greeting = "이름을 입력해주세요."
            
    # 5. HTML 템플릿에 인사말을 채워서 웹페이지를 보여줍니다.
    # (GET 요청일 경우 greeting=""이 전달됩니다.)
    return render_template_string(HTML_TEMPLATE, greeting_message=greeting)


# 6. 이 파일을 직접 실행했을 때 웹 서버를 시작합니다.
if __name__ == "__main__":
    app.run(debug=True)