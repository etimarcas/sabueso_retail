from django.urls import include,path
from .views import ItemCreate,ItemList,ItemDetail,ItemUpdate,ItemDelete

urlpatterns = [

    path('item/create', ItemCreate.as_view(), name='item-create'),  
    path('item/',ItemList.as_view()),
    path('item/<int:pk>/', ItemDetail.as_view, name='item-detail'), 
    path('item/update',ItemUpdate.as_view(),name='item-update'),
    path('item/delete',ItemDelete.as_view(),name='item-delete')
]