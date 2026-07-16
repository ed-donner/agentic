import time
import modal
from datetime import datetime

Pricer = modal.Cls.lookup("pricer-service-agentic", "Pricer")
pricer = Pricer()
while True:
    reply = pricer.price.remote("Keep the model warm.")
    print(f"{datetime.now()}: {reply}")
    time.sleep(30)
