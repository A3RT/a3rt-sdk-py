# A3RT SDK for Python

`a3rt-sdk-py` is a Python library for [A3RT](https://a3rt.recruit.co.jp/) APIs provided by Recruit Co., Ltd.

## Requirement

- requests

## Installation

To install a3rt-sdk-py from PyPI: 

```shell
$ pip install a3rt-sdk-py
```

You can also install from source code:

```shell
$ git clone git@github.com:A3RT/a3rt-sdk-py.git
$ cd a3rt-sdk-py
$ python setup.py install
```

## Usage

```python
from a3rt import a3rt

api = a3rt.API(apikey="YOURAPIKEY")
```

## Example

### Text Suggest API Version 2

```python
api.text_suggest(previous_description="馬", style="0")
```

### Text Classification API

```python
api.text_classification(text="システムの企画から開発・運用まで幅広く関われます。", model_id="default")
```

### Talk API

```python
api.talk(query="こんにちは")
```

### Proofreading API Version2

```python
api.proofreading(sentence="システムの規格から開発・運用まで幅広く関われます。")
```

### Named Entity API

```python
api.named_entity(sentence="佐藤太郎さんの誕生日は1月1日です。")
```
