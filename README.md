# graphql_fastapi_not_clean_architecture

実行手順

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

サーバーが立ち上がると DB が作られるので、下記データをインサート

```
INSERT INTO users VALUES(1, 'yamada', 'test@example.com');
INSERT INTO tasks VALUES(1, '要件定義', '未完了', 1);
```

GraphQL で実行する場合は下記からクエリを実行

```
http://127.0.0.1:8000/graphql/
```

ID には Base64 でエンコードする必要がある。
User:1 → VXNlcjox

REST で実行する場合は下記からクエリを実行

```
http://127.0.0.1:8000/docs/
```
