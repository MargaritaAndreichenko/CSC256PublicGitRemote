import pytest
import requests

url_ddg = "https://api.duckduckgo.com"


presidents = ('Washington', 'Adams', 'Jefferson', 'Madison', 'Monroe','Adams', 'Jackson', 'Van Buren', 'Harrison', 'Tyler', 'Polk', 'Taylor', 'Fillmore', 'Pierce', 'Buchanan', 'Lincoln', 'Johnson','Grant', 'Hayes','Garfield', 
              'Arthur',  'Cleveland', 'Harrison', 'Cleveland', 'McKinley', 'Roosevelt','Taft', 'Wilson', 'Harding','Coolidge','Hoover','Roosevelt','Truman', 'Eisenhower', 'Kennedy', 'Johnson', 'Nixon', 'Ford', 'Carter', 'Reagan','Bush', 'Clinton', 'Bush', 'Obama', 'Trump')


def test_presidents():
    resp = requests.get(url_ddg + "/?q=presidents of the united states&format=json")
    rsp_data = resp.json()

    text = ''
    for it in rsp_data['RelatedTopics']:
        text += it['Text']

    for president in presidents:
        assert president in text
