#!/usr/bin/python

import binascii,sys

if len(sys.argv) != 4:
  print "Usage : python audio_injector.py [template_image] [template_audio_file] [final_image_file]"
  sys.exit(0)

audio_file_path = sys.argv[2] # audio file that you want to inject to image.
image_template = sys.argv[1] # image file that you want to inject the audio to it.
injected_image = sys.argv[3] # final image file that contains the injected audio file.

def read_audio_file():
 audio_file = open(audio_file_path,"rb")
 data = binascii.hexlify(audio_file.read()) 
 return data

def inject_audio_to_image(image_path):
 audio_data = read_audio_file()
 image_file = open(image_path,"rb")
 data = binascii.hexlify(image_file.read())
 data3 = data + read_audio_file()
 bin_data = binascii.unhexlify(data3)
 fi = open(injected_image,"wb")
 fi.write(bin_data)
 fi.close() 


read_audio_file()
inject_audio_to_image(image_template)

