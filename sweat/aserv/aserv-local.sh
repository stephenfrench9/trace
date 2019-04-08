docker run --name app-aserv -d aserv
docker network create my-net
docker network connect my-net app-aserv
