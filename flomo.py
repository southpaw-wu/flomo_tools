import requests
import json
import re
import os

if __name__ == '__main__':
    api = os.getenv('POPCLIP_OPTION_API')
    content = os.getenv('POPCLIP_TEXT')

    command = 'osascript flomo.scpt'
    output = os.popen(command)
    line = output.readlines()
    if len(line)!=0 :
        resultStr = line[-1]
        result = resultStr.split(' ')

        tags = ''
        for tag in result:
           tags = tags + '#' + tag + ' '
        tags = tags[:-1]
        content = tags + content

        session = requests.session()
        response = session.post(
                api,
                headers={'Content-Type': 'application/json'},
                json={'content': content}
                )
 
