# Audio_injector
Python script to inject audio files to images and extract it.

To inject audio file run :
 python audio_injector.py [template_image] [template_audio_file] [final_image_file].

To extract audio file from image run :
 python audio_extractor.py [injected_image_file] [audio_file_result] [final_offset].

#Examples :
To inject image :

.. *python audio_injector.py 123.png a.mp3 askar.png

To extract audio from image :

.. *python audio_extractor.py askar.png askar.mp3 640420
