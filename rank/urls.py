from django.conf.urls import url
from .views import get_ranks,commit_score
urlpatterns = [
    url(r'^get_rank$',get_ranks),
    url(r'commit',commit_score)
]