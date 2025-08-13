from django.http import JsonResponse


def emicalculation(request):
    data = {}
    try:
        LoanAmount = float(request.POST.get('loanAmount', 0))
        downPayment = float(request.POST.get('downPayment', 0))
        interest_rate = float(request.POST.get('interest_rate', 0))
        tenure = int(request.POST.get('tenure', 0))

        principal = LoanAmount - downPayment
        monthly_rate = interest_rate / 12 / 100
        months = tenure * 12

        if months <= 0 or principal <= 0:
            raise ValueError("Invalid principal or tenure")

        # EMI calculation
        if monthly_rate == 0:
            emi = principal / months
        else:
            emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / \
                ((1 + monthly_rate) ** months - 1)

        emi = round(emi, 2)
        data['resultData'] = emi
        data['success'] = True

    except (ValueError, TypeError):
        data['resultData'] = 'Some thing went Wrong'
        data['success'] = False

    return JsonResponse(data)
