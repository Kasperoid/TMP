from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

class ConsoleLogger(Logger):
    def log(self, message):
        print(f"Console Log: {message}")

class FileLogger(Logger):
    def log(self, message):
        print(f"File Log: {message}")

class LoggerFactory(ABC):
    @abstractmethod
    def create_logger(self):
        pass

class ConsoleLoggerFactory(LoggerFactory):
    def create_logger(self):
        return ConsoleLogger()

class FileLoggerFactory(LoggerFactory):
    def create_logger(self):
        return FileLogger()

console_factory = ConsoleLoggerFactory()
file_factory = FileLoggerFactory()

console_logger = console_factory.create_logger()
file_logger = file_factory.create_logger()

console_logger.log("This is a console log.")
file_logger.log("This is a file log.")