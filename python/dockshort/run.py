#!/usr/bin/python

import os
import subprocess

"""
Command runner

Issues commands in the shell
"""

def execute(command_tokens):
    """ Runs command (first token), replacing current process
    """
    print ' '.join(command_tokens)
    os.execvp(command_tokens[0], command_tokens)

def call(command_tokens):
    """ Runs a command (first token), and resumes python script

    Returns the call object
    """
    return subprocess.call(comamnd_tokens)
