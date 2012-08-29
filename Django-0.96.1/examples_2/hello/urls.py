from django.conf.urls.defaults import *

urlpatterns = patterns('examples.hello.views',
    (r'^html/$', 'hello_html'),
    (r'^text/$', 'hello_text'),
    (r'^write/$', 'hello_write'),
    (r'^metadata/$', 'metadata'),
    (r'^getdata/$', 'get_data'),
    (r'^postdata/$', 'post_data'),
    (r'^volume_control/$', 'volume_action'),
    (r'^vlc_player_control/$', 'vlc_player_action'),
    (r'^mouse_control/$', 'mouse_move_action'),
    (r'^mouse_click/$', 'mouse_click_action'),

)
