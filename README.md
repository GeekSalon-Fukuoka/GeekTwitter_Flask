# GeekTwitter_Flask
みなさんご存知、GeekTwitterをFlaskで作成してみた。

CRUD搭載＋ログイン機能。

## Environments
- MacOS
- Python 3.8.13(yamlに記載)
- shell zsh


## 環境構築
### 1. 仮想環境構築
```zsh
% make
```

### 2. 仮想環境の有効化
```zsh
% conda activate gt
```

### 3. DB構築
```zsh
% make reset
```

## Execution
仮想環境有効化後、実行
```zsh
# 以下はお好みでどうぞ！
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
% make delete
```

### Anaconda
#### 仮想環境構築
基本しなくていいが、仮想環境が構築されない場合
```zsh
% make anaconda
```

#### 仮想環境削除
```zsh
% conda deactivate
% make remove
```

