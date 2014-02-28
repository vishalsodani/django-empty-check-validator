from django.core.exceptions import ValidationError

class EmptyCheck(object):
    def __call__(self, value):
        if len(value.strip()) == 0:
            raise ValidationError("Value cannot be empty")
