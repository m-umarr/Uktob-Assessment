from django.urls import path
from .views import *

urlpatterns = [
    path('get/<int:note_id>', get_note, name='get_note'),
    path('post-note', post_note, name='post-note'),
    path('put/<int:note_id>', put_note, name='put_note'),
    path('patch/<int:note_id>', patch_note, name='patch_note'),
    path('del/<int:note_id>', delete_note, name='delete_note'),
]
