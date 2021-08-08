# Extractive Text Summarization

A demo project on extractive text summarization.

## Usage

Prepare data:

```bash
python scripts/download_dataset.py
sh scripts/download_corenlp.sh
python src/preprocess.py -mode tokenize -raw_path raw_stories -save_path tokenized
python src/preprocess.py -mode format_to_lines -raw_path tokenized -save_path json_data -n_cpus 1 -use_bert_basic_tokenizer false -map_path urls
python src/preprocess.py -mode format_to_bert -raw_path json_data -save_path bert_data -lower -n_cpus 1 -log_file logs/preprocess.log
```

Train model:

```bash
python src/train.py -task ext -mode train -bert_data_path bert_data -ext_dropout 0.1 -model_path checkpoints -lr 2e-3 -visible_gpus 1 -report_every 50 -save_checkpoint_steps 250 -batch_size 2000 -train_steps 500 -accum_count 2 -log_file logs/ext_bert_cnndm -use_interval true -warmup_steps 100 -max_pos 512
```

Evaluate model:

```bash
python src/train.py -task ext -mode validate -batch_size 2000 -test_batch_size 500 -bert_data_path bert_data -log_file logs/val_ext_bert_cnndm -model_path checkpoints -sep_optim true -use_interval true -visible_gpus 1 -max_pos 512 -max_length 200 -alpha 0.95 -min_length 50 -result_path logs/ext_bert_cnndm
```

With local or virtual environment:

```bash
git clone https://github.com/Illumaria/extractive-text-summarization.git
cd extractive-text-summarization/
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
FLASK_APP=app.py flask run --host=0.0.0.0 --port=5000
```

With Docker:

```bash
git clone https://github.com/Illumaria/extractive-text-summarization.git
cd extractive-text-summarization/
docker build -t ext_sum .
docker run --rm -p <YOUR_PORT>:5000 ext_sum
```