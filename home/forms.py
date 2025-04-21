from django import forms

from home.models.address import Address

class AddressForm(forms.BaseModelForm):
    class Meta:
        model = Address
        exclude = []

    def is_valid(self):
        is_valid = super().is_valid()
        if not is_valid:
            return False

        if self.cleaned_data["postal_code"] == "123456":
            self.add_error("postal_code", "Postal code cannot be 123456")
            return False

        return True