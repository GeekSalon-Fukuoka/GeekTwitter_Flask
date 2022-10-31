# all is Environment creation and Execution
all: anaconda clean db

# db:reset
reset: clean db

# db delete
clean:
	cd db
	rm -f test.db

# db:create
db:
	cd db
	chmod 764 create_db.sh
	./create_db.sh

# 仮想環境構築
anaconda:
	conda env create --file geektwitter.yaml
	conda activate gt

# 実行
exe:
	python app.py