# Testing
Чтобы запустить тесты, введите в консоли в директории issue-1:  
"python -m doctest testing.py"

Для более подробной информации из тестов добавьте параметр -v:  
"python -m doctest -v testing.py"

Если хотите пропускать пробелы, добавьте флаг  
"-o NORMALIZE_WHITESPACE"

В итоге, у вас получится:  
"python -m doctest -o NORMALIZE_WHITESPACE -v testing.py" 
