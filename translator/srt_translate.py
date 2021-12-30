#!/usr/bin/python

import sys
import argparse
import os
from deep_translator import GoogleTranslator

def translate(text, src="auto", dest="en"):
    """Translate `text` from `src` language to `dest`"""
    return GoogleTranslator(source=src, target=dest).translate(text)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Python script to translate text using Google Translate API (googletrans wrapper)")
    parser.add_argument("target", help="Text/Document to translate")
    parser.add_argument("-s", "--source", help="Source language, default is Google Translate's auto detection", default="auto")
    parser.add_argument("-d", "--destination", help="Destination language, default is English", default="it")
    
    args = parser.parse_args()
    target = args.target
    src = args.source
    dest = args.destination
    
    if os.path.isfile(target):
        # translate a document instead
        # get basename of file
        basename = os.path.basename(target)
        # get the path dir
        dirname = os.path.dirname(target)
        try:
            filename, ext = basename.split(".")
        except:
            # no extension
            filename = basename
            ext = ""

        content_string = ''
        translated_text = ''
        translate_call_count = 0
        
        with open(target) as f:
            #open(os.path.join(dirname, f"{filename}_{dest}{f'.{ext}' if ext else ''}"), "w")   
        
            for line in f:
                if(len(content_string) < 4900):
                    content_string += line
                else:
                    translate_call_count += 1
                    print('translate call count:', translate_call_count)
                    translated_text = translate(content_string, src, dest)
                    print(translated_text)
                    open(os.path.join(dirname, f"{filename}_{dest}{f'.{ext}' if ext else ''}"), "a").write(translated_text)
                    content_string = ''
                    
            if(len(content_string) > 0):
                translated_text = translate(content_string, src, dest)
                print(translated_text)
                open(os.path.join(dirname, f"{filename}_{dest}{f'.{ext}' if ext else ''}"), "a").write(translated_text)

        # write to new document file
        #open(os.path.join(dirname, f"{filename}_{dest}{f'.{ext}' if ext else ''}"), "a").write(translated_text)
    else:
        # not a file, just text, print the translated text to standard output
        print(translate(target, src, dest))
        