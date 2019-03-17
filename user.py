import requests
import logging
import bs4
from os import environ
from profile import get_profile_data

from lib import exception


class User(object):
    def __init__(self, uname):
        '''
            Constructor for the User class taking the username
        '''
        self.userName = uname
        self.isLoggedIn = False
        self._fetchData(uname)

    def _fetchData(self, uname):
        data = get_profile_data(uname)
        self.rating = data[0]
        self.title = data[1]
        self.max_rating = data[2]

    def _authenticator(func):
        def wrapper(self, *args, **kargs):
            if not self.isLoggedIn:
                raise exception.NotLoggedIn('Function only available when logged in')
            return func(self, *args, **kargs)
        return wrapper

    def login(self, passW='not_given'):
        '''
            Used to login to the Spoj,
            its necessary for submitting the problem
        '''
        self.__session = requests.Session()
        if(passW=='not_given'):
            import getpass
            passW=getpass.getpass('enter password : ')

        loginDat = {'handle': self.userName, 'password': passW}
        resp = self.__session.post('http://codeforces.com/enter?back=%2F', data=loginDat)
        if 'forbidden' in resp.text:
            print(resp.text)
            self.__session.close()
            print('Invalid handle or password')
#            raise exception.LoginFalied('Invalid handle or password')
            return
        self.isLoggedIn = True

    def close(self):
        self.__session.close()
        self.isLoggedIn = False

