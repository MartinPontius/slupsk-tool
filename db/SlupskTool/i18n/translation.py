from django.utils.translation import get_language_from_request
from .dictionary import Dictionary

# Different ways to get language preferences
# a) django.utils.translation.get_language()
# b) django.utils.translation.get_language_from_request(request) returns the browser-preferred language and falls back to english if the preferred language is not available
# c) request.LANGUAGE_CODE (needs django.middleware.locale.LocaleMiddleware)
#    1) language prefix in the requested URL
#    2) cookie (django_language)
#    3) Accept-Language HTTP header
#    4) global LANGUAGE_CODE setting
#    Note: language preference is expected to be in the default language format (e.g. pl or en, not polish or english)

# Get additional info on language
# get_language_info()

def translate(request):

    #language = request.COOKIES.get('django_language')
    return Dictionary().get_dict(request.LANGUAGE_CODE)
