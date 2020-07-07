## Error Responses

[failed request schema](https://github.com/Rollylni/supercell/blob/master/schemas/error_response-schema.json)

### Error Model
```js
ClientError {
reason (string, optional),
message (string, optional),
type (string, optional),
detail (object, optional)
}
```

### Response messages  

| HTTP Status Code | Reason |
|------------------|--------|
| 200              | Successful response |
| 400              | Client provided incorrect parameters for the request |
| 403              | Access denied, either because of missing/incorrect credentials or used API token does not grant access to  the requested resource |
| 404              | Resource was not found |
| 429              | Request was throttled, because amount of requests was above the threshold defined for the used API token |
| 500              | Unknown error happened when handling the request |
| 503              | Service is temprorarily unavailable because of maintenance |
