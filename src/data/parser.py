
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
        try:
            stats = self.soups['stats']
            selector = 'items > item'
            item = stats.select_one(selector)
            return item['id']
        except TypeError as e:
            return None

    @property
    def primary_name(self):
        try:
            stats = self.soups['stats']
            selector = 'items > item > name[type=primary]'
            primary_name = stats.select_one(selector)
            return primary_name['value']
        except TypeError as e:
            return None

    @property
    def alternate_names(self):
        try:
            stats = self.soups['stats']
            selector = 'items > item > name[type=alternate]'
            alternate_names = stats.select(selector)
            return [alternate_name['value'] for alternate_name in alternate_names]
        except TypeError as e:
            return []

    @property
    def suggested_num_players(self):
        try:
            stats = self.soups['stats']
            selector = 'items > item > poll[name=suggested_numplayers] > results'
            poll = Poll()
            for result_set in stats.select(selector):
                for result in result_set.select('result'):
                    poll[result['value']][result_set['numplayers']] = result['numvotes']
            return poll.votes
        except TypeError as e:
            return Poll().votes

    @property
    def language_dependence(self):
        try:
            stats = self.soups['stats']
            selector = 'items > item > poll[name=language_dependence] > results > result'
            poll = {}
            for result in stats.select(selector):
                poll[result['level']] = result['numvotes']
            return poll
        except TypeError as e:
            return {}

    @property
    def suggested_player_age(self):
        try:
            stats = self.soups['stats']
            selector = 'items > item > poll[name=suggested_playerage] > results > result'
            poll = {}
            for result in stats.select(selector):
                poll[result['value']] = result['numvotes']
            return poll
        except TypeError as e:
            return {}

    @property
    def description(self):
        try:
            stats = self.soups['stats']
            selector = 'items > item > description'
            description = stats.select_one(selector)
            return description.get_text()
        except TypeError as e:
            return None

    @property
    def year_published(self):
        try:
            stats = self.soups['stats']
            selector = 'items > item > yearpublished'
            year_published = stats.select_one(selector)
            return year_published['value']
        except TypeError as e:
            return None

    @property
    def min_players(self):
        try:
            stats = self.soups['stats']
            selector = 'items > item > minplayers'
            min_players = stats.select_one(selector)
            return min_players['value']
        except TypeError as e:
            return None

    @property
    def max_players(self):
        try:
            stats = self.soups['stats']
            selector = 'items > item > maxplayers'
            max_players = stats.select_one(selector)
            return max_players['value']
        except TypeError as e:
            return None

    @property
    def playing_time(self):
        try:
            stats = self.soups['stats']
            selector = 'items > item > playingtime'
            playing_time = stats.select_one(selector)
            return playing_time['value']
        except TypeError as e:
            return None

    @property
    def min_playing_time(self):
        try:
            stats = self.soups['stats']
            selector = 'items > item > minplaytime'
            min_playing_time = stats.select_one(selector)
            return min_playing_time['value']
        except TypeError as e:
            return None

    @property
    def max_playing_time(self):
        try:
            stats = self.soups['stats']
            selector = 'items > item > maxplaytime'
            max_playing_time = stats.select_one(selector)
            return max_playing_time['value']
        except TypeError as e:
            return None

    @property
    def min_age(self):
        try:
            stats = self.soups['stats']
            selector = 'items > item > minage'
            min_age = stats.select_one(selector)
            return min_age['value']
        except TypeError as e:
            return None

    @property
    def categories(self):
        try:
            stats = self.soups['stats']
            selector = 'items > item > link[type=boardgamecategory]'
            categories = stats.select(selector)
            return [category['value'] for category in categories]
        except TypeError as e:
            return []

    @property
    def mechanics(self):
        try:
            stats = self.soups['stats']
            selector = 'items > item > link[type=boardgamemechanic]'
            mechanics = stats.select(selector)
            return [mechanic['value'] for mechanic in mechanics]
        except TypeError as e:
            return []

    @property
    def families(self):
        try:
            stats = self.soups['stats']
            selector = 'items > item > link[type=boardgamefamily]'
            families = stats.select(selector)
            return [family['value'] for family in families]
        except TypeError as e:
            return []

    @property
    def designers(self):
        try:
            stats = self.soups['stats']
            selector = 'items > item > link[type=boardgamedesigner]'
            designers = stats.select(selector)
            return [designer['value'] for designer in designers]
        except TypeError as e:
            return []

    @property
    def artists(self):
        try:
            stats = self.soups['stats']
            selector = 'items > item > link[type=boardgameartist]'
            artists = stats.select(selector)
            return [artist['value'] for artist in artists]
        except TypeError as e:
            return []

    @property
    def publishers(self):
        try:
            stats = self.soups['stats']
            selector = 'items > item > link[type=boardgamepublisher]'
            publishers = stats.select(selector)
            return [publisher['value'] for publisher in publishers]
        except TypeError as e:
            return []

    @property
    def users_rated(self):
        try:
            stats = self.soups['stats']
            selector = 'items > item > statistics > ratings > usersrated'
            users_rated = stats.select_one(selector)
            return users_rated['value']
        except TypeError as e:
            return None

    @property
    def average_rating(self):
        try:
            stats = self.soups['stats']
            selector = 'items > item > statistics > ratings > average'
            average_rating = stats.select_one(selector)
            return average_rating['value']  
        except TypeError as e: 
            return None

    @property
    def bayes_average_rating(self):
        try:
            stats = self.soups['stats']
            selector = 'items > item > statistics > ratings > bayesaverage'
            bayes_average_rating = stats.select_one(selector)
            return bayes_average_rating['value']
        except TypeError as e:
            return None

    @property
    def ranks(self):
        try:
            stats = self.soups['stats']
            selector = 'items > item > statistics > ratings > ranks > rank'
            ranks = {}
            for rank in stats.select(selector):
                ranks[rank['friendlyname']] = rank['value']
            return ranks
        except TypeError as e:
            return {}

    @property
    def rating_standard_deviation(self):
        try:
            stats = self.soups['stats']
            selector = 'items > item > statistics > ratings > stddev'
            rating_standard_deviation = stats.select_one(selector)
            return rating_standard_deviation['value']  
        except TypeError as e:
            return None

    @property
    def median_rating(self):
        try:
            stats = self.soups['stats']
            selector = 'items > item > statistics > ratings > median'
            median_rating = stats.select_one(selector)
            return median_rating['value'] 
        except TypeError as e:
            return None

    @property
    def owned(self):
        try:
            stats = self.soups['stats']
            selector = 'items > item > statistics > ratings > owned'
            owned = stats.select_one(selector)
            return owned['value']
        except TypeError as e:
            return None

    @property
    def trading(self):
        try:
            stats = self.soups['stats']
            selector = 'items > item > statistics > ratings > trading'
            trading = stats.select_one(selector)
            return trading['value']
        except TypeError as e:
            return None

    @property
    def wanting(self):
        try:
            stats = self.soups['stats']
            selector = 'items > item > statistics > ratings > wanting'
            wanting = stats.select_one(selector)
            return wanting['value']  
        except TypeError as e:
            return None

    @property
    def wishing(self):
        try:
            stats = self.soups['stats']
            selector = 'items > item > statistics > ratings > wishing'
            wishing = stats.select_one(selector)
            return wishing['value']   
        except TypeError as e:
            return None

    @property
    def num_comments(self):
        try:
            stats = self.soups['stats']
            selector = 'items > item > statistics > ratings > numcomments'
            num_comments = stats.select_one(selector)
            return num_comments['value']
        except TypeError as e:
            return None

    @property
    def num_weights(self):
        try:
            stats = self.soups['stats']
            selector = 'items > item > statistics > ratings > numweights'
            num_weights = stats.select_one(selector)
            return num_weights['value']  
        except TypeError as e:
            return None

    @property
    def average_weight(self):
        try:
            stats = self.soups['stats']
            selector = 'items > item > statistics > ratings > averageweight'
            average_weight = stats.select_one(selector)
            return average_weight['value']      
        except TypeError as e:
            return None

    def flatten(self):

        row = \
        {
            'id': self.id
            , 'primary_name': self.primary_name
            , 'alternate_names': self.alternate_names
            , 'description': self.description
            , 'suggested_num_players': self.suggested_num_players
            , 'language_dependence': self.language_dependence
            , 'suggested_player_age': self.suggested_player_age
            , 'year_published': self.year_published
            , 'min_players': self.min_players
            , 'max_players': self.max_players
            , 'playing_time': self.playing_time
            , 'min_playing_time': self.min_playing_time
            , 'max_playing_time': self.max_playing_time
            , 'min_age': self.min_age
            , 'categories': self.categories
            , 'mechanics': self.mechanics
            , 'families': self.families
            , 'artists': self.artists
            , 'designers': self.designers
            , 'publishers': self.publishers
            , 'users_rated': self.users_rated
            , 'average_rating': self.average_rating
            , 'bayes_average_rating': self.bayes_average_rating
            , 'ranks': self.ranks
            , 'rating_standard_deviation': self.rating_standard_deviation
            , 'median_rating': self.median_rating
            , 'owned': self.owned
            , 'trading': self.trading
            , 'wanting': self.wanting
            , 'wishing': self.wishing
            , 'num_comments': self.num_comments
            , 'num_weights': self.num_weights
            , 'average_weight': self.average_weight
        }

        return row


class Poll(object):
        
    def __init__(self):
        self.votes = {}
        self.votes['Not Recommended'] = {}
        self.votes['Recommended'] = {}
        self.votes['Best'] = {}

    def __iter__(self):
        return self.votes.iteritems()

    def __getitem__(self, key):
        return self.votes[key]

    def __setitem__(self, key, value):
        self.votes[key] = value
