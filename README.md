# Mercadolibre Reto3 

IP_PUBLIC = ""

POST
curl -H "Content-Type: application/json" -X POST -d '{"id":"8033322","user":"cherrera"}' http://$IP_PUBLIC/json


GET
curl http://$IP_PUBLIC/json/8033322


UPDATE
curl -H "Content-Type: application/json" -X PUT -d '{"id":"8033322","user":"jherrera"}' http://$IP_PUBLIC/json


DELETE
curl -X DELETE http://$IP_PUBLIC/json/8033322
