def is_planet_mnemonic_correct(solar_system, mnemonic):
    no_asteroid = []
    for i in solar_system:
        if i != "Asteroid":
            no_asteroid.append(i)
    
    planet_letters = []
    for i in no_asteroid:
        planet_letters.append(i[0])
    
    mnemonic_split = mnemonic.split()
    mnemonic_letters = []
    for i in mnemonic_split:
        mnemonic_letters.append(i[0])

    if planet_letters == mnemonic_letters:
        return True
    return False