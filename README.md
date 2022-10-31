# GeekTwitter_Flask
みなさんご存知、GeekTwitterをFlaskで作成してみた。

CRUD搭載＋ログイン機能。

## Environment
1. 環境構築
```zsh
% make
```

2. 有効化・非有効化
```zsh
% conda activate gt
% conda deactivate gt
```

## Execution
仮想環境有効化後、実行
```zsh
# 以下はお好みでどうぞ！(こだわりなければ、make exeで)
% make exe
% python app.py
```

## Makefileコマンド
### DBのリセット
rails db:resetと似た効果あり。DB削除と作成を行う。
```zsh
% make reset
```

### DB構築
基本しなくていいが、`./db`内に作成されない場合
```zsh
% make create
```
### DB削除
DBを削除のみしたい場合
```zsh
% make clean
```

### Anaconda仮想環境構築
基本しなくていいが、仮想環境が構築されない場合
```zsh
% make anaconda
```
