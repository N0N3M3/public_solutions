from flask import Flask, render_template

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ЫАЫАЫАЫАЫАЫАЫАЫАЫАЫАЫАЫАЫАЫА'


@app.route('/')
def index():
    return render_template('base.html', title='Заготовка')


@app.route('/training/<prof>')
def training(prof: str):
    if 'инженер' in prof or 'строитель' in prof:
        return render_template('index.html', title='Домашняя страница', name='Инженерные тренажеры',
                               path_to_photo='/static/images/daabo88-a4e0431e-c8ae-477f-bd89-0c5923cc45ee.png')
    else:
        return render_template('index.html', title='Домашняя страница', name='Научные симуляторы',
                               path_to_photo='/static/images/7_4_1.jpg')


if __name__ == '__main__':
    app.run()
