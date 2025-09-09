import argparse
import app
parser = argparse.ArgumentParser(description="easy 320px maximum size thumbnails.")

parser.add_argument("--dir", required=True, help="your directory with jpg files")
args = parser.parse_args()
app.create_thumbnails(args.dir)