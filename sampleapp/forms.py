from  django import forms


class UploadForm(forms.Form):
    uploadFile = forms.FileField()
