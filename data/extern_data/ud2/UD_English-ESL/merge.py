import os
import urllib

UD_RELEASE = "2.3"

def check_fce():
    code = 0
    try:
        code = os.stat("fce-released-dataset/license").st_size
    except OSError:
        print('''Error:  FCE folder 'fce-released-dataset' not in the current directory.
        Please download the dataset from https://www.ilexir.co.uk/datasets/index.html
        and unzip the file in the current directory.''')
    return code

def obtain_data(code):
    opener = urllib.URLopener()
    try:
        opener.retrieve("http://esltreebank.org/data-"+UD_RELEASE+"-"+str(code)+"/data.zip", \
                        "data.zip")
        print("Done, annotations with data are in data.zip")
    except IOError:
        print("Error: Failed obtaining annotations with data from the specified url")
        
def main():
    code = check_fce()
    if code:
        obtain_data(code)
    
if __name__ == "__main__":
    main()

