import random
import string
from django.db import models
from django.contrib.auth.models import AbstractUser


def generate_friend_id():
    """
    Generates a random 5 character ID
    """
    # TODO: Find fix for possibly generating the same ID again, despite the low chances
    characters = string.ascii_uppercase + string.digits
    return "".join(random.choice(characters) for _ in range(5))


class User(AbstractUser):
    # Generate unique friend ID for each user
    friend_id = models.CharField(
        max_length=5, default=generate_friend_id, unique=True, editable=False
    )

    def __str__(self):
        return "{} ({})".format(self.username, self.friend_id)
