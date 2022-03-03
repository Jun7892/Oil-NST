from django.apps import AppConfig
import boto3
import tensorflow_hub as hub

class NstappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'nstapp'
    hub_module = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
    # secret 으로 빼놓고 해당 파일은 .gitignore를 해도 좋지만, github 레포를 그냥 private 으로 설정하는 것을 추천 (배포 과정이 더 간단해짐)
    s3 = boto3.client('s3', aws_access_key_id='',
                      aws_secret_access_key='', region_name='ap-northeast-2')