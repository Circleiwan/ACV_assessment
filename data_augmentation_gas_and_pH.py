import numpy as np
import random
import csv

def data_augmentation(lower, upper, amount):
  random_list = []
  for _ in range(0,amount):
    number = np.random.uniform(lower,upper)
    random_list.append(round(number, 2))
  return random_list
'''
def data_augmentation_pH(lower, upper, amount):
  random_list_pH = []
  for _ in range(0,amount):
    number = np.random.uniform(lower,upper)
    random_list_pH.append(round(number, 2))
  return random_list_pH
'''
def generate_csv_file(filename, list_data1, list_data2, name1, name2):
  with open(filename + '.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(['index',name1,name2])
    for index, data in enumerate(list(zip(list_data1, list_data2))):
      writer.writerow([index, data[0], data[1]])

def main():
  pH_augmentation = data_augmentation(2.5,3.8,100)
  pH_augmentation.sort(reverse=True)
  gas_augmentation = data_augmentation(6.0, 8.0,100)
  gas_augmentation.sort(reverse=True)
  print('List of pH Augmentation\n',pH_augmentation)
  print('Amount = ',len(pH_augmentation))
  print('List of gas Augmentation\n',gas_augmentation)
  print('Amount = ',len(gas_augmentation))
  try:
    return generate_csv_file('data_csv', pH_augmentation, gas_augmentation, 'pH', 'Gas')
  except TypeError:
    return "Something went wrong!"
main()