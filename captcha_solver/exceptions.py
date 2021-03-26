#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Exceptions used in library. """


class captcha_solverError(Exception):
    """ captcha_solver base exception. """


class SafePassage(captcha_solverError):
    """ Raised when all checks have passed. Such as being detected or try again. """
    pass


class ResolveMoreLater(captcha_solverError):
    """ Raised when audio deciphering is incorrect and we can try again. """
    pass


class TryAgain(captcha_solverError):
    """ Raised when audio deciphering is incorrect and we can try again. """
    pass


class ReloadError(captcha_solverError):
    """ Raised when audio file doesn't reload to a new one. """
    pass


class DownloadError(captcha_solverError):
    """ Raised when downloading the audio file errors. """
    pass


class ButtonError(captcha_solverError):
    """ Raised when a button doesn't appear. """
    pass


class IframeError(captcha_solverError):
    """ Raised when defacing page times out. """
    pass
