from django.urls import path, include
from article import views
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('viewset', views.ArticleViewSet, basename='article')

router.register('GenericViewSet', views.genercicViewSet, basename='articleGenericViewSet')

router.register('modelViewSet', views.modelViewSet, basename='articleGenericViewSet')


'''if you are adding router.register('', views.genercicViewSet, basename='articleGenericViewSet'), article in url
example router.register('articlee', views.genercicViewSet, basename='articleGenericViewSet')
the name article should be mentioned in last of url 
example: http://127.0.0.1:8000/GenericViewSet/12/articlee/'''


urlpatterns = [
    path('', include(router.urls)),
    path('article/', views.article_list),
    path('articleDetail/<int:pk>/', views.article_detail),
    path('articleList/', views.ArticleList.as_view()),
    path('articleDetail/<int:id>/', views.Articledetail.as_view()),
    path('GenericViewList/',views.GenericApiList.as_view()),
    path('GenericViewDetail/<int:pk>',views.GenericApiDetail.as_view()),
]