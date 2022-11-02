# all is anaconda env creation
all: env

# 仮想環境含めた全削除
clean: delete remove

# 仮想環境構築
env:
	conda env create --file geektwitter.yaml

# 仮想環境削除
remove:
	conda remove -n gt --all -y

# db:reset
reset: delete create

# db:create
create:
	chmod 764 ./db/create_db.sh
	./db/create_db.sh

# db:delete
delete:
	rm -f ./db/test.db

# 実行
exe:
	python app.py