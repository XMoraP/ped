login = $@
signup = $@

cli:
	@python3 app/cli7.py $(login) $(signup)

serv: 
	@python3 app/serv7.py 

testt:
	@python3 -m unittest -v test/test_servidor.py

%:
	@echo "La regla '$@' no está definida en el Makefile."
	@false

clean:
	@echo "Limpiando..."
	rm -r cliserv2.py.swp
	rm -r k*

