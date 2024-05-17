.PHONY: all clean test

all: build

build:
    @echo "Building service..."
    pip install -r requirements.txt
    make build

test:
    @echo "Running tests..."
    #test commands here
    make test

clean:
    @echo "Cleaning up..."
    #clean commands here
    make clean
