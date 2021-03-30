from Item import Item


class App:
    dItems = {}

    def print(self):
        print('Terraform items:')
        for i in self.dItems:

            item: Item = self.dItems[i]
            print(i + ';' + str(item.cidr) + ';' + str(item.vcn))
            if len(item.dRefItemIds)>0:
                print('References:')
            for j in item.dRefItemIds:
                print('  ' + j)

    def calculate(self):
        for i in self.dItems:
            item: Item = self.dItems[i]
            for j in item.dRefItemIds:
                refItem: Item = self.dItems.get(j)
                if refItem:
                    if refItem.type == 'oci_core_vcn':
                        item.vcn = j
            if item.vcn:
                item.dRefItemIds.pop(item.vcn)


