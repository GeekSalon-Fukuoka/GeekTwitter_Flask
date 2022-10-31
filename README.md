# GeekTwitter_Flask
みなさんご存知、GeekTwitterをFlaskで作成してみた。

CRUD搭載＋ログイン機能。

## Environment
### Anaconda
1. 仮想環境構築
```zsh
% conda env create --file geektwitter.yaml
```

2. 有効化・非有効化
```zsh
% conda activate gt
% conda deactivate gt
```

### DBの構築
以下の３つの手順で作成
```zsh
% python
>>> from app import db
>>> db.create_all()
```

## Execution
仮想環境有効化後、実行
```zsh
% python app.py
```
