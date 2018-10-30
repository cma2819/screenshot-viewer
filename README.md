# What's this?
Screenshot Viewerは、主にキャプチャソフトで保存したスクリーンショットを、余計な操作なしで即座に表示するためのツールです。
街へいこうよ どうぶつの森のRTAのために作りました。

## Install
動作にはPython3の環境が必要です。[Python.jpの環境構築ガイド](https://www.python.jp/install/install.html)が簡潔にまとまっていてわかりやすいです。

手順に従ってインストールした上で、コマンドプロンプト（あるいはそれに準ずるもの）で以下のコマンドを入力してみてください。
```
> python --version
```

正しくインストールができていれば、以下のような表示になります。

```
Python 3.6.4 :: Anaconda, Inc.
```
※環境によって差異はありますが、「python」コマンドに反応していれば大丈夫です。

Pythonのインストールが完了したら、本プログラムをダウンロードしてください。
GitHub（恐らくみなさんが見ているであろうページ）の右上あたり、
「Clone or download」→「Download ZIP」でダウンロードできます。

※GitHubにお慣れになられている方々は、Cloneするなりなんなり自由にしてください。

ダウンロードしたzipを好きなフォルダに展開して下さい。

## Setup
Python環境に必要なライブラリをインストールします。

展開したフォルダでコマンドプロンプトを起動してください。

```
例：
> D:\
> cd D:\develop\ss_viewer\screenshot-viewer
```

以下のコマンドでライブラリをインストールします。
```
> python setup.py install
```

（私が未熟故に）色々怒られるかもしれませんが、以下の表記が出たら多分問題なくインストールができています。
```
Finished processing dependencies for ScreenShot-Viewer==0.9.0
```

## How to Use
実行の際には、フォルダ内の「main.py」を実行します。

もしかしたら「main.py」をダブルクリックとかするだけでいけるかもしれません。

いけなかった場合は、先ほどと同様にこのフォルダでコマンドプロンプトを起動し、以下のコマンドを入力してください。

```
> python main.py
```

起動すると、対象フォルダを設定する画面が表示されます。

スクリーンショット機能で画像が保存されるフォルダを選択し、「フォルダーの選択」を押下してください。

ウィンドウ起動中は常に選択されたフォルダを監視し、スクリーンショット機能で新しい画像が保存された際に自動的にウィンドウに表示されます。

※フォルダーを選択しなおしたい場合は起動しなおしてください。作りこみ甘くてゴメンナサイ

「Reset」ボタンを押下すると、表示されていた画像が消えます。

画像を一度消すことで、似たような画面を再度キャプチャする際にキャプチャ漏れが起きることを防ぐことができます。

使い方は以上です。

## Contact
質問は[Twitter](https://twitter.com/cma2819)か、Discordの個人宛（cma2819#2218）までご連絡ください。