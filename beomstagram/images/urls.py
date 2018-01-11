from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.Feed.as_view(),
        name='feed',
    ),
    url(
        regex=r'(?P<image_id>\w+)/like/',
        view=views.LikeImage.as_view(),
        name='like_image',
    )
]


# /image/3/like
# /image/3/unlike

# 0 create the url and the view
# 1 take the id from the url
# 2 we want to find an image with thid id
# 3 we want to create a like for that image