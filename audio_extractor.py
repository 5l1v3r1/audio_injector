#!usr/bin/python

import binascii,sys

if len(sys.argv) != 4:
  print "Usage : python audio_extractor.py [injected_image_file] [audio_file_result] [final_offset]"
  sys.exit(0)
injected_image = sys.argv[1]
extracted_audio_result = sys.argv[2]
final_offset = sys.argv[3]
def extract_audio():
 open_image_file = open(injected_image,"rb")
 data = open_image_file.read()
 hex_data = binascii.hexlify(data)
 audio_file_hex_data = hex_data[int(final_offset)::]
 binary_data_for_audio_file = binascii.unhexlify(audio_file_hex_data)
 write_audio_file = open(extracted_audio_result,"wb")
 write_audio_file.write(binary_data_for_audio_file)
 write_audio_file.close()
extract_audio()
