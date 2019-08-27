To reproduce this issue, run the following commands. 
Get `poetry` from here: https://poetry.eustace.io/docs/#installation

```
$ git checkout 1.18.1
$ poetry install
$ poetry run ./repro.sh
```

To compare with 1.4.4:

```
$ git checkout 1.4.4
$ poetry update
$ poetry run ./repro.sh
```
