from battlefield import Battlefield

battlefield = Battlefield()

battlefield.display_welcome()

battlefield.run_game()

while len(battlefield.herd.units_available) > 0 and len(battlefield.fleet.units_available) > 0:
    battlefield.battle_phase()

battlefield.display_winner()