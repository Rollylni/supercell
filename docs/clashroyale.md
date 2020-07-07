# Clash Royale API

**work with ClasH Royale Api**
  * API Url: https://api.clashroyale.com
  * [Homepage](https://developer.clashroyale.com)

# class ClashRoyale

## usage
```python
from supercel import ClashRoyale

token = "my_api_token"
api = ClashRoyale(token)
print(api.get_players(["tag1", "tag2"]).response)
``` 

## Methods

### get_player(tag)

**Gets player information by Tag**

| Parameter          | Data Type | Description       |
|--------------------|-----------|-------------------|
| tag __(required)__ |  String   | Tag of the player |



**:returns:** after a successful request, returns a [ResponseObject](./ResponseObject.md) with the [schema](https://github.com/Rollylni/supercell/blob/master/schemas/cr/player-schema.json),

if the request failed, then it returns an [error scheme](https://github.com/Rollylni/supercell/blob/master/schemas/error_response-schema.json),

*all errors that may happen when requesting an API you can see* [here](./error-responses.md)

**:usage:** 
```python
api = ClashRoyale()
player = api.get_player("#PLAYER_TAG")
print(player.response)
```

### get_clan(tag)

**Gets clan information by Tag**

| Parameter          | Data Type | Description       |
|--------------------|-----------|-------------------|
| tag __(required)__ |  String   | Tag of the clan   |



**:returns:** after a successful request, returns a [ResponseObject](./ResponseObject.md) with the [schema](https://github.com/Rollylni/supercell/blob/master/schemas/cr/clan-schema.json),

if the request failed, then it returns an [error scheme](https://github.com/Rollylni/supercell/blob/master/schemas/error_response-schema.json),

*all errors that may happen when requesting an API you can see* [here](./error-responses.md)

### search_clans(**params)

**Search clans by filtering**

| Parameter          | Data Type | Description       |
|--------------------|-----------|-------------------|
| params             |  kwargs   | method parameters |



**:returns:** after a successful request, returns a [ResponseObject](./ResponseObject.md) with the [schema](https://github.com/Rollylni/supercell/blob/master/schemas/cr/clans-schema.json),

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



**:returns:** after a successful request, returns a [ResponseObject](./ResponseObject.md) with the [schema](https://github.com/Rollylni/supercell/blob/master/schemas/cr/clan_members-schema.json),

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



**:returns:** after a successful request, returns a [ResponseObject](./ResponseObject.md) with the [schema](https://github.com/Rollylni/supercell/blob/master/schemas/cr/clan_warlog-schema.json),

if the request failed, then it returns an [error scheme](https://github.com/Rollylni/supercell/blob/master/schemas/error_response-schema.json) 

*all errors that may happen when requesting an API you can see* [here](./error-responses.md) 

### get_cards(before=None, after=None, limit=None)

**Gets list of available cards.**

| Parameter             | Data Type | Description                                        |
|-----------------------|-----------|----------------------------------------------------|
| before                |  String   | Return only items that occur before this marker    |
| after                 |  String   | Return only items that occur after this maker      |
| limit                 |  Integer  | Limit the number of items returned in the response |



**:returns:** after a successful request, returns a [ResponseObject](./ResponseObject.md) with the [schema](https://github.com/Rollylni/supercell/blob/master/schemas/cr/cards-schema.json),

if the request failed, then it returns an [error scheme](https://github.com/Rollylni/supercell/blob/master/schemas/error_response-schema.json) 

*all errors that may happen when requesting an API you can see* [here](./error-responses.md) 

### get_tournaments(name, before=None, after=None, limit=None)

**Search all tournament by name**

| Parameter             | Data Type | Description                                        |
|-----------------------|-----------|----------------------------------------------------|
| name                  |  String   | Search clans by nam                                |
| before                |  String   | Return only items that occur before this marker    |
| after                 |  String   | Return only items that occur after this maker      |
| limit                 |  Integer  | Limit the number of items returned in the response |



**:returns:** after a successful request, returns a [ResponseObject](./ResponseObject.md) with the [schema](https://github.com/Rollylni/supercell/blob/master/schemas/cr/tournaments-schema.json),

if the request failed, then it returns an [error scheme](https://github.com/Rollylni/supercell/blob/master/schemas/error_response-schema.json) 

*all errors that may happen when requesting an API you can see* [here](./error-responses.md) 

### get_tournament(tag)

**Get information about a single tournament by a tournament tag**

| Parameter          | Data Type | Description       |
|--------------------|-----------|-------------------|
| tag __(required)__ |  String   | Tag of the tournament |



**:returns:** after a successful request, returns a [ResponseObject](./ResponseObject.md) with the [schema](https://github.com/Rollylni/supercell/blob/master/schemas/cr/tournament-schema.json),

if the request failed, then it returns an [error scheme](https://github.com/Rollylni/supercell/blob/master/schemas/error_response-schema.json),

*all errors that may happen when requesting an API you can see* [here](./error-responses.md)

### get_global_tournaments()

**Get list of global tournaments**

**:returns:** after a successful request, returns a [ResponseObject](./ResponseObject.md) with the [schema](https://github.com/Rollylni/supercell/blob/master/schemas/cr/tournaments_global-schema.json),

if the request failed, then it returns an [error scheme](https://github.com/Rollylni/supercell/blob/master/schemas/error_response-schema.json),

*all errors that may happen when requesting an API you can see* [here](./error-responses.md)

### get_player_chests(tag)

**Gets information about player upcoming chests**

| Parameter          | Data Type | Description       |
|--------------------|-----------|-------------------|
| tag __(required)__ |  String   | Tag of the player |



**:returns:** after a successful request, returns a [ResponseObject](./ResponseObject.md) with the [schema](https://github.com/Rollylni/supercell/blob/master/schemas/cr/player_chests-schema.json),

if the request failed, then it returns an [error scheme](https://github.com/Rollylni/supercell/blob/master/schemas/error_response-schema.json),

*all errors that may happen when requesting an API you can see* [here](./error-responses.md)

### get_player_battlelog(tag)

**Get list of recent battles for a player**

| Parameter          | Data Type | Description       |
|--------------------|-----------|-------------------|
| tag __(required)__ |  String   | Tag of the player |



**:returns:** after a successful request, returns a [ResponseObject](./ResponseObject.md) with the [schema](https://github.com/Rollylni/supercell/blob/master/schemas/cr/player_battlelog-schema.json),

if the request failed, then it returns an [error scheme](https://github.com/Rollylni/supercell/blob/master/schemas/error_response-schema.json),

*all errors that may happen when requesting an API you can see* [here](./error-responses.md)

### get_clan_war(tag)

**Retrieve information about clan's current clan war**

| Parameter          | Data Type | Description       |
|--------------------|-----------|-------------------|
| tag __(required)__ |  String   | Tag of the clan   |



**:returns:** after a successful request, returns a [ResponseObject](./ResponseObject.md) with the [schema](https://github.com/Rollylni/supercell/blob/master/schemas/cr/currentwar-schema.json),

if the request failed, then it returns an [error scheme](https://github.com/Rollylni/supercell/blob/master/schemas/error_response-schema.json),

*all errors that may happen when requesting an API you can see* [here](./error-responses.md)

### get_locations(locationId=None, rankings=None, tag=None, before=None, after=None, limit=None, brawlerId=None)

**Gets list locations**

| Parameter             | Data Type | Description                                              |
|-----------------------|-----------|----------------------------------------------------------|
| locationId            |  String   | Identifier of the location to retrieve                   |
| tag                   |  String   | Tag of the tournament                                    |
| rankings              |  String   | Rankings type                                            |
| before                |  String   | Return only items that occur before this marker          |
| after                 |  String   | Return only items that occur after this maker            |
| limit                 |  Integer  | Limit the number of items returned in the response       |                       |

**:returns:** after a successful request, returns a [ResponseObject](./ResponseObject.md) with one of these schemas [players_rankings](https://github.com/Rollylni/supercell/blob/master/schemas/cr/rankings_players-schema.json),
[clans_rankings](https://github.com/Rollylni/supercell/blob/master/schemas/cr/rankings_clans-schema.json),
[clanwars_rankings](https://github.com/Rollylni/supercell/blob/master/schemas/cr/rankings_clanwars-schema.json),
[tournament_rankings](https://github.com/Rollylni/supercell/blob/master/schemas/cr/rankings_tournaments-schema.json),
[location](https://github.com/Rollylni/supercell/blob/master/schemas/cr/location-schema.json),
[locations](https://github.com/Rollylni/supercell/blob/master/schemas/cr/locations-schema.json),

if the request failed, then it returns an [error scheme](https://github.com/Rollylni/supercell/blob/master/schemas/error_response-schema.json) 

*all errors that may happen when requesting an API you can see* [here](./error-responses.md) 
