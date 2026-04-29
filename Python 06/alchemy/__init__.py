from .elements import create_air
from .potions import healing_potion as hp, strength_potion
from .transmutation import lead_to_gold

heal = hp

__all__: list[str] = ['create_air', 'heal', 'strength_potion',
                      'lead_to_gold']
