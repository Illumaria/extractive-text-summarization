# Work Log

`05.08.2021`:
* Choose the model. The [MatchSum](https://github.com/maszhongming/MatchSum) model takes the second place in the [CNN / DM benchmark rating](https://paperswithcode.com/sota/extractive-document-summarization-on-cnn) on [Papers With Code](https://paperswithcode.com/) and has a very simple (in terms of file number) implementation. Other approaches like [Neural Extractive Text Summarization with Syntactic Compression](https://arxiv.org/pdf/1902.00863v2.pdf) on the first place or freshly released [Deep Differential Amplifier for Extractive Summarization](https://aclanthology.org/2021.acl-long.31.pdf) are also worth trying out but could require much more time to implement.
`06.08.2021`:
* `MatchSum` seems to be just an improvement of [BertSumExt](https://paperswithcode.com/paper/text-summarization-with-pretrained-encoders) models. Since the more fundamental approaches are easier to explain and tune, switching to this architecture.
* Fixed training scripts for [PreSumm](https://github.com/nlpyang/PreSumm) repository, because they're kinda outdated (like designed for PyTorch 1.1.0).
* Wrote a single script for dataset downloading and preprocessing.
* Trained the model for 500 steps on combined CNN/DM dataset.
* Faced a problem of not obvious model inference.
`08.08.2021`:
* The task implies to use custom model or some model to retrain/fine-tune. However, due to the limited time, I will implement [Bert Extractive Summarizer](https://github.com/dmmiller612/bert-extractive-summarizer) for now.