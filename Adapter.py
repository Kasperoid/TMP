class Target:
    def request(self):
        return "Target: The default target's behavior."

class Adaptee:
    def specific_request(self):
        return ".eetpadA eht fo roivaheb laicepS"

class Adapter(Target, Adaptee):
    def request(self):
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"

def client_code(target: "Target") -> None:
    print(target.request(), end="")

adaptee = Adaptee()
print("Adaptee: " + adaptee.specific_request())
adapter = Adapter()
client_code(adapter)