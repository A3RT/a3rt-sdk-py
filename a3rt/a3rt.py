# -*- coding: utf-8 -*-

import json
import requests


class API(object):

    def __init__(self, apikey=None, api_secret=None):
        self.api_url = "https://api.a3rt.recruit-tech.co.jp/"
        self.apikey = apikey

    def request(self, endpoint, method="GET", file=None, params=None):
        url = self.api_url + endpoint
        params.update({"apikey": self.apikey})

        try:
            with requests.Session() as s:
                if method == "GET":
                    response = s.get(url, params=params)
                else:
                    response = s.post(url, files=file, data=params)
        except requests.RequestException as e:
            raise e

        content = ""
        if len(response.content) > 0:
            content = json.loads(response.content.decode("utf-8"))

        return content

    def text_suggest(self, **params):
        """Text Suggest API

        Parameters
        ----------
        - previous_description (必須): 文を生成するための入力文を指定します
        - style (任意): 生成する文の種類を指定します。現代文／和歌／プログラミング言語（Go） の３種類から選べます。
        - separation (任意): 生成する文の長さを指定します。単語／フレーズ／センテンスの３種類から選べます。

        Docs
        ----
        https://a3rt.recruit-tech.co.jp/product/textSuggestAPI/
        """

        endpoint = "text_suggest/v1/predict"
        return self.request(endpoint, params=params)

    def text_suggest_v2(self, **params):
        """Text Suggest API Version2

        Parameters
        ----------
        - previous_description (必須): 文を生成するための入力文を指定します
        - style (任意): 生成する文の種類を指定します。現代文／和歌／プログラミング言語（Go）／ユーザー独自モデルの４種類から選べます。
        - separation (任意): 生成する文の長さを指定します。単語／フレーズ／センテンスの３種類から選べます。

        Docs
        ----
        https://a3rt.recruit-tech.co.jp/product/textSuggestAPI/
        """

        endpoint = "text_suggest/v2/predict"
        return self.request(endpoint, params=params)

    def talk(self, **params):
        """Talk API

        Parameters
        ----------
        - query (必須): 入力テキストを指定します

        Docs
        ----
        https://a3rt.recruit-tech.co.jp/product/talkAPI/
        """

        endpoint = "talk/v1/smalltalk"
        return self.request(endpoint, "POST", params=params)

    def proofreading(self, **params):
        """Proofreading API

        Parameters
        ----------
        - sentence (必須): チェック対象となる文を入力します
        - sensitivity (任意): チェック感度を３段階で指定します。highが誤字の指摘が多く、lowは少なく、mediumはその中間です。

        Docs
        ----
        https://a3rt.recruit-tech.co.jp/product/proofreadingAPI/
        """

        endpoint = "proofreading/v1/typo"
        return self.request(endpoint, params=params)

    def image_influence(self, **params):
        """Image Influence API

        Parameters
        ----------
        - predict (必須): 予想点を0~9点で指定します
        - imagefile (必須): 採点したい画像を指定します

        Docs
        ----
        https://a3rt.recruit-tech.co.jp/product/imageInfluenceAPI/
        """

        endpoint = "image_influence/v1/meat_score"
        file = {"imagefile": open(params["imagefile"], "rb")}
        del params["imagefile"]
        return self.request(endpoint, "POST", file=file, params=params)

    def text_classification(self, **params):
        """Text Classification API

        Parameters
        ----------
        - model_id (必須): モデルIDを指定します。空の場合はdefault
        - text (必須): 予測したいテキストを指定します。最大1000文字, 最大500単語

        Docs
        ----
        https://a3rt.recruit-tech.co.jp/product/textClassificationAPI/
        """

        endpoint = "text_classification/v1/classify"
        return self.request(endpoint, "POST", params=params)
