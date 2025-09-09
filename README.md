# generator thumbnailów o wielkości max 320px po podaniu ścieżki do folderu

# jak uruchomić:

--bash
git clone https://github.com/ItsMeZoq/320px_thumbnail.git

cd 320px_thumbnail

python -m venv venv

venv\Scripts\activate

pip install -r "requirments.txt"

python cli.py --dir "type your directory path here"
