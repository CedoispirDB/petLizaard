import time
import datetime

def send_message():
    from urllib.parse import urlencode
    from urllib.request import Request, urlopen
    import base64

    # local image from drive
    seconds = (time.ctime(time.time()))
    seconds = seconds[10:16]

    # file = 'logo.jpg'
    # image = open(file, 'rb')
    # image_read = image.read()
    # image1 = base64.encodebytes(image_read)

    # # remote image from url
    # image2 = base64.b64encode(urlopen("https://www.google.de/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png").read())

    url = 'https://www.pushsafer.com/api'
    post_fields = {
        "t" : 'Timer',
        "m" : 'Feed the goodest boi',
        "s" : 11,
        "v" : 3,
        "i" : 33,
        "c" : '#FF0000',
        "d" : 'a',
        "u" : 'https://www.pushsafer.com',
        "ut" : 'Open Pushsafer',
        "k" : '678HaeS07xeoZEmdscDf',
        # "p" : 'data:image/jpeg;base64,'+str(image1.decode('ascii')),
        # "p2" : 'data:image/png;base64,'+str(image2.decode('ascii')),
        }
    
    if seconds == '9:00':
        post_fields["m"] = '10+ small crickets, 2x collard greens, 1x bell pepper slice and 1x strawberry'
    elif seconds == '12:00':
        post_fields["m"] = '10+ dubia roaches, 2x kale, 1 slice squash, 1x blueberry'
    elif seconds == '15:00':
        post_fields["m"] = '10+ small crickets, 2x dandelion greens, 1 slice pumpkin, 1 slice banana'
    elif seconds == '18:00':
        post_fields["m"] = '10+ dubia roaches, 2x collard greens, 1 bell pepper slice, 1x grape'
    elif seconds == '03:00':
        post_fields["m"] = '10+ dubia roaches, 2x collard greens, 1 bell pepper slice, 1x grape'
    
    
    request = Request(url, urlencode(post_fields).encode())
    json = urlopen(request).read().decode()
    print(json)


def main():
    seconds = time.ctime(time.time())[11:16]
    #send_message()
    #print(send_message())
    if seconds == '9:00':
        send_message()
    elif seconds == '12:00':
       send_message()
    elif seconds == '15:00':
        send_message()
    elif seconds == '18:00':
        send_message()
    elif seconds == '03:00':
        print('worked')
        send_message()

    



if __name__ == '__main__':
    main()




    