from django.views.generic import DetailView, FormView
from .models import Message
from .forms import MessageForm


#class MassageDetailView(DetailView):
 #   model = Message

class MessageAddView(FormView):
    form_class = MessageForm
    template_name = 'contact/message_form.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()   #bo form jest instancja ModelForm, ktory posiada metode save()
        return super(MessageAddView, self).form_valid(form)

