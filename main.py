import argparse
import requests
def downloadsavefile(url, nameoffile):
    with requests.get(url, stream=True) as v:
        v.raise_for_status()
        with open(nameoffile, "wb") as f:
            for chunk in v.iter_content(chunk_size=8192):
                f.write(chunk)
    return nameoffile
if __name__=="__main__":
    parser= argparse.ArgumentParser()
    parser.add_argument("url",help="paste img url here")    
    parser.add_argument("filename",help="name img file that u want to save")
    arg= parser.parse_args()
    url=arg.url
    nameoffile=arg.filename
    downloadsavefile(url, nameoffile)

