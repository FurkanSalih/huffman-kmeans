class Centroid(object):
	"""docstring for Centroid"""
	def __init__(self, pos, sub_items=[]):
		self.pos = pos
		self._sub_items = sub_items

	def add_item(self, item):
		self._sub_items.append(item)

	def remove_item(self, item):
		self._sub_items.remove(item)

	def __str__(self):
		return "Centroid Object: Position: Pos: %s sub_items: %i" % ((self.pos), len(self._sub_items))