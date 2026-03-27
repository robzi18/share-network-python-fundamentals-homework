import math
# Initial Data
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


def f_to_c(f_temp):
    Temp_C = (f_temp - 32) * 5/9
    return round(Temp_C, 2)


f100_in_celsius = f_to_c(100)


def c_to_f(c_temp):
    Temp_F = c_temp * (9/5) + 32
    return round(Temp_F, 2)


c0_in_fahrenheit = c_to_f(0)


def get_force(mass, acceleration):
    return mass * acceleration


train_force = get_force(train_mass, train_acceleration)
print(f"The GE train supplies {train_force} Newtons of force.")


def get_energy(mass, c):
    return mass * c


bomb_energy = get_energy(bomb_mass, c=3*10**8)

print(f"A 1kg bomb supplies {bomb_energy} Joules")
