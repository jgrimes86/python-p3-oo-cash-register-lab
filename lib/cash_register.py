#!/usr/bin/env python3

class CashRegister:
  
  # total = 0
  # items = []
  last_item_value = 0

  def __init__(self, discount=0, total=0):
    self.discount = discount
    self.total = total
    self.items = []

  def add_item(self, new_item, price, quantity=1):
    self.total = self.total + (price * quantity)
    for i in range(quantity):
      self.items.append(new_item)
    self.last_item_value = price * quantity

  def apply_discount(self):
    if self.discount > 0:
      self.total = self.total - (self.total * (self.discount / 100 ))
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    self.total = self.total - self.last_item_value
    

# CashRegister.add_items()