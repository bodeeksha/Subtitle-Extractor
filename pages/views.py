import boto3
import json
from django.shortcuts import render
from video_subtitle.config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY


def index(request):
    return render(request, 'form.html')


def subtitleView(request, *args, **kwargs):

    try:
        dynamo_client = boto3.resource(service_name='dynamodb', region_name='ap-south-1',
                                       aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

        table = dynamo_client.Table('subs')
        data = table.get_item(Key={'test-key-1': str(kwargs['id'])})
        data = json.loads(data['Item']['srt'])

        context = {'subtitles': data}

    except:
        context = {}

    if request.method == 'POST':
        context.clear()
        context['subtitles'] = []
        query = request.POST['search']

        for subtitle in data:
            if query.lower() in subtitle['content'].lower():
                context['subtitles'].append(subtitle)

    return render(request, 'subtitles.html', context)


def progressView(request, *args, **kwargs):
    context = {
        'task_id': kwargs['task_id'],
        'id': kwargs['id'],
    }
    return render(request, 'progress.html', context)
