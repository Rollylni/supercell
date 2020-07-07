import requests
import json

class ResponseObject:
    """
    :param response: method response
    :type response: dict
    
    :ivar response: dict
    """
    response = {}
    
    def __init__(self, response={}):
        self.response = response
    
    def get(self, key):
        """
        :param key: str
        :returns: mixed
        """
        keys = key.split(".")
        if len(keys) > 1:
            response = self.response[keys.pop(0)]
            for k in keys:
                if isinstance(response, (dict, list, tuple)) and k in response:
                    response = response[k]
                else:
                    return None
            return response   
        else:
            return self.response.get(key)
            
    def __getitem__(self, key):
        return self.get(key)

class SupercellAPI:
    """
    :param token: your access token
    :type token: str
    
    :ivar TOKEN: str
    :ivar API_HOST: str
    :ivar API_NAME: str
    :ivar VERSION: str
    :ivar LOGGING: bool
    """
    TOKEN = None
    API_HOST = None
    API_NAME = "Supercell"
    VERSION = "v1"
    LOGGING = True
    
    def __init__(self, token=None):
        self.TOKEN = token
        
    def get_players(self, tags):
        """ Get players information
        
        :param tags: Tag of the players
        :type tags: (list, tuple, dict)
        
        :returns: list
        """
        players = []
        for tag in tags:
            player = self.get_player(tag)
            players.append(player.response)
            
        return players
        
    def valid_tag(self, tag):
        """
        :param tag: str
        :returns: str
        """
        return tag.replace("#", "%23")
       
    def log(self, message=None, method=None):
        """
        :param message: str
        :param method: str
        """
        if not self.LOGGING:
            return
        if method is not None:
            print("[{}] Method {} Failed!".format(self.API_NAME, method))
        if message is not None:    
            print("[{}] {}".format(self.API_NAME, message))
        
    def get_host(self):
        """
        :returns: str
        """
        return "https://{}/{}/".format(self.API_HOST, self.VERSION)
        
    def request(self, method, params={}, log=True):
        """
        :param method: api method
        :type method: str
        
        :param params: method parameters
        :type params: dict
        
        :returns: ResponseObject
        """
        headers = {
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + self.TOKEN
        }
        if self.LOGGING:
            self.LOGGING = log
        
        try:
            response = requests.get(self.get_host() + method, params=params, headers=headers)
            if not response.ok:
                response.raise_for_status()
            response = response.json()
        except requests.exceptions.HTTPError as e:
            self.log("HTTP Error: {}".format(e))
            try:
                response = response.json()
            except:
                response = []
            if "reason" in response:
                self.log("API Reason: {}, {}".format(response["reason"], response.get("message", "No Message")))
                if "detail" in response:
                    self.log("Detail: {}".format(response["detail"]))
        except json.decoder.JSONDecodeError as e:
            self.log("JSON Error: {}".format(e))
            response = []
        except:
            self.log(method=method)
        finally:
            self.LOGGING = True
            response = ResponseObject(response)
        return response
        
            
class BrawlStars(SupercellAPI):
    """ class to work with Brawl Stars Api
    
    More in <https://developer.brawlstars.com>
    """
    API_NAME = "Brawl-Stars"
    API_HOST = "api.brawlstars.com"
    
    def get_player(self, tag):
        """ Get player Information
        
        :param tag: Tag of the Player
        :type tag: str
        
        :returns: ResponseObject
        """
        return self.request("players/{}".format(self.valid_tag(tag)))
        
    def get_player_battlelog(self, tag):
        """ Get log of recent battles for a player.
        
        :param tag: Tag of the Player
        :type tag: str
        
        :returns: ResponseObject
        """
        return self.request("players/{}/battlelog".format(self.valid_tag(tag)))
    
    def get_club(self, tag):
        """ Get club Information
        
        :param tag: Tag of the Club
        :type tag: str
        
        :returns: ResponseObject
        """
        return self.request("clubs/{}".format(self.valid_tag(tag)))
    
    def get_club_members(self, tag, before=None, after=None, limit=None):
        """ List club Members
        
        :param tag: Tag of the Club
        :type tag: str
        
        :param before: Return only items that occur before this marker
        :type before: str
        
        :param after: Return only items that occur after this marker
        :type after: str
        
        :param limit: Limit the number of items returned in the response
        :type limit: int
        """
        params = {}
        
        if before is not None:
            params["before"] = before
        if after is not None:
            params["after"] = after
        if limit is not None:
            params["limit"] = limit
        return self.request("clubs/{}/members".format(self.valid_tag(tag)), params)
    
    def get_brawlers(self, before=None, after=None, limit=None):
        """ Get list of available brawlers
        
        :param before: Return only items that occur before this marker
        :type before: str
        
        :param after: Return only items that occur after this marker
        :type after: str
        
        :param limit: Limit the number of items returned in the response
        :type limit: int
        """
        params = {}
        
        if before is not None:
            params["before"] = before
        if after is not None:
            params["after"] = after
        if limit is not None:
            params["limit"] = limit
        return self.request("brawlers", params)
        
    def get_brawler(self, id=16E6):
        """ Get information about a brawler
        
        :param id: Identifier of the brawler
        :type id: str
        """
        return self.request("brawlers/{}".format(round(id)))
    
    def get_rankings(self, country="global", rankings="players", before=None,
                                   after=None, limit=None, brawlerId=None):
        """ Get player, club or brawler rankings for a country or global rankings.
        
        :param country: Two letter country code, or 'global' for global rankings
        :type country: str
        
        :param rankings: Rankings type
        :type rankings: str
        
        :param before: Return only items that occur before this marker
        :type before: str
        
        :param after: Return only items that occur after this marker
        :type after: str
        
        :param limit: Limit the number of items returned in the response
        :type limit: int
        
        :param brawlerId: Identifier of the brawler
        :type brawlerId: str
        """
        params = {}
        
        if before is not None:
            params["before"] = before
        if after is not None:
            params["after"] = after
        if limit is not None:
            params["limit"] = limit
            
        if rankings in ("players", "clubs", "brawlers"):
            if brawlerId is not None and rankings == "brawlers":
                return self.request("rankings/{}/brawlers/{}".format(country, brawlerId), params)
            else:
                return self.request("rankings/{}/{}".format(country, rankings), params)
        else:
            self.log("Notice: undefined Rankings type {}".format(rankings))
            return ResponseObject()
     
class ClashRoyale(SupercellAPI):
    """ class to work with Clash Royale Api
    
    More in <https://developer.clashroyale.com>
    """
    API_NAME = "Clash-Royale"
    API_HOST = "api.clashroyale.com"
    
    def search_clans(self, **params):
        """ Search clans by filters
        
        :param name: Search clans by Name
        :type name: str
        
        :param locationId: Filter by clan location identifier
        :type locationId: int
        
        :param minMembers: Filter by minimum number of Clan members
        :type minMembers: int
        
        :param maxMembers: Filter by maximum number of Clan members
        :type maxMembers: int
        
        :param minScore: Filter by minimum amount of Clan score
        :type minScore: int
        
        :param before: Return only items that occur before this marker
        :type before: str
        
        :param after: Return only items that occur after this marker
        :type after: str
        
        :param limit: Limit the number of items returned in the response
        :type limit: int 
        """
        return self.request("clans", params)
    
    def get_clan(self, tag):
        """ Get clan Information
        
        :param tag: Tag of the clan
        :type tag: str
        """
        return self.request("clans/{}".format(self.valid_tag(tag)))
        
    def get_clan_members(self, tag, before=None, after=None, limit=None):
        """ List clan Members
        
        :param tag: Tag of the Clan
        :type tag: str
        
        :param before: Return only items that occur before this marker
        :type before: str
        
        :param after: Return only items that occur after this marker
        :type after: str
        
        :param limit: Limit the number of items returned in the response
        :type limit: int
        """
        params = {}
        
        if before is not None:
            params["before"] = before
        if after is not None:
            params["after"] = after
        if limit is not None:
            params["limit"] = limit
        return self.request("clans/{}/members".format(self.valid_tag(tag)), params)
        
    def get_clan_warlog(self, tag, before=None, after=None, limit=None):
        """ Retrieve clan's clan war log
        
        :param tag: Tag of the Clan
        :type tag: str
        
        :param before: Return only items that occur before this marker
        :type before: str
        
        :param after: Return only items that occur after this marker
        :type after: str
        
        :param limit: Limit the number of items returned in the response
        :type limit: int
        """
        params = {}
        
        if before is not None:
            params["before"] = before
        if after is not None:
            params["after"] = after
        if limit is not None:
            params["limit"] = limit
        return self.request("clans/{}/warlog".format(self.valid_tag(tag)), params)
    
    def get_clan_war(self, tag):
        """ Retrieve information about clan's current clan war
        
        :param tag: Tag of the Clan
        :type tag:str
        """
        return self.request("clans/{}/currentwar".format(self.valid_tag(tag)))
        
    def get_player(self, tag):
        """ Get player Information
        
        :param tag: Tag of the Player
        :type tag: str
        """
        return self.request("players/{}".format(self.valid_tag(tag)))
        
    def get_player_chests(self, tag):
        """ Get information about player upcoming chests
        
        :param tag: Tag of the Player
        :type tag:str
        """
        return self.request("players/{}/upcomingchests".format(self.valid_tag(tag)))
    
    def get_player_battlelog(self, tag):
        """ Get list of recent battles for a player
        
        :param tag: Tag the of Player
        :type tag: str
        """
        return self.request("players/{}/battlelog".format(self.valid_tag(tag)))
        
    def get_cards(self,  before=None, after=None, limit=None):
        """ Get list of available cards
        
        :param before: Return only items that occur before this marker
        :type before: str
        
        :param after: Return only items that occur after this marker
        :type after: str
        
        :param limit: Limit the number of items returned in the response
        :type limit: int
        """
        params = {}
        
        if before is not None:
            params["before"] = before
        if after is not None:
            params["after"] = after
        if limit is not None:
            params["limit"] = limit
        return self.request("cards", params)
        
    def get_tournaments(self, name=None, before=None, after=None, limit=None):
        """ Search all tournament by name
        
        :param name: Search clans by name
        :type name: str
        
        :param before: Return only items that occur before this marker
        :type before: str
        
        :param after: Return only items that occur after this marker
        :type after: str
        
        :param limit: Limit the number of items returned in the response
        :type limit: int
        """
        params = {}
        
        if name is not None:
            params["name"] = name
        if before is not None:
            params["before"] = before
        if after is not None:
            params["after"] = after
        if limit is not None:
            params["limit"] = limit
        return self.request("tournaments", params)
        
    def get_tournament(self, tag):
        """ Get information about a single tournament by a tournament tag
        
        :param tag: Tag of the tournament to retrieve
        :type tag: str
        """
        return self.request("tournaments/{}".format(tag))
        
    def get_global_tournaments(self):
        """ Get list of global tournaments
        """
        return self.request("globaltournaments")
        
    def get_locations(self, locationId=None, rankings=None, tag=None, before=None, after=None, limit=None):
        """ Get List locations
            Get location information
            Get clan rankings for a specific location
            Get player rankings for a specific location
            Get clan war rankings for a specific location
            Get Global tournament rankings
        
        :param locationId: Identifier of the location to retrieve
        :type locationId: str
        
        :param rankings: Rankings type (players, clans, clanwars)
        :type rankings: str
        
        :param tag: Tag of the tournament
        :type tag: str
        
        :param before: Return only items that occur before this marker
        :type before: str
        
        :param after: Return only items that occur after this marker
        :type after: str
        
        :param limit: Limit the number of items returned in the response
        :type limit: int
        """
        params = {}
        
        if before is not None:
            params["before"] = before
        if after is not None:
            params["after"] = after
        if limit is not None:
            params["limit"] = limit
            
        if locationId is None and rankings is None and tag is None:
            return self.request("locations", params)
        elif locationId is not None and rankings is None:
            return self.request("locations/{}".format(locationId))
        elif locationId is not None and rankings is not None:
            if rankings in ("players", "clanwars", "clans"):
                return self.request("locations/{}/rankings/{}".format(locationId, rankings))
            else:
                self.log("Notice: undefined Rankings type {}".format(rankings))
        elif tag is not None:
            return self.request("locations/global/rankings/tournaments/{}".format(tag))
        else:
            self.log("Notice: could not recognize the type of location -> get_locations()")
        return ResponseObject()
        
class ClashOfClans(SupercellAPI):
    """ class to work with Clash of Clans Api
    
    More in <https://developer.clashofclans.com>
    """
    API_NAME = "Clash-of-Clans"
    API_HOST = "api.clashofclans.com"
    
    def search_clans(self, **params):
        """ Search clans by filtering
       
        :type params: kwargs 
        :param params: 
        
            :param name: search clans by Name
            :type name: str
            
            :param warFrequency: filter by clan war Frequency
            :type warFrequency: str
            
            :param locationId: Filter by clan location Identifier
            :type locationId: int
            
            :param minMembers: Filter by minimum number of clan members
            :type minMembers: int
            
            :param maxMembers: Filter by maximum number of clan members
            :type maxMembers: int
            
            :param minClanPoints: Filter by minimum amount of clan points
            :type minClanPoints: imt
            
            :param minClanLevel: Filter by minimum clan Level
            :type minClanLevel: int
            
            :param before: Return only items that occur before this marker
            :type before: str
        
            :param after: Return only items that occur after this marker
            :type after: str
        
            :param limit: Limit the number of items returned in the response
            :type limit: int 
            
            :param labelIds: Comma separatered list of label IDs to use for filtering results
            :param labelIds: str
        """
        return self.request("clans", params)
        
    def get_clan(self, tag):
        """ Get clan Information by tag
        
        :param tag: Tag of the clan
        :type tag: str
        """
        return self.request("clans/{}".format(self.valid_tag(tag)))
        
    def get_clan_members(self, tag, before=None, after=None, limit=None):
        """ List clan Members
        
        :param tag: Tag of the Clan
        :type tag: str
        
        :param before: Return only items that occur before this marker
        :type before: str
        
        :param after: Return only items that occur after this marker
        :type after: str
        
        :param limit: Limit the number of items returned in the response
        :type limit: int
        """
        params = {}
        
        if before is not None:
            params["before"] = before
        if after is not None:
            params["after"] = after
        if limit is not None:
            params["limit"] = limit
        return self.request("clans/{}/members".format(self.valid_tag(tag)), params)
        
    def get_clan_warlog(self, tag, before=None, after=None, limit=None):
        """ Retrieve clan's clan war log 
        
        :param tag: Tag of the Clan
        :type tag: str
        
        :param before: Return only items that occur before this marker
        :type before: str
        
        :param after: Return only items that occur after this marker
        :type after: str
        
        :param limit: Limit the number of items returned in the response
        :type limit: int
        """
        params = {}
        
        if before is not None:
            params["before"] = before
        if after is not None:
            params["after"] = after
        if limit is not None:
            params["limit"] = limit
        return self.request("clans/{}/warlog".format(self.valid_tag(tag)), params) 
        
    def get_clan_war(self, tag, league=False):
        """ Retrieve information about clan's current clan war
        
        :param tag: Tag of the clan
        :type tag: str
        
        :param league: Retrieve information about clan's current clan war league group 
        :type league: bool
        """
        league = "currentwar/leaguegroup" if league else "currentwar"
        return self.request("clans/{}/{}".format(self.valid_tag(tag), league))
        
    def get_clanwar_leagues(self, tag):
        """ Retrieve information about individual clan war league war
        
        :param tag: Tag of the war
        :type tag: str
        """
        return self.request("clanwarleagues/wars/{warTag}".format(warTag=tag))
        
    def get_player(self, tag):
        """ Get player information
        
        :param tag: Tag of the Player
        :param tag: str
        """
        return self.request("players/{}".format(self.valid_tag(tag)))
        
    def get_leagues(self, leagueId=None, seasonId=None, before=None, after=None, limit=None,
                                                    seasons=False, warleagues=False):
        """ Get list leagues
            Get league information
            Get league seasons
            Get league season rankings
            Get list war leagues
            Get war league information
            
        :param leagueId: identifier of the league
        :type leagueId: str
        
        :param seasonId: identifier of the season
        :type seasonId: str
        
        :param before: Return only items that occur before this marker
        :type before: str
        
        :param after: Return only items that occur after this marker
        :type after: str
        
        :param limit: Limit the number of items returned in the response
        :type limit: int
        
        :param seasons: Get league seasons
        :type seasons: bool
        
        :param warleagues: Get war league information
        :type warleagues: bool
        """
        params = {}
        
        if before is not None:
            params["before"] = before
        if after is not None:
            params["after"] = after
        if limit is not None:
            params["limit"] = limit
            
        if leagueId is None and not seasons and not warleagues:
            return self.request("leagues", params)
        if leagueId is not None and not seasons and not warleagues:
            return self.request("leagues/{}".format(leagueId))
        if leagueId is not None and seasons:
            season = "seasons" if seasonId is None else "seasons/{}".format(seasonId)
            return self.request("leagues/{}/{}".format(leagueId, season), params)
        if warleagues:
            if leagueId is None:
                return self.request("warleagues", params)
            else:
                return self.request("warleagues/{}".format(leagueId))
        return ResponseObject()
        
    def get_locations(self, locationId=None, rankings=None,
                            before=None, after=None, limit=None):
        """ Get list locations
            Get location information
            Get clan Rankings for a specific location
            Get player Rankings for a specific location
            Get clan versus Rankings for a specific location
            Get player versus Rankings for a specific location
        
        :param locationId: identifier of the location to retrieve
        :type locationId: str
        
        :param rankings: Rankings type
        :type rankings: str
        
        :param before: Return only items that occur before this marker
        :type before: str
        
        :param after: Return only items that occur after this marker
        :type after: str
        
        :param limit: Limit the number of items returned in the response
        :type limit: int
        """
        params = {}
        
        if before is not None:
            params["before"] = before
        if after is not None:
            params["after"] = after
        if limit is not None:
            params["limit"] = limit
            
        if locationId is None:
            return self.request("locations", params)
        elif rankings is None:
            return self.request("locations/{}".format(locationId))
        elif rankings in ("clans", "clans-versus", "players", "players-versus"):
            return self.request("locations/{}/rankings/{}".format(leagueId, rankings), params)
        else:
            self.log("Notice: undefined Rankings type {type}".format(type=rankings))
        return ResponseObject()
        
    def get_labels(self, clans=False, before=None, after=None, limit=None):
        """ Get list player labels 
        
        :param clans: Get list clan labels
        :type clans: bool
        
        :param before: Return only items that occur before this marker
        :type before: str
        
        :param after: Return only items that occur after this marker
        :type after: str
        
        :param limit: Limit the number of items returned in the response
        :type limit: int
        """
        params = {}
        
        if before is not None:
            params["before"] = before
        if after is not None:
            params["after"] = after
        if limit is not None:
            params["limit"] = limit
            
        label = "clans" if clans else "players"
        return self.request("labels/{}".format(label), params)