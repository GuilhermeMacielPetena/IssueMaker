from flask import Flask, request, jsonify, json 
from issue import Issue

app = Flask(__name__)

@app.route('/issue', methods=['POST'])
def addIssueToRepository():
    data = request.get_json()

    title = data['title']
    body = data['body']

    Issue.make_github_issue(title, body)

    return jsonify(data)
 
    
if __name__ == '__main__':
    app.run(debug=True)