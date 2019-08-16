from django.contrib import admin
from django.urls import path

import address_retrieval_app.views as AddressRetrievalView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AddressRetrievalView.TopView.as_view()),
    path('result/', AddressRetrievalView.ResultView.as_view()),
]
