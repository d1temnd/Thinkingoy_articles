from flask import Flask, request, Response, render_template, abort
import os

app = Flask(__name__)

base_path = 'files'


@app.route('/')
def index():
    files = os.listdir(base_path)  

    return render_template('index.html', files=files)


@app.route('/view')
def view_file():
    
    file_name = request.args.get('file')

    # Определяем базовый путь
    full_path = os.path.join(base_path, file_name)
    print(full_path)


    try:
        # Читаем файл и возвращаем его содержимое
        with open(full_path, 'r') as file:
            content = file.read()
            return Response(content, mimetype='text/plain')
    except FileNotFoundError:
        return "Файл не найден!"
    except Exception as e:
        return f"Произошла ошибка: {str(e)}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
