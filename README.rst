================
 webpage2trello
================

What's this?
============

This tool extracts title from a list of web pages and create a new Trello card with the title.


Version and Requirement
=======================

- Python 3
- bs4

How to Use
==========

Get Trello API Key, Token, and List name
----------------------------------------

Go `https://trello.com/1/appKey/generate` to generate a new key.

Then run ``https://trello.com/1/authorize?key=YOUR_API_KEY&name=YOUR+TOKEN+NAME&expiration=30days&response_type=token&scope=read,write`` from your web browser to get a new API token.

Next, go to your board and get the board ID from URL of the page. Run the following python script to check your list ID.

::

  import urllib.request
  import json
  url = "https://api.trello.com/1/boards/YOUR_BOARD_ID/lists?key=YOUR_API_KEY&token=YOUR_API_TOKEN"
  response = urllib.request.urlopen(url)
  res_json = json.loads(response.read().decode())
  print(res_json)


Finally, create a new config.ini file with the following format.

::

  [trello]
  api_key = YOUR_API_KEY
  api_token = YOUR_API_TOKEN
  t_board = YOUR_BOARD_ID
  t_list_id = YOUR_LIST_ID


Create Web pages List
---------------------

Create a new list with the following format:

::

  TARGET_URL_1
  TARGET_URL_2
  ...


Run command
-----------

Run the following command and you can create new Trello cards.

::

  python main.py -i WEB_PAGE_LIST -c config.ini



