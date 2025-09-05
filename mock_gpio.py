class MockGPIO:
    BCM = "BCM"
    OUT = "OUT"
    HIGH = 1
    LOW = 0

    def setmode(self, mode): print(f"GPIO setmode({mode})")
    def setup(self, pin, mode): print(f"GPIO setup({pin}, {mode})")
    def output(self, pin, state): print(f"GPIO output({pin}, {state})")
    def cleanup(self): print("GPIO cleanup")

GPIO = MockGPIO()