## langchainを使って会話を保持する
### how to use
1. config/config.yamlに以下のようにopenaiのAPI_KEYをセット

```
openai_api:
  api_key: {your_api_key}
```

2. poetry install

3. python work.py

直近2回分の会話内容を保持するchatが可能。

[sample](./images/sample.png)
