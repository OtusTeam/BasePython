from django.shortcuts import render
from .models import Animal
from .tasks import get_metrics, send_email_task


def index_view(request):
    result = get_metrics.delay(url=request.path, method=request.method)
    print(result)
    print(result.id)
    print(type(result))
    print(result.status)
    print(result.result)
    # animals = Animal.objects.all().select_related('category')
    animals = Animal.objects.all().select_related('category').prefetch_related('category__foods')
    # animals = Animal.objects.all().prefetch_related('category__foods')

    return render(request, 'mainapp/index.html', {'animals': animals})


def contact_view(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        send_email_task.delay(
            from_email='admin@admin',
            to_email='help@admin.com',
            title='to us',
            text=text
        )
        return render(request, 'mainapp/contact.html')
    return render(request, 'mainapp/contact.html')


def get_task_result_view(request, task_id):
    result = get_metrics.AsyncResult(task_id)

    context = {
        'task_id': result.id,
        'status': result.status,
        'result': result.result
    }
    return render(request, 'mainapp/task_result.html', context=context)