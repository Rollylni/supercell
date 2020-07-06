# Brawl Stars API

**work with BrawL Stars Api**
  * API Url: https://api.brawlstars.com
  * [Homepage](https://developer.brawlstars.com)

# class BrawlStars

## usage
```python
from supercel import BrawlStars

token = "my_api_token"
api = BrawlStars(token)
print(api.get_players(["tag1", "tag2"]).response)
``` 

## Methods

### get_player(tag)

**Gets player information by Tag**

| Parameter          | Data Type | Description       |
|--------------------|-----------|-------------------|
| tag __(required)__ |  String   | Tag of the player |



**:returns:** after a successful request, returns a [ResponseObject](./ResponseObject.md) with the [schema](https://github.com/Rollylni/supercell/blob/master/schemas/bs/player-schema.json),

if the request failed, then it returns an [error scheme](https://github.com/Rollylni/supercell/blob/master/schemas/error_response-schema.json),

*all errors that may happen when requesting an API you can see* [here](./error-responses.md)

**:usage:** 
```python
api = BrawlStars()
player = api.get_player("#PLAYER_TAG")
print(player.response)
```


### get_club(tag)

**Gets club information by Tag**

| Parameter             | Data Type | Description       |
|-----------------------|-----------|-------------------|
| tag __(required)__    |  String   | Tag of the club   |


**:returns:** after a successful request, returns a [ResponseObject](./ResponseObject.md) with the [schema](https://github.com/Rollylni/supercell/blob/master/schemas/bs/club-schema.json),

if the request failed, then it returns an [error scheme](https://github.com/Rollylni/supercell/blob/master/schemas/error_response-schema.json)

*all errors that may happen when requesting an API you can see* [here](./error-responses.md)

### get_player_battlelog(tag)

**Gets log of recent battles for a player.**

| Parameter             | Data Type | Description       |
|-----------------------|-----------|-------------------|
| tag __(required)__    |  String   | Tag of the player |



**:returns:** after a successful request, returns a [ResponseObject](./ResponseObject.md) with the [schema](https://github.com/Rollylni/supercell/blob/master/schemas/bs/battlelog-schema.json),

if the request failed, then it returns an [error scheme](https://github.com/Rollylni/supercell/blob/master/schemas/error_response-schema.json) 

*all errors that may happen when requesting an API you can see* [here](./error-responses.md)

### get_club_members(tag, before=None, after=None, limit=None)

**Gets list club members.**

| Parameter             | Data Type | Description                                        |
|-----------------------|-----------|----------------------------------------------------|
| tag __(required)__    |  String   | Tag of the club                                    |
| before                |  String   | Return only items that occur before this marker    |
| after                 |  String   | Return only items that occur after this maker      |
| limit                 |  Integer  | Limit the number of items returned in the response |



**:returns:** after a successful request, returns a [ResponseObject](./ResponseObject.md) with the [schema](https://github.com/Rollylni/supercell/blob/master/schemas/bs/club_members-schema.json),

if the request failed, then it returns an [error scheme](https://github.com/Rollylni/supercell/blob/master/schemas/error_response-schema.json) 

*all errors that may happen when requesting an API you can see* [here](./error-responses.md) 

### get_brawlers(before=None, after=None, limit=None)

**Gets list of available brawlers.**

| Parameter             | Data Type | Description                                        |
|-----------------------|-----------|----------------------------------------------------|
| before                |  String   | Return only items that occur before this marker    |
| after                 |  String   | Return only items that occur after this maker      |
| limit                 |  Integer  | Limit the number of items returned in the response |



**:returns:** after a successful request, returns a [ResponseObject](./ResponseObject.md) with the [schema](https://github.com/Rollylni/supercell/blob/master/schemas/bs/brawlers-schema.json),

if the request failed, then it returns an [error scheme](https://github.com/Rollylni/supercell/blob/master/schemas/error_response-schema.json) 

*all errors that may happen when requesting an API you can see* [here](./error-responses.md) 

### get_brawler(id=16E6)

**Gets information about a brawler**

| Parameter | Data Type | Description       |
|-----------|-----------|-------------------|
| id        |  String   | Id of the brawler |


**:returns:** after a successful request, returns a [ResponseObject](./ResponseObject.md) with the [schema](https://github.com/Rollylni/supercell/blob/master/schemas/bs/brawler-schema.json),

if the request failed, then it returns an [error scheme](https://github.com/Rollylni/supercell/blob/master/schemas/error_response-schema.json)

*all errors that may happen when requesting an API you can see* [here](./error-responses.md)

### get_rankings(country="global", rankings="players", before=None, after=None, limit=None, brawlerId=None)

**Gets player, club or brawler rankings for a country or global rankings.**

| Parameter             | Data Type | Description                                              |
|-----------------------|-----------|----------------------------------------------------------|
| country               |  String   | Two letter country code, or 'global' for global rankings |
| rankings              |  String   | Rankings type                                            |
| before                |  String   | Return only items that occur before this marker          |
| after                 |  String   | Return only items that occur after this maker            |
| limit                 |  Integer  | Limit the number of items returned in the response       |
| brawlerId             |  String   | Identifier of the brawler                                |

**:returns:** after a successful request, returns a [ResponseObject](./ResponseObject.md) with one of these schemas [players_rankings](https://github.com/Rollylni/supercell/blob/master/schemas/bs/rankings_players-schema.json),
[clubs_rankings](https://github.com/Rollylni/supercell/blob/master/schemas/bs/rankings_clubs-schema.json),
[brawlers_rankings](https://github.com/Rollylni/supercell/blob/master/schemas/bs/rankings_brawlers-schema.json),

if the request failed, then it returns an [error scheme](https://github.com/Rollylni/supercell/blob/master/schemas/error_response-schema.json) 

*all errors that may happen when requesting an API you can see* [here](./error-responses.md) 