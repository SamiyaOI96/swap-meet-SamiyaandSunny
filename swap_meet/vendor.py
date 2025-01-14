from swap_meet.item import Item

class Vendor:
    def __init__(self,inventory = None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory 

    def add(self,item):
        self.item = item
        self.inventory.append(item)
        return self.item
    
    def remove(self,item):
        self.item = item
        if item not in self.inventory:
            return False
        elif item in self.inventory: 
            self.inventory.remove(item)
        return self.item

    def get_by_category(self,category=""):
        item_list=[]
        for item in self.inventory:
            if item.category == category:
                item_list.append(item)
        return item_list
    
    def swap_items(self, vendor, my_item, their_item):

        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False

        self.remove(my_item) 
        vendor.add(my_item) 
        vendor.remove(their_item)
        self.add(their_item)
        return True

    def swap_first_item(self, vendor):
        if len(self.inventory) == 0:  
            return False
        if len(vendor.inventory) == 0: 
            return False
            
        self.vendor = vendor
        my_first_item = self.inventory[0] 
        friend_first_item = vendor.inventory[0]
        result = self.swap_items(vendor, my_first_item, friend_first_item)
        return result
    
    def get_best_by_category(self, category):
        highest_condition = 0
        best_item = None

        for item in self.inventory:
            if item.category == category:
                if item.condition > highest_condition:
                    highest_condition = item.condition
                    best_item = item
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        if not self.inventory or not other.inventory:
            return False
        #^ the condition is explicit and is deemed to be defensive 
        

        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)
        result = self.swap_items(other, my_best_item, their_best_item)
        return result

    


        



            





    
        
        




