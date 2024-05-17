.PHONY: all clean test

all: build

build:
    @echo "Building service..."
    pip install -r requirements.txt

test:
    @echo "Running tests..."
    # Add your test commands here

clean:
    @echo "Cleaning up..."
    # Add your clean commands here
