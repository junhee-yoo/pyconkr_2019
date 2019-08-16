import re
import requests
import bs4
from cliff import lister


class TutorialSub2Command2(lister.Lister):
    _description = "Tutorial Subcommand1 Command2"

    def get_parser(self, prog_name):
        return super(TutorialSub2Command2, self).get_parser(prog_name)

    def take_action(self, parsed_args):
        resp = requests.get('https://weather.naver.com')
        bs = bs4.BeautifulSoup(resp.content, 'html.parser')
        # tags = bs.find_all('tr', attrs={'class': 'now'})
        # date = tags[0].contents[1].contents[2].contents[0][1:-1]
        # temperature = tags[0].contents[5].contents[1].contents[1].contents[0].contents[0]
        # l = [(date, temperature)]
        l = list()

        tags = bs.find_all('tr', attrs={'class': 'line'})
        for tag in tags:
            date = tag.contents[1].contents[2].contents[0][1:-1]
            summary = tag.contents[7].contents[0]
            temperature = tag.contents[7].contents[1].contents[1].contents[0].contents[0]
            rain = tag.contents[7].contents[1].contents[3].contents[0].contents[0] + '%'
            l.append((date, summary, temperature, rain))

        return ('date', 'summary', 'temperature', 'rain'), l
