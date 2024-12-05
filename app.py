from flask import Flask, request, render_template, redirect, url_for
import uuid

app = Flask(__name__)

valid_hwids = {}

@app.route('/')
def home():
    return "Bạn phải vượt qua link để lấy HWID."

@app.route('/generate')
def generate():
    hwid = str(uuid.uuid4())
    valid_hwids[hwid] = False  # False indicates hwid has not been used yet
    return redirect(url_for('show_hwid', hwid=hwid))

@app.route('/show')
def show_hwid():
    hwid = request.args.get('hwid')
    if hwid not in valid_hwids or valid_hwids[hwid]:
        return "HWID này đã được sử dụng hoặc không hợp lệ. Vui lòng tạo một HWID mới từ bước đầu."

    valid_hwids[hwid] = True  # Mark hwid as used

    return render_template('index.html', hwid=hwid)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Lấy cổng từ biến môi trường hoặc mặc định là 5000
    app.run(host='0.0.0.0', port=port, debug=True)
