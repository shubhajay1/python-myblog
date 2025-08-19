from django.http import JsonResponse


def emicalculation(request):
    data = {}
    try:
        principal = float(request.POST.get('loanAmount', 0))
        interest_rate = float(request.POST.get('interest_rate', 0))
        tenure = int(request.POST.get('tenure', 0))

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

        print(emi)
        data['resultData'] = emi
        data['success'] = True

    except (ValueError, TypeError) as e:
        data['resultData'] = str(e)
        data['success'] = False

    return JsonResponse(data)
