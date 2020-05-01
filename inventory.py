#!/usr/bin/python3
# -*- coding: utf-8 -*-
def displayInventory(inventory):
    print('Inventory:')
    item_totel = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_totel += v

    print('Total number of items: %d' %item_totel)


stuff = {'rope': 1, 'arrow': 12, 'gold coin': 42, 'torch': 6, 'dagger': 1}
displayInventory(stuff)

