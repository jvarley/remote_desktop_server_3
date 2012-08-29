from django.http import HttpResponse
from django.utils.html import escape
from controller_factory import ControllerFactory

controllerFactory = ControllerFactory()

mouseController = controllerFactory.get_mouse_controller()
volumeController = controllerFactory.get_volume_controller()
vlcController = controllerFactory.get_vlc_controller()


def hello_html(request):
    "This view is a basic 'hello world' example in HTML."
    return HttpResponse('<h1>Hello, world.</h1>')

def hello_text(request):
    "This view is a basic 'hello world' example in plain text."
    return HttpResponse('Hello, world.', mimetype='text/plain')

def hello_write(request):
    "This view demonstrates how an HttpResponse object has a write() method."
    r = HttpResponse()
    r.write("<p>Here's a paragraph.</p>")
    r.write("<p>Here's another paragraph.</p>")
    return r

def metadata(request):
    "This view demonstrates how to retrieve request metadata, such as HTTP headers."
    r = HttpResponse('<h1>All about you</h1>')
    r.write("<p>Here's all known metadata about your request, according to <code>request.META</code>:</p>")
    r.write('<table>')
    meta_items = request.META.items()
    meta_items.sort()
    for k, v in meta_items:
        r.write('<tr><th>%s</th><td>%r</td></tr>' % (k, v))
    r.write('</table>')
    return r

def get_data(request):
    "This view demonstrates how to retrieve GET data."
    r = HttpResponse()
    if request.GET:
        r.write('<p>GET data found! Here it is:</p>')
        r.write('<ul>%s</ul>' % ''.join(['<li><strong>%s:</strong> %r</li>' % (escape(k), escape(v)) for k, v in request.GET.items()]))
    r.write('<form action="" method="get">')
    r.write('<p>First name: <input type="text" name="first_name"></p>')
    r.write('<p>Last name: <input type="text" name="last_name"></p>')
    r.write('<p><input type="submit" value="Submit"></p>')
    r.write('</form>')
    return r

def post_data(request):
    "This view demonstrates how to retrieve POST data."
    r = HttpResponse()
    if request.POST:
        r.write('<p>POST data found! Here it is:</p>')
        r.write('<ul>%s</ul>' % ''.join(['<li><strong>%s:</strong> %r</li>' % (escape(k), escape(v)) for k, v in request.POST.items()]))
    r.write('<form action="" method="post">')
    r.write('<p>First name: <input type="text" name="first_name"></p>')
    r.write('<p>Last name: <input type="text" name="last_name"></p>')
    r.write('<p><input type="submit" value="Submit"></p>')
    r.write('</form>')
    return r

def volume_action(request):
    "This view demonstrates how to retrieve POST data."
    r = HttpResponse()
    if request.POST:
        
        new_volume = int(float(request.POST.items()[0][1]))
        volumeController.set_volume(new_volume)
        current_volume=volumeController.get_volume()
        r.write('<p>Adjust the volume, currently: %r</p>'%current_volume)
    r.write('<form action="" method="post">')
    r.write('<p>New Volume: <input type="text" name="new_volume"></p>')
    r.write('<p><input type="submit" value="Submit"></p>')
    r.write('</form>')
    return r

def vlc_player_action(request):
    #vlcController.launch_player()
    mouse_position = mouseController.get_mouse_position()
    "This view is a basic 'hello world' example in HTML."
    mouseController.set_mouse_position(432,114)
    return HttpResponse('<h1>Hello,' + str(mouse_position) + ' world.</h1>')

def mouse_move_action(request):
    r = HttpResponse()
    if request.POST:
        dx = int(float(request.POST.items()[0][1]))
        dy = int(float(request.POST.items()[1][1]))
        
        current_mouse_position = mouseController.get_mouse_position()
        
        new_x = current_mouse_position[0] + dx
        new_y = current_mouse_position[1] + dy
        
        mouseController.set_mouse_position(new_x,new_y)

    mouse_position = mouseController.get_mouse_position()
    r.write('<p>Current Mouse Position:  ' + str(mouse_position) + '</p>')
    r.write('<form action="" method="post">')
    r.write('<p>New dx: <input type="text" name="new_dx"></p>')
    r.write('<p>New dy: <input type="text" name="new_dy"></p>')
    r.write('<p><input type="submit" value="Submit"></p>')
    r.write('</form>')
    return r


def mouse_click_action(request):
    r = HttpResponse()
    if request.POST:

        x,y = mouseController.get_mouse_position()

        left_click = request.POST.items()[0][1]
        right_click = request.POST.items()[1][1]

        if left_click == "true":
            mouseController.click_at_location(x,y,1)

        #if right_click == "true":
        mouseController.click_at_location(x,y,3)

        

    r.write('<p>Mouse Click:</p>')
    r.write('<form action="" method="post">')
    r.write('<p>left_click: <input type="text" name="left_click"></p>')
    r.write('<p>right_click: <input type="text" name="right_click"></p>')
    r.write('<p><input type="submit" value="Submit"></p>')
    r.write('</form>')
    return r


