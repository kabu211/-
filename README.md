# NetMonitor

ブラウザでネットワークの状態を確認できるダッシュボードを目指す学習用プロジェクトです。現在は初期開発段階で、通信の測定や記録は行いません。

## 必要なもの

- Python 3.14.9

## セットアップ

プロジェクトのディレクトリで仮想環境を作成し、有効化します。

```bash
/Library/Frameworks/Python.framework/Versions/3.14/bin/python3.14 -m venv .venv-3.14
source .venv-3.14/bin/activate
```

必要なライブラリをインストールします。

```bash
python -m pip install -r requirements.txt
```

## アプリの起動

```bash
python app.py
```

ブラウザで <http://127.0.0.1:5000/> を開きます。終了するときはターミナルで `Ctrl+C` を押します。

## テスト

仮想環境を有効にした状態で実行します。

```bash
python -m pytest
```

## ファイル構成

- `app.py`: FlaskアプリとトップページのURLを定義します。
- `templates/index.html`: ブラウザに表示するトップページです。
- `tests/test_app.py`: トップページの応答と表示内容を確認します。
- `requirements.txt`: このプロジェクトが使うPythonライブラリを記録します。
- `.gitignore`: 仮想環境、キャッシュ、秘密情報、ローカルデータをGitの対象外にします。
