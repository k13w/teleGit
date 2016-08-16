#!/usr/bin/env python
# -*- coding:utf-8 -*-

from requests import get
from json import loads
from argparse import ArgumentParser


class GitHub:

    def get_repos(self, user):
        self.msg = ""
        req = loads(get('https://api.github.com/users/' +
                        user + '/repos').text)
        self.msg += '\nRepositorys of user.'
        for i in range(len(req)):
            self.msg += '\n\nName repository: ' + str(req[i]['name'])
            self.msg += '\nDescription repository: ' + \
                str(req[i]['description'])
            self.msg += '\nURL repository: ' + str(req[i]['html_url'])
            self.msg += '\nStars: total: ' + \
                str(req[i]['stargazers_count'])
            self.msg += '\nForks total: ' + \
                str(req[i]['forks_count'])
        return self.msg

    def get_info(self, user):
        self.msg = ""
        req = loads(get('https://api.github.com/users/' + user).text)
        self.msg += '\nInformation of user:\n'
        self.msg += '\nName: ' + str(req['name'])
        self.msg += '\nEmail: ' + str(req['email'])
        self.msg += '\nCompany: ' + str(req['company'])
        self.msg += '\nBlog: ' + str(req['blog'])
        self.msg += '\nBio: ' + str(req['bio'])
        self.msg += '\nLocation: ' + str(req['location'])
        self.msg += '\nPublic repository: ' + str(req['public_repos'])
        self.msg += '\nFollowers: ' + str(req['followers']) + '\n'
        return self.msg

    def arguments(self):
        self.user = GitHub()
        self.parser = ArgumentParser()
        self.parser.add_argument('--repos', dest='repos', action='store_true',
                                 help='List all repository.')
        self.parser.add_argument('--user', dest='user', action='store',
                                 required=True, help='Parameter for set user.')
        self.parser.add_argument('--info', dest='info', action='store_true',
                                 help='Parameter for to get info of user')
        self.parser.add_argument('--all', dest='all', action='store_true',
                                 help='Parameter for to define all options')
        self.args = self.parser.parse_args()
        if self.args.user and self.args.info:
            print(self.user.GetInfo(self.args.user))
        elif self.args.user and self.args.repos:
            print(self.user.GetRepos(self.args.user))
        elif self.args.user and self.args.all:
            print(self.user.GetRepos(self.args.user))
            print(self.user.GetInfo(self.args.user))
        else:
            print('Use --info, --repos or --all.')
