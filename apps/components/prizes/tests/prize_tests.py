import os

from django.test import TestCase
from django.conf import settings
from django.core.files.images import ImageFile
from django.db import IntegrityError

from components.prizes.models import Prize

class PrizeTest(TestCase):
  """
  Tests basic methods of a prize.
  """
  def testConstraints(self):
    """
    Tests that the uniqueness constraints are enforced.
    A prize with the same round_name, award_to, and award_criteria as another cannot be created.
    """
    image_path = os.path.join(settings.PROJECT_ROOT, "fixtures", "test_images", "test.jpg")
    image = ImageFile(open(image_path, "r"))
    prize = Prize(
        title="Super prize!",
        description="A test prize",
        image=image,
        award_to="individual_overall",
        award_criteria="points",
        round_name="Round 1"
    )
    prize.save()
    
    prize2 = Prize(
        title="Dup prize!",
        description="A duplicate test prize",
        image=image,
        award_to="individual_overall",
        award_criteria="points",
        round_name="Round 1"
    )
    try:
      prize2.save()
      self.fail("IntegrityError exception not thrown.")
    except IntegrityError:
      pass
      
    prize2.round_name = "Overall"
    try:
      prize2.save()
    except IntegrityError:
      self.fail("IntegrityError exception should not be thrown.")
      
    prize2.round_name = "Round 1"
    prize2.award_criteria = "energy"
    try:
      prize2.save()
    except IntegrityError:
      self.fail("IntegrityError exception should not be thrown.")
      
    prize2.award_criteria = "points"
    prize2.award_to = "floor_overall"
    try:
      prize2.save()
    except IntegrityError:
      self.fail("IntegrityError exception should not be thrown.")
      
    # Make sure to clean up!
    prize.delete()
    prize2.delete()