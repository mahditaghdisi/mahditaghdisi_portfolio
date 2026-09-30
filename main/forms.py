from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    # honeypot: a field real visitors never see or fill in (hidden via CSS),
    # but simple bots that auto-fill every input on the page will fill it in —
    # so if it's non-empty, we silently treat the submission as spam.
    website = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "class": "field-honeypot", "tabindex": "-1", "autocomplete": "off",
    }))

    class Meta:
        model = ContactMessage
        fields = ["name", "phone", "description"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "field-input", "required": True, "autocomplete": "name",
            }),
            "phone": forms.TextInput(attrs={
                "class": "field-input", "required": True, "autocomplete": "tel",
            }),
            "description": forms.Textarea(attrs={
                "class": "field-input field-textarea", "rows": 4,
            }),
        }

    def clean_website(self):
        # if the honeypot got filled in, reject the submission as spam
        value = self.cleaned_data.get("website")
        if value:
            raise forms.ValidationError("spam detected")
        return value

    def __init__(self, *args, lang="fa", **kwargs):
        super().__init__(*args, **kwargs)
        labels = {
            "fa": {"name": "نام", "phone": "شماره تماس", "description": "توضیحات پروژه (اختیاری)"},
            "en": {"name": "Name", "phone": "Phone", "description": "Project description (optional)"},
        }[lang]
        for field_name, label in labels.items():
            self.fields[field_name].label = label
        self.fields["description"].required = False
