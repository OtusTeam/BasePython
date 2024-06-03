from django.http import HttpResponseRedirect
from django.shortcuts import render
from .tasks import send_admin_message
from celery.result import AsyncResult


# Create your views here.
def contact_view(request):
    if request.method == 'POST':
        # send_admin_message()  # simple call
        task_result = send_admin_message.delay(message='New message')
        print(type(task_result))
        print(task_result)
        print(task_result.ready())
        print(task_result.state)
        return HttpResponseRedirect('/contacts/')
    return render(request, 'contacts/contacts.html')


def status_view(request, task_id):
    task_result = AsyncResult(task_id)

    result = None
    if task_result.ready():
        result = task_result.get()

    context = {'task_result': task_result, 'result': result}
    return render(request, 'contacts/status.html', context)
