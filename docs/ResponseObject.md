## class ResponseObject

all methods of the [BrawlStars](./brawlstars.md), [ClashRoyale](./clashroyale.md), and [ClashOfClans](./clashofclans.md) classes return a ResponseObject

### usage
```python
import supercel

api = supercel.BrawlStars("TOKEN") 
response = api.get_player("#PLGQ2RJV2")

name = response.get("name")
trophies = response.get("trophies")
club = response.get("club.tag")
print(name, trophies, club)
```

### ResponseObject.get(key)

:param key: str
:returns: mixed