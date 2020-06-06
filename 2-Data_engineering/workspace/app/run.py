
import json
import plotly
import pandas as pd
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from flask import Flask
from flask import render_template, request, jsonify
from plotly.graph_objs import Bar
from joblib import load
from sqlalchemy import create_engine
import re
from wordcloud import WordCloud
#need to update plotly package
import plotly.express as px


nltk.download('stopwords')

app = Flask(__name__)


def tokenize(text):
    # normalize case and remove punctuation
    text = re.sub(r"[^a-zA-Z0-9]", " ", text.lower())
    # tokenize text
    tokens = word_tokenize(text)
    # lemmatize and remove stop words
    lemmatizer = WordNetLemmatizer()
    stop_words = stopwords.words("english")
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return tokens

# load data
engine = create_engine('sqlite:///data/DisasterResponse.db')
df = pd.read_sql_table('messages', engine)


# load model
model = load('models/classifier.pkl')


# index webpage displays cool visuals and receives user input text for model
@app.route('/')
@app.route('/index')
def index():
    
    # extract data needed for visuals
    # Gragh one data extraction: Bar charts
    category_counts=df.iloc[:,3:].sum().sort_values(ascending=False)
    categories=list(category_counts.index)    
    
    #Graph two data extraction: word cloud
    text=' '.join(df.message.tolist())
    token=tokenize(text)
    all_token=' '.join(token)
    wordcloud = WordCloud(max_font_size=70, max_words=200, background_color="black").generate(all_token)
    
    # create visuals
    # TODO: Below is an example - modify to create your own visuals
    graphs = [
        #graph one
        {
            'data': [
                Bar(
                    x=categories,
                    y=category_counts,
                    text=category_counts,
                    textposition='outside'
                )
            ],

            'layout': {
                'title': 'Distribution of Message Categories',
                'yaxis': {
                    'title': "Count"
                },
                'xaxis': {
                    'title': "Category"
                }
            }
        },
        #graph two
        {
            'data':[
                px.imshow(wordcloud)
            ],
            
            'layout':{
                'title': 'Word Cloud of All Messages'
            }
        }
    ]
    
    # encode plotly graphs in JSON
    ids = ["graph-{}".format(i) for i, _ in enumerate(graphs)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    
    # render web page with plotly graphs
    return render_template('master.html', ids=ids, graphJSON=graphJSON)


# web page that handles user query and displays model results
@app.route('/go')
def go():
    # save user input in query
    query = request.args.get('query', '') 

    # use model to predict classification for query
    classification_labels = model.predict([query])[0]
    classification_results = dict(zip(df.columns[2:], classification_labels))

    # This will render the go.html Please see that file. 
    return render_template(
        'go.html',
        query=query,
        classification_result=classification_results
    )


def main():
    app.run(host='0.0.0.0', port=3001, debug=True)


if __name__ == '__main__':
    main()