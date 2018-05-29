from django.shortcuts import HttpResponse, render, redirect
from django.views.generic import ListView
from Chat.models import Chat
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class ChatView(ListView,LoginRequiredMixin):
    model = Chat
    template_name = 'Chat/chat.html'

@csrf_exempt
def post(request):
    if request.method == 'POST' and request.user.is_authenticated:
        post_type = request.POST.get('post_type')
        if post_type == 'send_chat':
            new_chat = Chat.objects.create(
                content = request.POST.get('content'),
                sender = request.user,
            )
            new_chat.save()
            return HttpResponse()
        elif post_type == 'get_chat':
            last_chat_id = int(request.POST.get('last_chat_id'))
            chats = Chat.objects.filter(id__gt = last_chat_id)
            return render(request, 'Chat/chat_update.html', {'chats': chats})
    else:
        raise redirect('login/')
