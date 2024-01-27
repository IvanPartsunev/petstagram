from django.core.exceptions import ValidationError

FILE_MAX_SIZE = 5 * 1024 * 1024


def validate_file_size(image_object):
    if image_object.size > FILE_MAX_SIZE:
        raise ValidationError("The maximum file size that can be uploaded is 5 MB")
