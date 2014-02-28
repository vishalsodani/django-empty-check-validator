from django.core.exceptions import ValidationError

# Usage example in a custom form
# firstname = forms.CharField(validators = [EmptyCheck()])
class EmptyCheck(object):
    def __call__(self, value):
        if len(value.strip()) == 0:
            raise ValidationError("Value cannot be empty")
