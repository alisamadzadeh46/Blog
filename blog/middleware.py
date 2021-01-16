from .models import IpAddress


class SaveIpdAddressMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        try:
            ipaddress = IpAddress.objects.get(ipaddress=ip)
        except IpAddress.DoesNotExist:
            ipaddress = IpAddress(ipaddress=ip)
            ipaddress.save()
        request.user.ipaddress = ipaddress

        response = self.get_response(request)

        return response