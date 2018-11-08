import os, fnmatch, uuid, shutil
from uuid import uuid4

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from app.models import Label,Image,Batch, Comment, STATUS_CHOICES
from app.models import MyUser

img_extension = 'png'

def getbatchlist(filelist):
    def chunks(li, n):
        for i in range(0, len(li), n):
            yield li[i:i + n]
    return list(chunks(filelist, 5))

static_path = settings.STATICFILES_DIRS[0]
raw_path = os.path.join(static_path, 'raw')
dataset_path = os.path.join(static_path, 'dataset')
raw_files = fnmatch.filter(os.listdir(raw_path), '*.{}'.format(img_extension))
for chunk in getbatchlist(raw_files):
    b = Batch()
    b.save()
    for i in chunk:        
        j=unicode(uuid4())+'.{}'.format(img_extension)
        print(("batch: %s,src: %s, dst: %s")%(b,i,j))
        Image(batch=b, src_path=j, raw_path=i).save()
        _dst=os.path.join(dataset_path,j)
        _src=os.path.join(raw_path,i)
        
        shutil.move(src=_src, dst=_dst)

User.objects.all().delete()

User = get_user_model()
User.objects.create_superuser(
    username="admin",
    password="qwer1234",
    email=""
)
user01 = User.objects.create_user(
    username="user01",
    password="01passwd",
    email=""
)
user02 = User.objects.create_user(
    username="user02",
    password="02passwd",
    email=""
)
review01 = User.objects.create_user(
    username="review01",
    password="01passwd",
    email=""
)
MyUser.objects.create(user=user01, isreviewer=False)
MyUser.objects.create(user=user02, isreviewer=False)
MyUser.objects.create(user=review01, isreviewer=True)