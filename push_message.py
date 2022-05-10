#! /usr/bin/env python3

#

__author__ = "Aaron Castro"
__author_email__ = "aaron.castro.sanchez@outlook.com"
__author_nick__ = "i686"
__copyright__ = "Aaron Castro"
__license__ = "MIT"

import sys, getopt, argparse, requests

def telegram_bot_sendtext(message,token,chatid):
        sendtext = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + chatid + '&parse_mode=Markdown&text=' + message
        response = requests.get(sendtext)

        return response.json()

if __name__ == '__main__':
        parser = argparse.ArgumentParser()
        parser.add_argument("-m", "--message")
        parser.add_argument("-t", "--token")
        parser.add_argument("-c", "--chatid")
        args = parser.parse_args()

        if (args.message) is not None and (args.token) is not None and (args.chatid) is not None:
                telegram_bot_sendtext(args.message,args.token,args.chatid)
        else:
                print("Some arguments are missing or invalid")
