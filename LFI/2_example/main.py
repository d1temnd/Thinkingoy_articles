from flask import Flask, request, render_template_string, abort, render_template, Response
import urllib.parse
import os

app = Flask(__name__)

base_path = "files"


@app.route('/')
def index():
    files = os.listdir(base_path)  # сами файлы пользовтелей

    return render_template('index.html', files=files)


@app.route('/file')
def file():
    filename = request.args.get('file')

    # Фильтрация на символ "/"
    if '/' in filename or '\\' in filename:
        return f'нельня использовать / и \\'


    # Кодирование символа "/" для обхода
    if filename:
        # Декодируем URL
        filename = urllib.parse.unquote(filename)
        filename = urllib.parse.unquote(filename)

        full_path = os.path.join(base_path, filename)
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


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
