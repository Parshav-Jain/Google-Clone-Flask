from flask import Flask , render_template

#This is the api work for the google clone that is giving the 
# result of api in our website
api_key = "................"
from apiclient.discovery import build

result = build("customsearch","v1",developerKey=api_key).cse()
query = 'Wikipedia'
resource = result.list(q = query,cx = '............').execute()
resource_items = resource['items']

#The api work ends here .

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('google.html',query = query)

@app.route('/search/<query>')
def search(query):
    
    for item in resource_items:
        title = item['title']
        link = item['link']
        snippet = item['snippet']
        items = [title,link,snippet]
        #print(title , link)
        #print('\n')
        return render_template('search_results.html',title = title , link = link,snippet = snippet,resource_items = resource_items,resource = resource,items  = items,query = query)
app.run(debug=True)
