VERSION=$1
REPO=$2

IMAGE=skirisclassifier_runtime


#apk add --update openssl


#wget https://github.com/openshift/source-to-image/releases/download/v1.1.9a/source-to-image-v1.1.9a-40ad911d-linux-amd64.tar.gz
#tar -zxf source-to-image-v1.1.9a-40ad911d-linux-amd64.tar.gz

until docker ps; 
do sleep 3; 
done; 

docker run -v  ${PWD}:/my_model seldonio/core-python-wrapper:0.7 /my_model SkIris ${VERSION} ${REPO} --image-name=${IMAGE} --base-image=python:3
cd ./build
./build_image.sh

#./s2i build . seldonio/seldon-core-s2i-python3 ${REPO}/${IMAGE}:${VERSION}


docker images 
echo "Pushing image to ${REPO}/${IMAGE}:${VERSION}"
echo $DOCKER_PASSWORD | docker login --username=$DOCKER_USERNAME --password-stdin 
./push_image.sh

docker push ${REPO}/${IMAGE}:${VERSION}

