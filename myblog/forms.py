from django import forms


class usersFormsModel(forms.Form):

    # num1 = forms.CharField(label="value 1", required=False)
    num1 = forms.CharField(label="First name")
    num2 = forms.CharField(label="Last Name", widget=forms.TextInput(
        attrs={'class': "custom-form-control"}))
    num3 = forms.CharField(label="Message", required=False, widget=forms.Textarea(
        attrs={'class': "custom-form-control", 'cols': 5, 'rows': 2}))
    email = forms.EmailField()


class emiCalculater(forms.Form):

    totallPrice = forms.IntegerField(
        label="Total Price", widget=forms.NumberInput(attrs={'value': '0'}))
    loanAmount = forms.IntegerField(
        label="Loan Amount", widget=forms.NumberInput(attrs={'value': '0', 'readonly': 'readonly'}))
    downPayment = forms.IntegerField(label="Down Payment", min_value=0, max_value=10000000, widget=forms.NumberInput(
        attrs={'type': 'range', 'step': '10000', 'value': '0', 'class': 'slider', 'id': 'downpaymentRange'}))
    interest_rate = forms.FloatField(label="Rate of interest (p.a)", min_value=0, max_value=20, widget=forms.NumberInput(
        attrs={'type': 'range', 'step': '0.1', 'value': '9.1', 'class': 'slider', 'id': 'interestRange'}))
    TENURE_CHOICES = [(i, f"{i} Year{'s' if i > 1 else ''}")
                      for i in range(1, 11)]
    # [(1, '1 Year'), (2, '2 Years'), ... (10, '10 Years')]

    tenure = forms.ChoiceField(
        label="Loan Tenure",
        choices=TENURE_CHOICES,
        initial=5,  # default selection
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'tenureDropdown'
        })
    )
