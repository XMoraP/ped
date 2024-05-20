
SRC=hw
EXE=$(SRC)


do: console

all: console postscript troff clean

console: awk bc c c++ factor forth haskell java javascript lisp lua perl python ruby rust scheme sh \
	 clean


awk: $(SRC).awk
	@echo "Hello world en $@..."
	awk -f $<

bc: $(SRC).bc
	@echo "Hello world en $@..."
	bc -q $<

c: $(SRC).c
	@echo "Hello world en $@..."
	gcc -o $(EXE) $< && ./$(EXE)

c++: $(SRC).cpp
	@echo "Hello world en $@..."
	g++ -o $(EXE) $< && ./$(EXE)

factor: $(SRC).factor
	@echo "Hello world en $@..."
	factor-lang $<

forth: $(SRC).forth
	@echo "Hello world en $@..."
	gforth $<

haskell: $(SRC).hs
	@echo "Hello world en $@..."
	runhaskell $<

java: $(SRC).java
	@echo "Hello world en $@..."
	javac $< && java HelloWorld

javascript: $(SRC).js
	@echo "Hello world en $@..."
	rhino $<
	node $<

lisp: $(SRC).lisp
	@echo "Hello world en $@..."
	clisp $<

lua: $(SRC).lua
	@echo "Hello world en $@..."
	lua $<

perl: $(SRC).pl
	@echo "Hello world en $@..."
	perl $<

postscript: $(SRC).ps
	@echo "Hello world en $@..."
	gs -sDEVICE=x11 $<

python: $(SRC).py
	@echo "Hello world en $@..."
	python $<

ruby: $(SRC).rb
	@echo "Hello world en $@..."
	ruby $<

rust: $(SRC).rs
	@echo "Hello world en $@..."
	rustc $< && ./$(EXE)

scheme: $(SRC).scheme
	@echo "Hello world en $@..."
	guile $<

sh: $(SRC).sh
	@echo "Hello world en $@..."
	sh $<

troff: $(SRC).troff
	@echo "Hello world en $@..."
	troff $<


clean:
	@echo "Limpiando..."
	rm -f $(EXE) HelloWorld.class
