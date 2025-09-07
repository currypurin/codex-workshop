# new-feature: シンプル Flask アプリ

このフォルダには、`GET /hello?name=NAME` に対して `Hello, NAME!` を返す最小の Flask アプリが含まれます。

## 前提
- Python 3.10 以上
- 仮想環境の利用を推奨

## セットアップ
```bash
cd new-feature
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -U pip
pip install -r requirements.txt
```

## 起動
```bash
python app.py
# デフォルト: http://127.0.0.1:5000
```

## 動作確認
ブラウザまたは curl で以下にアクセス:

- 名前あり: `http://127.0.0.1:5000/hello?name=Alice` → `Hello, Alice!`
- 名前省略: `http://127.0.0.1:5000/hello` → `Hello, World!`

## 補足
- 本番運用では Gunicorn/Uvicorn 等の WSGI/ASGI サーバを利用してください。
- デバッグ実行（`debug=True`）は開発用途のみです。

