# A3RT SDK for Python

これはA3RTの[A3RT](https://a3rt.recruit-tech.co.jp/)をPythonから利用するためのSDKです。

## Requirement

- requests

## Installation

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
