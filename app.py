from flask import Flask, render_template
import pickle

df = pickle.load(open('./model/model.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', 
                            book_name = list(df['Book-Title'].values),
                            book_author = list(df['Book-Author'].values),
                            image = list(df['Image-URL-M'].values),
                            votes = list(df['# Ratings'].values),
                            ratings = list(df['Avg Rating'].values),
                            )

if __name__ == '__main__':
    app.run(debug = True)
