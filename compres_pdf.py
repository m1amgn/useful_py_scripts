# Code snippet is using the ConvertAPI Python Client: https://github.com/ConvertAPI/convertapi-python

convertapi.api_secret = 'your-api-secret'
convertapi.convert('compress', {
    'File': '/path/to/my_file.pdf'
}, from_format = 'pdf').save_files('/path/to/dir')
