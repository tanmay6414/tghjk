from django.http import HttpResponse
from django.templatetags.static import static
from django.shortcuts import render
from boto3.s3.transfer import S3Transfer
import boto3


def index(request):
    return render(request, 'filedata/a.html')

def abc(request):

    if request.method == "GET":
        bname=request.GET['bname']
        
        file1=request.GET['file1']
        file2='/home/tanmay/Downloads/'+file1
        
        flist = []
        flist.append(bname)
        
        flist.append(file1)


       
        client = boto3.client('s3', aws_access_key_id='AKIAY6R3ASPPH2UHQZUS',aws_secret_access_key='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')
        transfer = S3Transfer(client)
        transfer.upload_file(file2 ,bname,file1)

        return render(request, 'filedata/abcd.html', {"flist": flist})
        