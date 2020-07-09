# Clash of Clans API

**work with Clash of Clans Api**
  * API Url: https://api.clashofclans.com
  * [Homepage](https://developer.clashofclans.com)

# class BrawlStars

## usage
```python
from supercel import ClashOfClans

token = "my_api_token"
api = ClashOfClans(token)
print(api.get_players(["tag1", "tag2"]).response)
``` 

## Methods

### get_player(tag)

**Gets player information by Tag**

| Parameter          | Data Type | Description       |
|--------------------|-----------|-------------------|
| tag __(required)__ |  String   | Tag of the player |



**:returns:** after a successful request, returns a [ResponseObject](./ResponseObject.md) with the [schema](https://github.com/Rollylni/supercell/blob/master/schemas/coc/player-schema.json),

if the request failed, then it returns an [error scheme](https://github.com/Rollylni/supercell/blob/master/schemas/error_response-schema.json),

*all errors that may happen when requesting an API you can see* [here](./error-responses.md)

### search_clans(**params)

**Search clans by filtering**

| Parameter          | Data Type | Description       |
|--------------------|-----------|-------------------|
| params             |  kwargs   | method parameters |



**:returns:** after a successful request, returns a [ResponseObject](./ResponseObject.md) with the [schema](https://github.com/Rollylni/supercell/blob/master/schemas/coc/clans-schema.json),

if the request failed, then it returns an [error scheme](https://github.com/Rollylni/supercell/blob/master/schemas/error_response-schema.json),

*all errors that may happen when requesting an API you can see* [here](./error-responses.md)

### get_clan(tag)

**Gets clan information by Tag**

| Parameter          | Data Type | Description       |
|--------------------|-----------|-------------------|
| tag __(required)__ |  String   | Tag of the clan   |



**:returns:** after a successful request, returns a [ResponseObject](./ResponseObject.md) with the [schema](https://github.com/Rollylni/supercell/blob/master/schemas/coc/clan-schema.json),

if the request failed, then it returns an [error scheme](https://github.com/Rollylni/supercell/blob/master/schemas/error_response-schema.json),

*all errors that may happen when requesting an API you can see* [here](./error-responses.md)

### get_clan_members(tag, before=None, after=None, limit=None)

**Gets list clan members.**

| Parameter             | Data Type | Description                                        |
|-----------------------|-----------|----------------------------------------------------|
| tag __(required)__    |  String   | Tag of the clan                                    |
| before                |  String   | Return only items that occur before this marker    |
| after                 |  String   | Return only items that occur after this maker      |
| limit                 |  Integer  | Limit the number of items returned in the response |



**:returns:** after a successful request, returns a [ResponseObject](./ResponseObject.md) with the [schema](https://github.com/Rollylni/supercell/blob/master/schemas/coc/clan_members-schema.json),

if the request failed, then it returns an [error scheme](https://github.com/Rollylni/supercell/blob/master/schemas/error_response-schema.json) 

*all errors that may happen when requesting an API you can see* [here](./error-responses.md) 

### get_clan_warlog(tag, before=None, after=None, limit=None)

**Retrieve clan's clan war log**

| Parameter             | Data Type | Description                                        |
|-----------------------|-----------|----------------------------------------------------|
| tag __(required)__    |  String   | Tag of the clan                                    |
| before                |  String   | Return only items that occur before this marker    |
| after                 |  String   | Return only items that occur after this maker      |
| limit                 |  Integer  | Limit the number of items returned in the response |



**:returns:** after a successful request, returns a [ResponseObject](./ResponseObject.md) with the [schema](https://github.com/Rollylni/supercell/blob/master/schemas/coc/clan_warlog-schema.json),

if the request failed, then it returns an [error scheme](https://github.com/Rollylni/supercell/blob/master/schemas/error_response-schema.json) 

*all errors that may happen when requesting an API you can see* [here](./error-responses.md) 

### get_clan_war(tag, league=False)

**Retrieve information about clan's current clan war**

| Parameter          | Data Type | Description       |
|--------------------|-----------|-------------------|
| tag __(required)__ |  String   | Tag of the clan   |
| league             |  Bool     | Retrieve information about clan's current clan war league group |


**:returns:** after a successful request, returns a [ResponseObject](./ResponseObject.md) with one of these schemas [war](https://github.com/Rollylni/supercell/blob/master/schemas/coc/currentwar-schema.json),
[war_league](https://github.com/Rollylni/supercell/blob/master/schemas/coc/currentwar_leaguegroup-schema.json),

if the request failed, then it returns an [error scheme](https://github.com/Rollylni/supercell/blob/master/schemas/error_response-schema.json),

*all errors that may happen when requesting an API you can see* [here](./error-responses.md)

### get_clanwar_leagues(tag)

**Retrieve information about individual clan war league war**

| Parameter          | Data Type | Description       |
|--------------------|-----------|-------------------|
| tag __(required)__ |  String   | Tag of the war    |



**:returns:** after a successful request, returns a [ResponseObject](./ResponseObject.md) with the [schema](https://github.com/Rollylni/supercell/blob/master/schemas/coc/clanwar_leagues-schema.json),

if the request failed, then it returns an [error scheme](https://github.com/Rollylni/supercell/blob/master/schemas/error_response-schema.json),

*all errors that may happen when requesting an API you can see* [here](./error-responses.md)

### get_labels(clans=False, before=None, after=None, limit=None)

**Gets list players labels**

| Parameter             | Data Type | Description                                        |
|-----------------------|-----------|----------------------------------------------------|
| clans                 |  Bool     | Get list clans labels                              |
| before                |  String   | Return only items that occur before this marker    |
| after                 |  String   | Return only items that occur after this maker      |
| limit                 |  Integer  | Limit the number of items returned in the response |



**:returns:** after a successful request, returns a [ResponseObject](./ResponseObject.md) with one of these schemas 
[clans labels](https://github.com/Rollylni/supercell/blob/master/schemas/coc/labels_clans-schema.json),
[players labels](https://github.com/Rollylni/supercell/blob/master/schemas/coc/labels_players-schema.json),


if the request failed, then it returns an [error scheme](https://github.com/Rollylni/supercell/blob/master/schemas/error_response-schema.json) 

*all errors that may happen when requesting an API you can see* [here](./error-responses.md) 

### get_locations(locationId=None, rankings=None, tag=None, before=None, after=None, limit=None)

**Gets list locations**

| Parameter             | Data Type | Description                                              |
|-----------------------|-----------|----------------------------------------------------------|
| locationId            |  String   | Identifier of the location to retrieve                   |
| rankings              |  String   | Rankings type                                            |
| before                |  String   | Return only items that occur before this marker          |
| after                 |  String   | Return only items that occur after this maker            |
| limit                 |  Integer  | Limit the number of items returned in the response       |

**:returns:** after a successful request, returns a [ResponseObject](./ResponseObject.md) with one of these schemas [players_rankings](https://github.com/Rollylni/supercell/blob/master/schemas/coc/rankings_players-schema.json),
[clans_rankings](https://github.com/Rollylni/supercell/blob/master/schemas/coc/rankings_clans-schema.json),
[players_versus](https://github.com/Rollylni/supercell/blob/master/schemas/coc/players_versus-schema.json),
[clans_versus](https://github.com/Rollylni/supercell/blob/master/schemas/coc/clans_versus-schema.json),
[location](https://github.com/Rollylni/supercell/blob/master/schemas/coc/location-schema.json),
[locations](https://github.com/Rollylni/supercell/blob/master/schemas/coc/locations-schema.json),

if the request failed, then it returns an [error scheme](https://github.com/Rollylni/supercell/blob/master/schemas/error_response-schema.json) 

*all errors that may happen when requesting an API you can see* [here](./error-responses.md) 

### get_leagues(leagueId=None, seasonId=None, before=None, after=None, limit=None, seasons=False, warleagues=False)

**Gets list leagues**

| Parameter             | Data Type | Description                                              |
|-----------------------|-----------|----------------------------------------------------------|
| leagueId              |  String   | Identifier of the league to retrieve                     |
| seasonId              |  String   | Identifier of the season to retrieve                     |
| tag                   |  String   | Tag of the tournament                                    |
| rankings              |  String   | Rankings type                                            |
| before                |  String   | Return only items that occur before this marker          |
| after                 |  String   | Return only items that occur after this maker            |
| limit                 |  Integer  | Limit the number of items returned in the response       |
| seasons               |  Bool     | Get league seasons                                       |
| warleagues            |  Bool     | Get war league information                               |

**:returns:** after a successful request, returns a [ResponseObject](./ResponseObject.md) with one of these schemas [league](https://github.com/Rollylni/supercell/blob/master/schemas/coc/league-schema.json),
[leagues](https://github.com/Rollylni/supercell/blob/master/schemas/coc/leagues-schema.json),
[league seasons](https://github.com/Rollylni/supercell/blob/master/schemas/coc/league_seasons-schema.json),
[league season](https://github.com/Rollylni/supercell/blob/master/schemas/coc/league_season-schema.json),
[war league](https://github.com/Rollylni/supercell/blob/master/schemas/coc/warleague-schema.json),
[war leagues](https://github.com/Rollylni/supercell/blob/master/schemas/coc/warleagues-schema.json),

if the request failed, then it returns an [error scheme](https://github.com/Rollylni/supercell/blob/master/schemas/error_response-schema.json) 

*all errors that may happen when requesting an API you can see* [here](./error-responses.md) 
