pushd ..

docker build --no-cache --progress=plain -f ./docker/speech-2-text/Dockerfile -t bobbylee90/speech2text-app:0.1.0 .

popd