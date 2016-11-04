
from bs4 import BeautifulSoup
from os import path
import pandas as pd

class Parser(object):

    def __init__(self, schema):

        self._schema = schema

        self._soups = {}
        for key in self.schema.schema.keys():
            with open(self._schema.local(key), 'rb') as f:
                self._soups[key] = BeautifulSoup(f.read(), 'lxml')

    @property
    def schema(self):
        return self._schema

    @property
    def soups(self):
        return self._soups

    @property
    def id(self):
        stats = self.soups['stats']
        item = stats.select_one('items > item')
        return int(item['id'])

    @property
    def primary_name(self):
        stats = self.soups['stats']
        primary_name = stats.select_one('items > item > name[type=primary]')
        return primary_name['value']

    @property
    def description(self):
        stats = self.soups['stats']
        description = stats.select_one('items > item > description')
        return description.get_text()

    def flatten(self):

        row = \
        {
            'id': self.id
            , 'primary_name': self.primary_name 
            , 'description': self.description
        }

        return row

    #      'primary_name': 'name[type=primary]'
    # , 'alternate_names': 'name[type=alternate]'
    # , 'suggested_num_players': 'poll[name=suggested_numplayers] > results'
    # , 'language_dependence': 'poll[name=language_dependence] > results > result'
    # , 'suggested_player_age': 'poll[name=suggested_playerage] > results > result'
    # , 'description': 'description'
    # , 'year_published': 'yearpublished'
    # , 'min_players' : 'minplayers'
    # , 'max_players' : 'maxplayers'
    # , 'playing_time' : 'playingtime'
    # , 'min_playing_time': 'minplaytime'
    # , 'max_playing_time': 'maxplaytime'
    # , 'min_age': 'minage'
    # , 'categories': 'link[type=boardgamecategory]'
    # , 'mechanics': 'link[type=boardgamemechanic]'
    # , 'families': 'link[type=boardgamefamily]'
    # , 'designers': 'link[type=boardgamedesigner]'
    # , 'artists': 'link[type=boardgameartist]'
    # , 'publishers': 'link[type=boardgamepublisher]'
    # , 'users_rated': 'statistics > ratings > usersrated'
    # , 'rating_mean': 'statistics > ratings > average'
    # , 'bayes_average_rating': 'statistics > ratings > bayesaverage'
    # , 'ranks': 'statistics > ratings > ranks > rank'
    # , 'rating_sd': 'statistics > ratings > stddev'
    # , 'rating_median': 'statistics > ratings > median'
    # , 'owned': 'statistics > ratings > owned'
    # , 'trading': 'statistics > ratings > trading'
    # , 'wanting': 'statistics > ratings > wanting'
    # , 'wishing': 'statistics > ratings > wishing'
    # , 'num_comments': 'statistics > ratings > numcomments'
    # , 'num_weights': 'statistics > ratings > numweights'
    # , 'weight_average': 'statistics > ratings > averageweight'