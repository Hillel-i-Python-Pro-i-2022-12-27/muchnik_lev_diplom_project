from django.core.mail import EmailMessage
from django.shortcuts import render

def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        # Отправка письма на почту
        try:
            subject = 'Новая заявка'
            message = f'Имя: {name}\nТелефон: {phone}\nПочта: {email}'
            email = EmailMessage(subject, message, to=['mira8@ukr.net'])
            email.send()
        except Exception as e:
            print(e)  # Выводим ошибку на консоль для отладки

        # Возвращаем пользователя на ту же страницу с пустыми полями формы
        return render(request, '_helpers/_header.html', {'success': True})

    # Если это GET-запрос, просто отображаем страницу с формой
    return render(request, '_helpers/_header.html')
