APP=parser
PORT=5000
VERSION=latest
DOCKERFILE=./docker/Dockerfile
PRODUCTION_BUILD=''${1:+True} && PRODUCTION_BUILD=${PRODUCTION_BUILD:-False}''
echo '#################################'
echo "PRODUCTION_BUILD: $PRODUCTION_BUILD"
echo '#################################'
if [[ $PRODUCTION_BUILD = True ]]; then
  sudo docker build --build-arg PRODUCTION_BUILD=$PRODUCTION_BUILD \
  --build-arg PORT=$PORT -t $APP:$VERSION -f $DOCKERFILE .
else
  sudo docker build --build-arg PORT=$PORT -t $APP:$VERSION -f $DOCKERFILE .
fi
