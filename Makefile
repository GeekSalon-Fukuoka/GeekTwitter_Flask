# all is Environment creation and Execution
all: anaconda clean db

# db:reset
reset: clean create

# db delete
clean:
	rm -f ./db/test.db

# db:create
create:
	cd db
	chmod 764 ./db/create_db.sh
	./db/create_db.sh

# 仮想環境構築
anaconda:
	conda env create --file geektwitter.yaml
	conda activate gt

# 実行
exe:
	python app.py