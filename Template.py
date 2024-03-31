from abc import ABC, abstractmethod

class DataMiner(ABC): # Базовый класс шаблонного метода
    @abstractmethod
    def openFile(self, path):
        ...
    @abstractmethod
    def extractData(self, path):
        ...
    @abstractmethod
    def parseData(self, rawData):
        ...

    def analyzeData(self, data):
        print(f'Анализ данных: {data}')
        return 'Итог анализа данных'

    def sendReport(self, analysis):
        print(f'Отправка отчета по данным анализа: {analysis}')
    @abstractmethod
    def closeFile(self, file):
        ...
    def mine(self, path):
        file = self.openFile(path)
        rawData = self.extractData(path)
        data = self.parseData(rawData)
        analysis = self.analyzeData(data)
        self.sendReport(analysis)
        self.closeFile(file)

class PDFDataMiner(DataMiner):
    def openFile(self, path):
        print(f'Открытие PDF-файла по пути {path}')
        return path

    def extractData(self, path):
        print(f'Происходит извлечение данных из файла {path}')
        return 'Строка данных файла'

    def parseData(self, rawData):
        print(f'Происходит парсинг данных')
        return 'Итоговые данные парсинга'

    def closeFile(self, file):
        print(f'Закрытие файла {file}')


pdf = PDFDataMiner()
pdf.mine('ustinov.txt')