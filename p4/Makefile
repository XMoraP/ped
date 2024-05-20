file = $@

cli:
	@python3 cli4.py $(file)

serv: 
	@python3 serv4.py 
%:
	@echo "La regla '$@' no está definida en el Makefile."
	@false

clean:
	@echo "Limpiando..."
	rm cliserv2.py.swp
