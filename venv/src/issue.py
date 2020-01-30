import os
import json
import requests
from   authentication import Authentication as AUTH

class Issue():

    def make_github_issue(title, body=None):
        url = 'https://api.github.com/repos/%s/%s/issues' % (AUTH.REPO_OWNER, AUTH.REPO_NAME)
        session = requests.Session()
        session.auth = (AUTH.USERNAME, AUTH.PASSWORD)
        issue = {'title': title,
                'body': body}
        addIssueToRepository = session.post(url, json.dumps(issue))
        if addIssueToRepository.status_code == 201:
            print ('Successfully created Issue {0:s}'.format(title))
        else:
            print ('Could not create Issue {0:s}'.format(title))
            print ('Response:', addIssueToRepository.content)