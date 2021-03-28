class App:
    dItems = {}

    def print(self):
        print('Terraform items:')
        for i in self.dItems:
            print(i)
            print('References:')
            for j in self.dItems[i].dRefItemIds:
                print('  ' + j)


