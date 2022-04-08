
from conta import Conta

conta1 = Conta(123, "Dudu", 100.0, 1000.0)
conta2 = Conta(321, "Kézia", 200.0, 1000.0)

conta1.extrato()
conta2.extrato()

conta1.transfere(50.0,conta2)

conta1.extrato()
conta2.extrato()

conta3 = Conta(456, "Lupita", 300.0, 1000.0)

conta3.extrato()