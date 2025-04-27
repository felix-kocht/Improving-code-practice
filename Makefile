# Run the backend API server
run:
	uvicorn api.api:app --reload --port 8000

# Run all tests
test:
	pytest

# Format code
format:
	black src/ tests/

# Lint code
lint:
	flake8 src/ tests/

# Tunnel API for external access
tunnel:
	lt --port 8000

pre-commit:
	pre-commit run --all-files

freeze:
	pip freeze > requirements.txt

# Start server and tunnel together
run-and-tunnel:
	uvicorn api.api:app --reload --port 8000 & \
	sleep 2 && lt --port 8000