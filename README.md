# A3RT SDK for Python

`a3rt-sdk-py` is a Python library for [A3RT](https://a3rt.recruit-tech.co.jp/) APIs provided by Recruit Technologies Co., Ltd.

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
import a3rt

api = a3rt.API(apikey="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
```

## Example

### Text Suggest API

```python
api.text_suggest(previous_description="馬", style=0)
```

### Text Classification API

```python
api.text_classification(text="システムの企画から開発・運用まで幅広く関われます。", model_id="default")
```

### Talk API

```python
api.talk(query="こんにちは")
```

### Image Influence API

```python
api.image_influence(imagefile="sample.jpg", predict=1)
```

### Proofreading API

```python
api.proofreading(sentence="システムの規格から開発・運用まで幅広く関われます。")
```

## Author

- Ngo_Hong_Giang
- sahori_uchida
- yuki_okuda
