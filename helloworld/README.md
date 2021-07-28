# Note

## http method and routing

```python
app = FastAPI()

@app.get('/')
def read_root():
    return {"Hello": "World"}
```

- FastAPIオブジェクトのデコレータでメソッド・ルーティングを設定できる
- ↑の例なら、getメソッドでルートパス


## operate parameters

```python
@app.get('/items/{item_id}')
def read_item(item_id: int, q: str = None):
    return {"item id": item_id, "query": q}
```

- パス文字列に通常通り変数を埋め込む（`{}`）感じでパスに変数を含めることができる
  - これを `'...{}'.format(item_id)` とすると item_id is not defined で例外になる。
- デコレートされる関数のルール
  - 引数の変数名が {} に記載したものと一致している必要がある。（今回ならitem_id）どうやらそれをキーにしてFastAPIが紐付けてくれてるみたい。
  - で、それ以外の変数はすべてクエリパラメータになる
  - パラメータ名も同様に関数の引数名と紐付いている


## Automatic document generation by FastAPI

FastAPIが自動でドキュメントを生成してくれる。

- 自動対話型APIドキュメント
  - サーバー実行中に `/docs` にアクセスする
  - 開発時はたとえば、 http://127.0.0.1:8000/docs にアクセスする
- 代替ドキュメント
  - サーバー実行中に `/redoc` にアクセスする
  - 開発時はたとえば、 http://127.0.0.1:8000/redoc にアクセスする
