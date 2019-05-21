from django.urls import re_path

from documents.views import DocumentViewSet, document_download_view, document_thumbnail_view
from .routers import OptionalSlashRouter

router = OptionalSlashRouter()
router.register(r'documents', DocumentViewSet)

urlpatterns = [
    re_path(r'^file/(?P<id>\w+)/$', document_download_view, name='document-file'),
    re_path(r'^thumbnail/(?P<id>\w+)/$', document_thumbnail_view),
]

urlpatterns += router.urls
