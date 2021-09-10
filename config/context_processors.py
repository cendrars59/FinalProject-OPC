# see documentation here
# http://www.formation-django.fr/framework-django/zoom-sur/context-processor.html
from club.models import Season
from users.models import InvolvedAsICategoryForSeason


def sidebar(request):
    if request.user.is_authenticated:
        active_season = Season.get_active_season()
        user_items = InvolvedAsICategoryForSeason.objects.filter(
            season=active_season).filter(member=request.user).exclude(is_player=True).only("category")
        user = request.user
        return {'active_season': active_season,
                'user_items': user_items,
                'user': user
                }
    else:
        return {'active_season': '',
                'user_categories': []
                }
