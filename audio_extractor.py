#!usr/bin/python

import binascii

injected_image = "123nn.png"
extracted_audio_result = "final_mp3.mp3"
def extract_audio():
 open_image_file = open(injected_image,"rb")
 data = open_image_file.read()
 hex_data = binascii.hexlify(data)
 audio_file_hex_data = hex_data[640362::]
 binary_data_for_audio_file = binascii.unhexlify(audio_file_hex_data)
 write_audio_file = open(extracted_audio_result,"wb")
 write_audio_file.write(binary_data_for_audio_file)
 write_audio_file.close()
extract_audio()
