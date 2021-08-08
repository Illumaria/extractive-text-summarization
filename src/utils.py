"""Supplementary functions"""
import logging
import logging.config
import os
import yaml


LOGGING_CONFIG_FILEPATH = "logging.conf.yml"

logger = logging.getLogger("ext_summarizer")


def setup_logging():
    """Set up the logger from config file"""
    with open(LOGGING_CONFIG_FILEPATH, 'r') as config_fin:
        cfg = yaml.safe_load(config_fin)
        os.makedirs(os.path.dirname(cfg['handlers']['file_handler']['filename']), exist_ok=True)
        logging.config.dictConfig(cfg)
