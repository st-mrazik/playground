## Requirements to run this script
[python](https://www.python.org/)

[virtualenv](https://virtualenv.pypa.io/en/latest/)

## How to run
```bash
# run this just for the first time to initialize virtualenv
virtualenv translator/.env --python python3
# run from here after first initialization
source translator/.env/bin/activate
pip install -r translator/requirements.txt
python translator/srt_translate.py translator/data/example.txt -d sk
```