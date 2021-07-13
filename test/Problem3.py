class ReadLog():
    def log(self):
        f1= open("resultLog.txt","w+")
        parse = ["ERROR","WARN"]
        with open( r"C:\Users\nineleaps\PycharmProjects\Meddiff\test\sample.log") as f:
          for line in f:
              for phrase in parse:
                if phrase in line:
                    f1.write(line)


read = ReadLog()
read.log()