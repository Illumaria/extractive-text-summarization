# Work Log

`05.08.2021`:
* Did some paper analysis in order to choose the model architecture. The [MatchSum](https://github.com/maszhongming/MatchSum) model takes the second place in the [CNN / DM benchmark rating](https://paperswithcode.com/sota/extractive-document-summarization-on-cnn) on [Papers With Code](https://paperswithcode.com/) and has a relatively simple implementation. Other approaches like [Neural Extractive Text Summarization with Syntactic Compression](https://arxiv.org/pdf/1902.00863v2.pdf) on the first place or freshly released [Deep Differential Amplifier for Extractive Summarization](https://aclanthology.org/2021.acl-long.31.pdf) are also worth trying out but could require much more time to implement.

`06.08.2021`:
* `MatchSum` seems to be just an improvement of [BertSumExt](https://paperswithcode.com/paper/text-summarization-with-pretrained-encoders) models. Since the more fundamental approaches are easier to explain and tune, switched to this architecture.
* Fixed training scripts for [PreSumm](https://github.com/nlpyang/PreSumm) repository, because they're kinda outdated (like designed for PyTorch 1.1.0).
* Wrote a script for dataset downloading and preprocessing.
* Trained the model for 500 steps on combined CNN/DM dataset.
* Faced a problem of not obvious model inference.
* The results of the experiments can be found in a [separate repository](https://github.com/Illumaria/extractive-text-summarization-experiments).

`08.08.2021`:
* The task implies to use custom model or some model to retrain/fine-tune. However, due to the limited time, I will implement [Bert Extractive Summarizer](https://github.com/dmmiller612/bert-extractive-summarizer) for now.
* Made Flask application that summarizes texts.
* Added Docker image implementation. No Kubernetes configs and deployments for now, because I don't have any cloud resources available.

## Задача

Одной из областей применения обработки естественного языка является суммаризация текстов, подразумевающая создание краткой версии текста, документа, статьи с помощью машинного обучения. Есть два вида суммаризации: абстрактная или генерирующая, когда на основе существующего текста модель создает новый текст меньшего объема, как правило в исходном тексте представленный лишь частично, и экстрактная или извлекающая, когда модель ранжирует предложения, фразы или абзацы в тексте и отбирает заданное пользователем число наиболее важных элементов, при этом идут они в той же последовательности, что и в оригинальном тексте, из-за чего как правило нарушается связность результата.

В данном случае предлагается реализовать последний подход для суммаризации текстов, как требующий меньше времени и ресурсов.

Детали:
- [X] Предложенное решение должно принимать на вход текст, количество предложений в итоговом тексте (или минимальное и максимальное число предложений в нем) и выдавать итоговый текст.
- [X] Предпочтительно, чтобы решение было основано на нейросетях с использованием PyTorch или TensorFlow, исключение возможно, если Вы решите представить решение как веб-сервис.
- [X] В остальном допускается использование любых библиотек Python.
- [ ] Допускается использование готовых моделей при условии, что будет представлено не оригинальное решение, а дообученное на новых данных, и в решении показано понимание архитектуры модели и причины её выбора.
  - Обучение было произведено, но для другой модели — не той, которая используется в данном решении. Эксперименты с обучением вынесены в [отдельный](https://github.com/Illumaria/extractive-text-summarization-experiments) репозиторий.
- [X] Для решения данной задачи Вы вправе использовать любые подходящие датасеты.
  - Была использована комбинация CNN и Daily Mail. Рассматривались также XSum, NYT и Reddit.
- [X] Мы предлагаем Вам самостоятельно выбрать метрику для оценки качества модели, но выбор той или иной метрики должен быть обоснован.
  - Стандартной метрикой в задачах суммаризации является ROUGE (ROUGE-1, ROUGE-2, ROUGE-L).

В качестве результата ожидается репозиторий, содержащий:
- [X] журнал в котором вы ведете ход работ, описываете решение, основные шаги в подготовке данных и обучении модели, эксперименты;
- [X] исходный код и скрипт для тестирования с тестовым датасетом;
- [ ] если решение представлено в Jupyter notebook, то журнал и код можно объединить и ограничиться несколькими примерами суммаризации в ноутбуке.

Будет плюсом:
- [ ] обученная модель является мультиязычной (хотя бы два языка);
- [X] в решении представлены плюсы и минусы существующего решения и варианты дальнейшего улучшения модели:
  - использование готовой библиотеки затрудняет внесение исправлений и добавление улучшений;
  - текущее решение не всегда выдаёт заданное число предложений (см. предыдущий пункт).

Будет огромным плюсом:
- [X] создано Flask-приложение для работы с моделью;
- [X] приложение и модель развернуты в Докере на удаленном сервере;
- [ ] пользователь может послать cURL запрос с текстом и количеством предложений для суммаризации и получить в ответ суммаризированный текст.
