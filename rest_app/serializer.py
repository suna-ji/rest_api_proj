from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        # fields = ('id', 'title', 'body')
        write_only_fields = ('title',)
        
#post모델을 클라이언트에게 json형식으로  