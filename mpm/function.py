def handle_upload_file(f):
    print("----------",f.name)
    with open('mpm/static/image/'+f.name,'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)