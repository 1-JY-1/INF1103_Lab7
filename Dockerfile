FROM python:3.11-slim
WORKDIR /app
COPY inventory.json inventory_manager.py mainprogram.py inventory.py product.py filehandling.py canbeshipped.py .
CMD ["python", "inventory_manager.py"]