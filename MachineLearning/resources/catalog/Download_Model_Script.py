# Copyright Activeeon 2007-2021. All rights reserved.
# -*- coding: utf-8 -*-
"""Proactive Download_Model for Machine Learning

This module contains the Python script for the Download_Model task.
"""
import ssl
import urllib.request

global variables, resultMetadata

__file__ = variables.get("PA_TASK_NAME")
print("BEGIN " + __file__)

# -------------------------------------------------------------
# Import an external python script containing a collection of
# common utility Python functions and classes
PA_CATALOG_REST_URL = variables.get("PA_CATALOG_REST_URL")
PA_PYTHON_UTILS_URL = PA_CATALOG_REST_URL + "/buckets/machine-learning/resources/Utils_Script/raw"
if PA_PYTHON_UTILS_URL.startswith('https'):
    exec(urllib.request.urlopen(PA_PYTHON_UTILS_URL, context=ssl._create_unverified_context()).read(), globals())
else:
    exec(urllib.request.urlopen(PA_PYTHON_UTILS_URL).read(), globals())
global check_task_is_enabled, get_input_variables
global get_and_decompress_model, export_model_for_download

# -------------------------------------------------------------
# Check if the Python task is enabled or not
check_task_is_enabled()

# -------------------------------------------------------------
# Get data from the propagated variables
#
input_variables = {'task.model_id': None}
get_input_variables(input_variables)

model_id = input_variables['task.model_id']
model = get_and_decompress_model(model_id)

# -------------------------------------------------------------
# Expose model for download
#
export_model_for_download(model)

# -------------------------------------------------------------
print("END " + __file__)