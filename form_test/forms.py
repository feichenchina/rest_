from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        cc_myself = cleaned_data.get("cc_myself")
        subject = cleaned_data.get("subject")

        if cc_myself and subject:
            # Only do something if both fields are valid so far.
            if "hello" not in subject:
                raise forms.ValidationError(
                    "Did not send for 'hello' in the subject despite "
                    "CC'ing yourself."
                )
            return cleaned_data