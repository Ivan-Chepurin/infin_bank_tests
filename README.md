# Как запустить тесты:
>1 Сначала нужно установить Python

>2 Открыть консоль в пути до папки проекта: 
>>C:\path\to\infin_bank_test

>3 Ввести команду 
>> pip install -r requirements.txt
> 
> Это утановит все необходимые зависимости

> 4 Ввести команду 
>> behave -f allure_behave.formatter:AllureFormatter -o reports ./features
> 
> Это запустит тесты а и сохранит отчеты в формате Allure
>
> Для просмотра результатов необходим Allure
