# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import html5lib
import urllib
import os
import math
import xlwt
import time
import shutil
import sys
from os import listdir
from shutil import copyfile
from xlrd import open_workbook
#from datetime import datetime, date, timedelta
#import calendar

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


for archivo in listdir('../..'):
    if archivo.endswith(".txt"):
        nuevo_archivo = open("../../"+archivo, "r")
        print(nuevo_archivo.read())