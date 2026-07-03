class LogAnalyzer:

    def __init__(self, filename):
        self.filename = filename
        self.error = 0
        self.warning = 0
        self.info = 0

    def read_log(self):
        try:
            file = open(self.filename, "r")

            for line in file:
                line = line.upper()

                if "ERROR" in line:
                    self.error += 1
                elif "WARNING" in line:
                    self.warning += 1
                elif "INFO" in line:
                    self.info += 1

            file.close()

        except FileNotFoundError:
            print("Log file not found!")

    def display(self):
        print("\n----- LOG ANALYSIS REPORT -----")
        print("Errors   :", self.error)
        print("Warnings :", self.warning)
        print("Info     :", self.info)



analyzer = LogAnalyzer("log.txt")


analyzer.read_log()

analyzer.display()