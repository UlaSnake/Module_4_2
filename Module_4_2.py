def test_function ():

    def inner_function ():
        print("Я в области видимости функции test_function")

    inner_function() # вызов функции внутри функции. Ничего не возвращает

#inner_function() # вызов вне функции не работает, приводит к ошибке, так как inner_function определена только внутри test_function и не доступна за её пределами.

test_function () # в данном случае успешно срабатывает