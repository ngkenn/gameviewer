
# Functions that will be used as template tags
# to render partial parts of the page
from django import template

register = template.Library()

# Function to process call to template tag show game list
@register.inclusion_tag('gameViewer/game_list.html')
def show_game_list(games):
    return { "games": games }