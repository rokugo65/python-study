from django.shortcuts import render
from django.views.generic import TemplateView

from address_retrieval_app.forms import ZipCodeForm
from address_retrieval_app.logic import AddressRetrieval

class TopView(TemplateView):
    template_name = "top.html"

    def get(self, request, *args, **kwargs):
        context = super(TopView, self).get_context_data(**kwargs)
        return render(self.request, self.template_name, context)
    
class ResultView(TemplateView):
    template_name = "result.html"

    def post(self, request, *args, **kwargs):
        context = super(ResultView, self).get_context_data(**kwargs)

        form = ZipCodeForm(request.POST)

        if form.is_valid():
            AR = AddressRetrieval()
            zipCode = form.cleaned_data['zipCode']
            
            context['zipCode'] = zipCode
            context['address'] = AR.ZipCode2Address(zipCode)
        else :
            context['zipCode'] = '郵便番号が入力されていません'
            context['address'] = ''

        return render(self.request, self.template_name, context)

    