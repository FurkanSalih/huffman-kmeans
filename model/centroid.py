class Centroid(object):

    """docstring for Centroid"""

    def __init__(self, pos):
        self.pos = pos
        self._sub_items = []
        self.pos_changed = True

    def add_item(self, item):
        self._sub_items.append(item)

    def remove_item(self, item):
        self._sub_items.remove(item)

    def calculate_new_pos(self):
        if len(self._sub_items) != 0:
            pos = [0, 0, 0]
            for item in self._sub_items:
                pos[0] += item[0]
                pos[1] += item[1]
                pos[2] += item[2]

            div = len(self._sub_items)
            pos[0] /= div
            pos[1] /= div
            pos[2] /= div

            self.pos_changed = self.pos != pos
            self.pos = pos
            self._sub_items = []
        else:
            self.pos_changed = False

    def __str__(self):
        return "Centroid Object: Position: \
        Pos: %s \
        sub_items: %i \
        pos_changed: %s" % ((self.pos), len(self._sub_items), self.pos_changed)
