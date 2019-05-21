from django.urls import reverse
from rest_framework import serializers
from .models import Document


class MaskedThumbnailField(serializers.ReadOnlyField):

    def to_representation(self, value):
        if not value:
            return None
        doc = Document.objects.get(thumbnail=value)
        # replace direct file link with file entry point URL
        base_url = self.context['request']._request.path.rstrip('/') \
            if self.context.get('request') else ''
        url = f'{base_url}/thumbnail/{doc.id}'
        return url

    def to_internal_value(self, data):
        return None


class DocumentSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    uuid = serializers.ReadOnlyField()
    upload_date = serializers.ReadOnlyField()
    thumbnail = MaskedThumbnailField()

    class Meta:
        model = Document
        fields = '__all__'

    def to_representation(self, instance, **kwargs):
        # replace direct file link with file entry point URL
        base_url = self.context['request']._request.path.rstrip('/') \
            if self.context.get('request') else ''
        data = super().to_representation(instance)
        data['file'] = base_url + reverse('document-file', args=(instance.id,)) \
            if data['file'] else None
        return data
