#!/usr/bin/python3
""" uses requests package to request url response"""
import requests
import sys

if __name__ == '__main__':
    variable = {'q': ''}
    if len(sys.argv) > 1:
        variable = {'q': sys.argv[1]}

    req = requests.post('http://0.0.0.0:5000/search_user', data=variable)
    try:
        derulo = req.json()
        if derulo:
            print('[{}] {}'.format(derulo.get('id'), derulo.get('name')))
        else:
            print('No result')
    except:
        print('Not a valid JSON')
