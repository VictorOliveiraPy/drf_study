# Notes study - project

# normal run
$ docker-compose exec movies pytest

# disable warnings
$ docker-compose exec study pytest -p no:warnings

# run only the last failed tests
$ docker-compose exec study pytest --lf

# run only the tests with names that match the string expression
$ docker-compose exec study pytest -k "movie and not all_movies"

# stop the test session after the first failure
$ docker-compose exec study pytest -x

# enter PDB after first failure then end the test session
$ docker-compose exec study pytest -x --pdb

# stop the test run after two failures
$ docker-compose exec study pytest --maxfail=2

# show local variables in tracebacks
$ docker-compose exec study pytest -l

# list the 2 slowest tests
$ docker-compose exec study pytest  --durations=2

# Por que utilizar APIView ?

Obviamente, você pode se mover mais rápido com ViewSets e roteadores - quando seus endpoints de API são mapeados de volta para o modelo - mas você sacrifica a legibilidade, pois a lógica está enterrada. Isso pode dificultar a integração de um novo desenvolvedor em seu projeto.

Explicit is better than implicit.
