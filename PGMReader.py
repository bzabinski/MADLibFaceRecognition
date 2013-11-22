
class PGMReader:

    def openFile(self, filePath):
        self._f = open(filePath, 'rb') #assumes P5 format
        for i in range(0, 3): #skips formatting text
            self._f.readline()

    def readByte(self):
        _oneByte = self._f.read(1)
        return ord(_oneByte)

    def closeFile(self):
        self._f.close()
