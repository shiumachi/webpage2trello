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


    webpage2trello
    ~~~~~~~~~~~~~~

    Create Trello cards from a list of URLs.

    usage:
        - add URL list to file.
        - change config file to add Trello API token, key, and List ID which you put cards into.
        - run `python main.py -i inputfile -c configfile`.


"""

import argparse
import configparser
import time

from webpage import Webpage
from trello import Trello

# time interval for web crawling (sec)
CRAWL_TIME_INTERVAL = 5


def parse_args():
    """ Parse and return command line args """

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_path", required=True)
    parser.add_argument("-c", "--config", required=True)
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    config = configparser.ConfigParser()
    config.read(args.config)

    # load URL list file
    urls = []
    with open(args.input_path) as f:
        for line in f:
            urls.append(line.strip())

    # parse web pages
    webpages = []
    for url in urls:
        webpages.append(Webpage.factory(url))
        time.sleep(CRAWL_TIME_INTERVAL)

    trello = Trello(config['trello']['api_key'],
                    config['trello']['api_token'],
                    config['trello']['t_list_id']
                    )

    # put data into Trello
    for q in webpages:
        trello.create_card(q.title, q.url)
