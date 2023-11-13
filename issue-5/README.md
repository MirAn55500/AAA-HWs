# Testing
Чтобы запустить тесты, введите в консоли в директории issue-5:  
"python -m pytest what_is_year_now_test.py"

Чтобы убрать лишнюю информацию, можно добавить параметр -q

Чтобы получить процент покрытия тестами, необходимо добавить:  
"--cov=what_is_year_now"

Получится:  
"python -m pytest -q what_is_year_now_test.py --cov=what_is_year_now"

Для генерации отчёта в формате html введите в конце: "--cov-report html"  
"python -m pytest -q -v what_is_year_now_test.py --cov=what_is_year_now --cov-report html"

