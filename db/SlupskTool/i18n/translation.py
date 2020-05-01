from django.utils.translation import get_language_from_request
from .dictionary import Dictionary

# Different ways to get language preferences
# django.utils.translation.get_language()
# django.utils.translation.get_language_from_request(request)
# request.LANGUAGE_CODE (needs django.middleware.locale.LocaleMiddleware)

# Get additional info on language
# get_language_info()


# get_language_from_request() returns the browser-preferred language and falls back to english if the preferred language is not available
def translate(request):
    return Dictionary(get_language_from_request(request)).get_dict()
