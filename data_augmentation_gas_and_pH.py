import numpy as np
import random

def data_augmentation_gas(lower, upper, amount):
  random_list_gas = []
  for _ in range(0,amount):
    number = np.random.uniform(lower,upper)
    random_list_gas.append(number)
  return random_list_gas
def data_augmentation_pH(lower, upper, amount):
  random_list_pH = []
  for _ in range(0,amount):
    number = np.random.uniform(lower,upper)
    random_list_pH.append(number)
  return random_list_pH

def main():
  pH_augmentation = data_augmentation_pH(2.5,3.8,100)
  gas_augmentation = data_augmentation_gas(6.0, 8.0,100)
  print('List of pH Augmentation\n',pH_augmentation)
  print('Amount = ',len(pH_augmentation))
  print('List of gas Augmentation\n',gas_augmentation)
  print('Amount = ',len(gas_augmentation))

main()