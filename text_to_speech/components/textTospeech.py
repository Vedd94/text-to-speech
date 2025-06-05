from text_to_speech.exception import TTSException
from text_to_speech.logger import logger
from text_to_speech.entity.config_entity import TTSConfig
from text_to_speech.constants import *
import os
from gtts import gTTS
import base64
import sys

class TTSapplication():
    def __init__(self, app_config=TTSConfig())-> None:
        try:
            self.app_config = app_config
            self.artifact_dir = app_config.artifact_dir
            self.audio_dir = app_config.audio_dir
            self.text_dir = app_config.text_dir
        except Exception as e:
            raise TTSException(e,sys)
        
    def text2speech(self, text, accent):
            try:
                text_filename = TEXT_FILE_NAME
                text_file_path = os.path.join(self.text_dir, TEXT_FILE_NAME)
                os.makedirs(self.text_dir, exist_ok=True)
                with open(text_file_path, 'a+') as file:
                    file.write(f'\n{text}')

                #Create oject for gtts
                tts = gTTS(text=text, lang='en', tld = accent, slow = False) #b

                file_name = f"converted_file{CURRENT_TIME_STAMP}"

                os.makedirs(self.audio_dir, exist_ok=True)
                audio_path = os.path.join(self.audio_dir, file_name)

                # save audio file

                tts.save(audio_path)

                with open(audio_path, 'rb') as file:
                    my_string = base64.b64encode(file.read())

                return my_string
            
            except Exception as e:
                 raise TTSException(e, sys)