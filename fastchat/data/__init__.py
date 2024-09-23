"""
convert html to markdown with basic data cleaning, deduplication
python3 -m fastchat.data.clean_sharegpt --in sharegpt_html.json --out sharegpt_clean.json
"""
import argparse
from concurrent.futures import ProcessPoolExecutor
import json
import logging
import re
from typing import Dict, Union
import bs4
import markdownify  # == 0.11.6
from tqdm import tqdm