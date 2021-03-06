import simplejson as json

from components.makahiki_base import get_current_round
from components.standings import get_standings_for_user

def get_mobile_standings(user):
  """
  Gets a mobile version of the standings. In the mobile version, we are only using information for the current round.
  """
  current_round = get_current_round()
  
  # Retrieve standings. Note that the get_standings_for_user method returns a JSON string.
  if current_round:
    floor_standings = json.loads(get_standings_for_user(user, "floor", current_round))
    overall_standings = json.loads(get_standings_for_user(user, "all", current_round))
  else:
    # Retrieve the overall standings.
    floor_standings = json.loads(get_standings_for_user(user, "floor", None))
    overall_standings = json.loads(get_standings_for_user(user, "all", None))
  
  # Generate strings for use in the mobile website.
  info = floor_standings["info"]
  index = floor_standings["myindex"]
  rank = info[index]["rank"]
  
  if current_round:
    floor_string = "You are #%d in points for %s for %s." % (rank, user.get_profile().floor, current_round)
  else:
    floor_string = "You are #%d in points for %s in the competition." % (rank, user.get_profile().floor)
  if index > 0:
    diff = info[index - 1]["points"] - info[index]["points"]
    if diff < 2:
      floor_string += " Get 1 more point to move to #%d." % (rank - 1,)
    else:
      floor_string += " Get %d more points to move to #%d." % (diff, rank - 1)
    
  info = overall_standings["info"]
  index = overall_standings["myindex"]
  rank = info[index]["rank"]

  if current_round:
    overall_string = "You are #%d in overall points for %s." % (rank, current_round)
  else:
    overall_string = "You are #%d in overall points in the competition." % rank
  if index > 0:
    diff = info[index - 1]["points"] - info[index]["points"]
    if diff < 2:
      overall_string += " Get 1 more point to move to #%d." % (rank - 1,)
    else:
      overall_string += " Get %d more points to move to #%d." % (diff, rank - 1)
    
  return {"floor": floor_string, "overall": overall_string}
    