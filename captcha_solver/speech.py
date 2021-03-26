#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Speech module. Text-to-speech classes - Sphinx, Google, WitAI, Amazon, and Azure. """
import asyncio
import json
import logging
import os
import re
import struct
import sys
import time
from datetime import datetime
from uuid import uuid4

import aiobotocore
import aiofiles

import requests
import speech_recognition as sr
import websockets

from pydub import AudioSegment

from captcha_solver import util
from captcha_solver.base import settings


async def mp3_to_wav(mp3_filename):
    """Convert mp3 to wav"""
    wav_filename = mp3_filename.replace(".mp3", ".wav")
    segment = AudioSegment.from_mp3(mp3_filename)
    sound = segment.set_channels(1).set_frame_rate(16000)
    garbage = len(sound) / 3.1
    sound = sound[+garbage:len(sound) - garbage]
    sound.export(wav_filename, format="wav")
    return wav_filename


class Google(object):
    async def get_text(self, mp3_filename):
        wav_filename = await mp3_to_wav(mp3_filename)
        # Initialize a new recognizer with the audio in memory as source
        recognizer = sr.Recognizer()
        with sr.AudioFile(wav_filename) as source:
            audio = recognizer.record(source)  # read the entire audio file

        # recognize speech using Google Speech Recognition
        audio_output = None
        try:
            audio_output = recognizer.recognize_google(audio)
            print("Google Speech Recognition: " + audio_output)
        except sr.UnknownValueError:
            logging.warning("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            logging.warning("Could not request results from Google Speech Recognition service; {0}".format(e))
        return audio_output

 
class WitAI(object):
    API_KEY = settings["speech"]["wit.ai"]["secret_key"]

    async def get_text(self, mp3_filename):
        wav_filename = await mp3_to_wav(mp3_filename)
        # Initialize a new recognizer with the audio in memory as source
        recognizer = sr.Recognizer()
        with sr.AudioFile(wav_filename) as source:
            audio = recognizer.record(source)  # read the entire audio file

        # recognize speech using WIT.AI Recognition
        audio_output = None
        try:
            # Llamamos al metodo de reconocimiento por wit y le pasamos el audio, y la key
            audio_output = recognizer.recognize_wit(audio, key=self.API_KEY)
            print("Wit.AI Recognition: " + audio_output)
        except sr.UnknownValueError:  # Definimos excepciones que se puedan presentar
            logging.warning("Wit.ai could not understand audio")
        except sr.RequestError as e:
            logging.warning("Could not request results from Wit.ia; {0}".format(e))

        return audio_output