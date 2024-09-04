from conta import Conta

conta1 = Conta(123, "Arthur", 3.15, -1100)

conta1.depositar(1200)
conta1.sacar(70)
conta1.pagar(1100)
conta1.extrato()