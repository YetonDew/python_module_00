import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'ex1'))
from ft_garden_data import Plant as BasePlant

class Plant(BasePlant):
	def grow(self, days: int):
		self.height += days

	def age_up(self, days: int):
		self.age += days

	def get_info(self):
		self.blueprinter()

def main():
    p = Plant("Rose", 25, 30)
    p.grow(5)
    p.age_up(5)
    p.get_info()


if __name__ == "__main__":
    main()
