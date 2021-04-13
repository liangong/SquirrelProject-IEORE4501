from django.forms import ModelForm
from sightings.models import SquirrelData


class AddSightingForm(ModelForm):
    class Meta:
        model = SquirrelData
        fields = {
            "unique_squirrel_id",
            "latitude",
            "longitude",
            "shift",
            "date",
            "age",
            "primary_fur_color",
            "location",
            "specific_location",
            "running",
            "chasing",
            "climbing",
            "eating",
            "foraging",
            "other_activities",
            "kuks",
            "quaas",
            "moans",
            "tail_flags",
            "tail_twitches",
            "approaches",
            "indifferent",
            "runs_from",
        }
