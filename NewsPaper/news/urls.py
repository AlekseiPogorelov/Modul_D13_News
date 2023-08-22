from django.urls import path
from .views import PostList, PostDetail, SearchPostList, PostCreate, PostUpdate, PostDelete, ArticleList, ArticleDetail, \
    ArticleCreate, ArticleUpdate, ArticleDelete, subscriptions
from django.views.decorators.cache import cache_page

urlpatterns = [
   path('', PostList.as_view(), name='post_list'),
   path('search/', cache_page(60)(SearchPostList.as_view())),
   path('<int:pk>', cache_page(60 * 5)(PostDetail.as_view())),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),

   path('article/', ArticleList.as_view(), name='article_list'),
   path('article/<int:pk>', ArticleDetail.as_view(), name='article_detail'),
   path('article/create/', ArticleCreate.as_view(), name='article_create'),
   path('<int:pk>/update/', ArticleUpdate.as_view(), name='article_update'),
   path('<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
   path('subscriptions/', subscriptions, name='subscriptions'),
]