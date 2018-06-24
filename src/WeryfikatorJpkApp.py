from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from xml.etree import ElementTree


class WeryfikatorJpk(BoxLayout):
    sumNaliczony = 0
    sumNalezny = 0

    def get_sum(self, files, naliczony_label, nalezny_label):
        ns = {'tns': 'http://jpk.mf.gov.pl/wzor/2017/11/13/1113/',
              'xsi': 'http://www.w3.org/2001/XMLSchema',
              'etd': 'http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/'}

        if not files:
            print('No file is selected')
            return

        try:
            xml = ElementTree.parse(files[0])
            naliczony = float(xml.find('{http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}ZakupCtrl/{'
                                       'http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}PodatekNaliczony').text)
            nalezny = float(xml.find('{http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}SprzedazCtrl/{'
                                     'http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}PodatekNalezny').text)
        except:
            print('File ' + files[0] + ' is not a valid JPK xml file')
            return

        self.__set_labels(self.sumNaliczony + naliczony, self.sumNalezny + nalezny, naliczony_label, nalezny_label)

    def reset_sum(self, naliczony_label, nalezny_label):
        self.__set_labels(0, 0, naliczony_label, nalezny_label)

    def __set_labels(self, naliczony, nalezny, naliczony_label, nalezny_label):
        self.sumNalezny = naliczony
        self.sumNaliczony = nalezny
        naliczony_label.text = 'Podatek naliczony: %.2f' % self.sumNaliczony
        naliczony_label.texture_update()
        nalezny_label.text = 'Podatek nalezny: %.2f' % self.sumNalezny
        nalezny_label.texture_update()


class WeryfikatorJpkApp(App):

    def build(self):
        return WeryfikatorJpk()


if __name__ == '__main__':
    WeryfikatorJpkApp().run()
