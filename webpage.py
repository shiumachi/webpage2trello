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


    webpage
    ~~~~~~~

    Represents web page.

"""

import argparse
import requests
from bs4 import BeautifulSoup


class Webpage(object):

    """ Web page.
    """

    title = None
    url = None

    def __init__(self, title=None, url=None):
        self.title = title
        self.url = url
        return

    def __str__(self):
        s = "title: {0}, url: {1}".format(self.title, self.url)
        return s

    @classmethod
    def factory(self, url):
        """ Create a new instance from URL.

        url: URL of a web page

        return: an instance of Webpage
        """
        soup = BeautifulSoup(requests.get(url).text, "lxml")
        title = soup.title.text
        return Webpage(title=title, url=url)


def parse_args():
    """ Parse and return command line args """

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_path", required=True)
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    urls = []

    with open(args.input_path) as f:
        for line in f:
            urls.append(line.strip())

    webpages = []

    for url in urls:
        webpages.append(Webpage.factory(url))

    for webpage in webpages:
        print(webpage)
