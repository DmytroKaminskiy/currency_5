from rest_framework import serializers

from currency.models import Rate, Source, ContactUs


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = (
            'id',
            'name',
            'code_name',
            'logo',
        )


class RateSerializer(serializers.ModelSerializer):
    source_obj = SourceSerializer(source='source', read_only=True)

    # read_only=True, write_only=False

    class Meta:
        model = Rate
        fields = (
            'id',
            'buy',
            'sale',
            'type',
            'source_obj',  # GET
            'source',  # POST
            'created',
        )
        extra_kwargs = {
            'source': {'write_only': True},
        }



class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = (
            'id',
            'email_to',
            'subject',
            'body',
        )
