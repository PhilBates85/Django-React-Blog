#from django.urls import path 
#from .views import ArticleListView, ArticleDetailView
from articles.api.views import ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ArticleViewSet, base_name='articles')
urlpatterns = router.urls

#urlpatterns = [
#    path('', ArticleListView.as_view()),
#    path('<pk>', ArticleDetailView.as_view()),
#]