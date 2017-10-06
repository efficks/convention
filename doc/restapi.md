# Resources

* [Organisme](#api-1-organism)
* Convention
* Version
* Article
* Clause

## /api/1/organism/
### GET all
`/api/1/organism/`
**Response**
```json
[
  {
    "id":0,
    "name":"nom du syndicat"
  },
  {
    "id":1,
    "name":"nom d'un employeur"
  }
]
```
### GET
`/api/1/organism/{id}`
**Parameters**
* **id**: Id interne de l'organisme
**Response**
```json
{
  "id":0,
  "name":"nom du syndicat"
}
```
