## Requirements to run this script
[python](https://www.python.org/)

[virtualenv](https://virtualenv.pypa.io/en/latest/)

## How to run
```bash
# run this just for the first time to initialize virtualenv
virtualenv translator/.env --python python3
# run from here after first initialization
source translator/.env/bin/activate
# this will install libraries inside virtualenv (run after modifying requirements.txt)
pip install -r translator/requirements.txt
python translator/srt_translate.py translator/data/example.txt -d sk
```