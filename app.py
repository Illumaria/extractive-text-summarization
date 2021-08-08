"""Main application logic"""
import logging

from flask import Flask, jsonify, render_template, request
from summarizer import Summarizer

from src.utils import setup_logging


DEFAULT_MODEL_NAME = 'distilbert-base-uncased'
DEFAULT_NUM_SENTENCES = 1

setup_logging()
logger = logging.getLogger('ext_summarizer')

summarization_model = Summarizer(model=DEFAULT_MODEL_NAME)

app = Flask(__name__)


@app.route('/')
def index():
    """Main service page"""
    return render_template('index.html')


@app.route('/summarize', methods=['POST'])
def summarize():
    """Endpoint for text summarization"""
    logger.info('Processing input...')
    errors = []
    summary = ''
    if request.method == 'POST':
        data = request.get_json()
        text = data.get('text', '')
        logger.debug("text: %s", text)
        num_sentences = int(data.get('num_sentences', DEFAULT_NUM_SENTENCES))
        logger.debug("num_sentences: %s", num_sentences)

        summary = summarization_model(text, num_sentences=num_sentences)
        logger.debug("summary: %s", summary)

    logger.debug('Returning summary: %s', summary)
    return jsonify({"errors": errors, "summary": summary})


if __name__ == "__main__":
    app.run()
