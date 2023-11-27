from django.urls import path
from .views import *

urlpatterns = [
    path('get/<int:id>', get_note, name='get_note'),
    path('post-note', post_note, name='post-note'),
    path('put/<int:id>', put_note, name='put_note'),
    path('patch/<int:id>', patch_note, name='patch_note'),
    path('del/<int:id>', delete_note, name='delete_note'),
    path('summarize/<int:notes_id>', SummarizeTextView.as_view(), name='summarize_text'),
]
