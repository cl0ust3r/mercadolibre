POST
curl -H "Content-Type: application/json" -X POST -d '{"id":"8033322","user":"cherrera"}' http://0.0.0.0/json
GET
curl http://0.0.0.0/json/8033322
UPDATE
curl -H "Content-Type: application/json" -X PUT -d '{"id":"8033322","user":"jherrera"}' http://0.0.0.0/json
DELETE
curl -X DELETE http://0.0.0.0/json/8033322
