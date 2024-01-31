APP=parser
PORT=5000
VERSION=latest
sudo docker run -it --publish $PORT:$PORT --volume "$PWD/app":/app $APP:$VERSION
