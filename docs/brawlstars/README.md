# Brawl Stars API

**work with BrawL Stars Api**
  * API Url: https://api.brawlstars.com
  * [Homepage](https://developer.brawlstars.com)

## class BrawlStars

| Parameter | Description  |  Type  |
|-----------|--------------|--------|
|  token    | access token | String |

## usage
```python
from supercel import BrawlStars

token = "my_api_token"
api = BrawlStars(token)
print(api.get_player("player tag").response)
``` 


