# -*- coding: utf-8 -*-
"""
   Copyright 2015 Sho Shimauchi

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.


    trello
    ~~~~~~

    Handler of Trello commands.

"""

import argparse
import configparser
import urllib.parse
import urllib.request

TRELLO_BASE_URL = "https://api.trello.com/1"


class Trello(object):

    api_key = None
    api_token = None
    list_id = None

    def __init__(self, api_key, api_token, list_id):
        self.api_key = api_key
        self.api_token = api_token
        self.list_id = list_id

    def create_card(self, name, url):
        post_url = "{0}/lists/{1}/cards?key={2}&token={3}".format(TRELLO_BASE_URL,
                                                                  self.list_id,
                                                                  self.api_key,
                                                                  self.api_token
                                                                  )
        d = {"name": name, "desc": url}
        post_data = urllib.parse.urlencode(d).encode('utf-8')
        response = urllib.request.urlopen(post_url, data=post_data)
        return response


def parse_args():
    """ Parse and return command line args """

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", required=True)
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    config = configparser.ConfigParser()
    config.read(args.config)
    trello = Trello(config['trello']['api_key'],
                    config['trello']['api_token'],
                    config['trello']['t_list_id']
                    )

    trello.create_card("test card", "test desc")
