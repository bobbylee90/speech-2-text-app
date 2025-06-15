pushd ..

sudo apt update -y && sudo apt install ffmpeg -y

pip install -r ./applications/speech-2-text/requirements.txt

popd